#!/usr/bin/env bash
set -e

mkdir -p $PREFIX/include
cp -vp include/cudnn*.h $PREFIX/include/

mkdir -p $PREFIX/lib
cp -vpP lib/libcudnn*.so* $PREFIX/lib/

check-glibc $PREFIX/lib/libcudnn*.so*