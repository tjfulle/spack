# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libuv(AutotoolsPackage):
    """Multi-platform library with a focus on asynchronous IO"""
    homepage = "http://libuv.org"
    url      = "https://github.com/libuv/libuv/archive/v1.9.0.tar.gz"

    version('1.9.0', '14737f9c76123a19a290dabb7d1cd04c')

    depends_on('automake', type='build')
    depends_on('autoconf', type='build')
    depends_on('libtool', type='build')

    def autoreconf(self, spec, prefix):
        # This is needed because autogen.sh generates on-the-fly
        # an m4 macro needed during configuration
        bash = which("bash")
        bash('autogen.sh')
