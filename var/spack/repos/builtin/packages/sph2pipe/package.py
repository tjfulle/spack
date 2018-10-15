# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sph2pipe(CMakePackage):
    """Sph2pipe is a portable tool for
    converting SPHERE files to other formats."""

    homepage = "https://www.ldc.upenn.edu/language-resources/tools/sphere-conversion-tools"
    url      = "https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/ctools/sph2pipe_v2.5.tar.gz"

    version('2.5', '771d9143e9aec0a22c6a14e138974be2')

    patch('cmake.patch')
