#!/usr/bin/env python
"""Check that the lowest CUDA architecture built into a set of binaries matches
the architecture the recipe claims to support.

Usage:
    python check_cuda_arch.py <file-or-glob> [<file-or-glob> ...]

The expected architecture is read from the ``cuda_arch_version`` environment variable (dotted,
e.g. ``8.2``) unless ``--arch-min`` is given.  ``cuobjdump`` must be on PATH.

The minimum for the group is the highest of the per-file minimums: a GPU below that
architecture cannot run at least one of the binaries, so the group as a whole does not
support it.  A file that happens to carry kernels for older GPUs than the rest therefore
does not drag the floor down.

Both SASS (``sm_XX``) and PTX (``compute_XX``) targets count; arch-conditional targets
(``sm_90a``, ``sm_100f``) count as their base architecture. Files without device code are
skipped.  The report lists SASS and PTX separately for the log, but the check uses the
lowest of the two.

Exit codes: 0 = match, 1 = mismatch or unreadable binary, 2 = bad invocation.
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

# sm_90, compute_90, sm_90a, sm_100f, ...
ARCH_RE = re.compile(r"(?:sm|compute)_(\d{2,3})[af]?(?![0-9A-Za-z_])")
ARCH_MIN_RE = re.compile(r"^([1-9][0-9]*)\.([0-9])$")
NO_DEVICE_CODE = "does not contain device code"


def parse_arch(text):
    """Convert a dotted architecture such as '8.2' into the key 82."""
    match = ARCH_MIN_RE.match(text.strip())
    if match is None:
        return None
    return int(match.group(1)) * 10 + int(match.group(2))


def format_arch(key):
    """Convert an architecture key such as 82 into the dotted form '8.2'."""
    return "{}.{}".format(key // 10, key % 10)


def expand(patterns):
    """Expand globs, keeping literal arguments that contain no glob characters.

    Unix shells expand globs themselves; cmd.exe does not.  Literal arguments are kept even
    when they do not exist, so that a mistyped path is reported by name instead of being
    silently dropped; a glob that matches nothing is reported as "no files matched".
    """
    paths = []
    for pattern in patterns:
        if any(char in pattern for char in "*?["):
            paths.extend(sorted(glob.glob(pattern)))
        else:
            paths.append(pattern)
    return paths


def architectures(cuobjdump, path, flag):
    """Return (sorted arch keys, cuobjdump output) for one listing mode.

    ``flag`` is ``--list-elf`` for SASS or ``--list-ptx`` for PTX.  The two are
    listed separately because cuobjdump names both kinds of image ``sm_XX``, so
    they cannot be told apart once the output is merged.
    """
    result = subprocess.run(
        [cuobjdump, flag, path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    keys = {int(digits) for digits in ARCH_RE.findall(result.stdout)}
    return sorted(keys), result.stdout


def render(keys):
    """Render architecture keys for the report, e.g. '7.5 8.0 9.0'."""
    return " ".join(format_arch(key) for key in keys) or "-"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Check that the lowest CUDA architecture in a set of binaries "
            "matches the expected minimum."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        metavar="FILE",
        help="binaries to inspect; globs are expanded",
    )
    parser.add_argument(
        "--arch-min",
        default=os.environ.get("cuda_arch_version"),
        help="expected minimum architecture, dotted (default: $cuda_arch_version)",
    )
    args = parser.parse_args(argv)

    if not args.arch_min:
        parser.error("cuda_arch_version is not set and --arch-min was not given")

    expected = parse_arch(args.arch_min)
    if expected is None:
        parser.error(
            'cuda_arch_version must look like 8.2, got "{}"'.format(args.arch_min)
        )

    cuobjdump = shutil.which("cuobjdump")
    if cuobjdump is None:
        parser.error("cuobjdump was not found on PATH")

    paths = expand(args.paths)
    if not paths:
        parser.error("no files matched")

    print(
        "Checking CUDA architectures against cuda_arch_version={}".format(args.arch_min)
    )

    failed = False
    found = []

    for path in paths:
        name = os.path.basename(path)
        sass, sass_output = architectures(cuobjdump, path, "--list-elf")
        ptx, ptx_output = architectures(cuobjdump, path, "--list-ptx")
        keys = sorted(set(sass) | set(ptx))
        if not keys:
            output = sass_output + ptx_output
            if NO_DEVICE_CODE in output:
                print("  {} : no device code, skipped".format(name))
            else:
                print("  {} : ERROR - could not read device code".format(name))
                print(output.rstrip("\n"))
                failed = True
            continue
        # SASS and PTX are reported separately for the log; the check itself
        # uses the lowest of the two.
        print("  {} :".format(name))
        print("      SASS : {}".format(render(sass)))
        print("      PTX  : {}".format(render(ptx)))
        found.append((keys[0], name))

    if not found:
        print(
            "ERROR: none of the {} file(s) contain CUDA device code".format(len(paths))
        )
        return 1

    # The group is only usable on a GPU that every binary supports, so the floor
    # is the highest of the per-file minimums, not the lowest.
    minimum, minimum_path = max(found, key=lambda item: item[0])

    print(
        "minimum = {} (set by {})   expected = {}".format(
            format_arch(minimum), minimum_path, format_arch(expected)
        )
    )

    if failed:
        print("FAILED: one or more files could not be inspected")
        return 1

    if minimum != expected:
        print(
            "FAILED: minimum supported architecture is {}, expected {}".format(
                format_arch(minimum), format_arch(expected)
            )
        )
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
