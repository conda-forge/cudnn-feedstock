#!/usr/bin/env bash
set -e

check-glibc lib/lib*.so*

mkdir -p $PREFIX/include
cp -vp include/cudnn*.h $PREFIX/include/

mkdir -p $PREFIX/lib
cp -vpP lib/libcudnn*.so* $PREFIX/lib/

python ${RECIPE_DIR}/check_cuda_arch.py ${PREFIX}/lib/libcudnn*.so
