#!/usr/bin/env bash
set -e

check-glibc lib/lib*.so*

for f in lib/lib*.so.*.*; do
  echo "$f"
  cuobjdump -ptx "$f" | grep "arch =" | sort | uniq
done

mkdir -p $PREFIX/include
cp -vp include/cudnn*.h $PREFIX/include/

mkdir -p $PREFIX/lib
cp -vpP lib/libcudnn*.so* $PREFIX/lib/
