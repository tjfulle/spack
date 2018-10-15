# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ravel(CMakePackage):
    """Ravel is a parallel communication trace visualization tool that
       orders events according to logical time."""

    homepage = "https://github.com/llnl/ravel"
    url = 'https://github.com/llnl/ravel/archive/v1.0.0.tar.gz'

    version('1.0.0', 'b25fece58331c2adfcce76c5036485c2')

    depends_on('cmake@2.8.9:', type='build')

    depends_on('muster@1.0.1:')
    depends_on('otf')
    depends_on('otf2')
    depends_on('qt@5:')

    def cmake_args(self):
        return ['-Wno-dev']
