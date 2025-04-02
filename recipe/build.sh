#!/usr/bin/env bash
set -e

check-glibc lib/lib*.so*

mkdir -p $PREFIX/include
cp include/cudnn*.h $PREFIX/include/

mkdir -p $PREFIX/lib
mv lib/libcudnn*.so* $PREFIX/lib/

