# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Numactl(AutotoolsPackage):
    """NUMA support for Linux"""

    homepage = "http://oss.sgi.com/projects/libnuma/"
    url      = "https://github.com/numactl/numactl/archive/v2.0.11.tar.gz"

    version('2.0.11',     'b56d2367217cde390b4d8087e00773b8')

    patch('numactl-2.0.11-sysmacros.patch', when="@2.0.11")

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
