About cudnn-feedstock
=====================

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/cudnn-feedstock/blob/main/LICENSE.txt)

Home: https://developer.nvidia.com/cudnn

Package license: [LicenseRef-cuDNN-Software-License-Agreement](https://docs.nvidia.com/deeplearning/cudnn/sla/index.html)

Summary: NVIDIA's cuDNN deep neural network acceleration library

Development: https://developer.nvidia.com/rdp/cudnn-download

Documentation: https://docs.nvidia.com/deeplearning/cudnn/

NVIDIA CUDA Deep Neural Network (cuDNN) is a GPU-accelerated library of
primitives for deep neural networks. It provides highly tuned
implementations of routines arising frequently in DNN applications.

License Agreements:- The packages are governed by the NVIDIA cuDNN
Software License Agreement (EULA). By downloading and using the packages,
you accept the terms and conditions of the NVIDIA cuDNN EULA -
https://docs.nvidia.com/deeplearning/cudnn/sla/index.html


Current build status
====================


<table>
    
  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=11465&branchName=main">
            <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/cudnn-feedstock?branchName=main">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>linux_64_cuda_compiler_version12.9</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=11465&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/cudnn-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_64_cuda_compiler_version12.9" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_aarch64_arm_variant_typesbsacuda_compiler_version12.9</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=11465&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/cudnn-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_aarch64_arm_variant_typesbsacuda_compiler_version12.9" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_aarch64_arm_variant_typetegracuda_compiler_version12.9</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=11465&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/cudnn-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_aarch64_arm_variant_typetegracuda_compiler_version12.9" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>win_64_cuda_compiler_version12.9</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=11465&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/cudnn-feedstock?branchName=main&jobName=win&configuration=win%20win_64_cuda_compiler_version12.9" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-cudnn-green.svg)](https://anaconda.org/conda-forge/cudnn) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/cudnn.svg)](https://anaconda.org/conda-forge/cudnn) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/cudnn.svg)](https://anaconda.org/conda-forge/cudnn) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/cudnn.svg)](https://anaconda.org/conda-forge/cudnn) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libcudnn-green.svg)](https://anaconda.org/conda-forge/libcudnn) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libcudnn.svg)](https://anaconda.org/conda-forge/libcudnn) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libcudnn.svg)](https://anaconda.org/conda-forge/libcudnn) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libcudnn.svg)](https://anaconda.org/conda-forge/libcudnn) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-libcudnn--dev-green.svg)](https://anaconda.org/conda-forge/libcudnn-dev) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/libcudnn-dev.svg)](https://anaconda.org/conda-forge/libcudnn-dev) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/libcudnn-dev.svg)](https://anaconda.org/conda-forge/libcudnn-dev) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/libcudnn-dev.svg)](https://anaconda.org/conda-forge/libcudnn-dev) |

Installing cudnn
================

Installing `cudnn` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, `cudnn, libcudnn, libcudnn-dev` can be installed with `conda`:

```
conda install cudnn libcudnn libcudnn-dev
```

or with `mamba`:

```
mamba install cudnn libcudnn libcudnn-dev
```

It is possible to list all of the versions of `cudnn` available on your platform with `conda`:

```
conda search cudnn --channel conda-forge
```

or with `mamba`:

```
mamba search cudnn --channel conda-forge
```

Alternatively, `mamba repoquery` may provide more information:

```
# Search all versions available on your platform:
mamba repoquery search cudnn --channel conda-forge

# List packages depending on `cudnn`:
mamba repoquery whoneeds cudnn --channel conda-forge

# List dependencies of `cudnn`:
mamba repoquery depends cudnn --channel conda-forge
```


About conda-forge
=================

[![Powered by
NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[Azure](https://azure.microsoft.com/en-us/services/devops/), [GitHub](https://github.com/),
[CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/),
[Drone](https://cloud.drone.io/welcome), and [TravisCI](https://travis-ci.com/)
it is possible to build and upload installable packages to the
[conda-forge](https://anaconda.org/conda-forge) [anaconda.org](https://anaconda.org/)
channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance,
[conda-smithy](https://github.com/conda-forge/conda-smithy) has been developed.
Using the ``conda-forge.yml`` within this repository, it is possible to re-render all of
this feedstock's supporting files (e.g. the CI configuration files) with ``conda smithy rerender``.

For more information, please check the [conda-forge documentation](https://conda-forge.org/docs/).

Terminology
===========

**feedstock** - the conda recipe (raw material), supporting scripts and CI configuration.

**conda-smithy** - the tool which helps orchestrate the feedstock.
                   Its primary use is in the construction of the CI ``.yml`` files
                   and simplify the management of *many* feedstocks.

**conda-forge** - the place where the feedstock and smithy live and work to
                  produce the finished article (built conda distributions)


Updating cudnn-feedstock
========================

If you would like to improve the cudnn recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`conda-forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `conda-forge` channel.
Note that all branches in the conda-forge/cudnn-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks, and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@adibbley](https://github.com/adibbley/)
* [@bdice](https://github.com/bdice/)
* [@billysuh7](https://github.com/billysuh7/)
* [@conda-forge/cuda](https://github.com/orgs/conda-forge/teams/cuda/)
* [@jakirkham](https://github.com/jakirkham/)
* [@vyasr](https://github.com/vyasr/)

