# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mitos(CMakePackage):
    """Mitos is a library and a tool for collecting sampled memory
    performance data to view with MemAxes"""

    homepage = "https://github.com/llnl/Mitos"
    url      = "https://github.com/LLNL/Mitos/archive/v0.9.1.tar.gz"
    git      = "https://github.com/llnl/Mitos.git"

    version('0.9.2', commit='8cb143a2e8c00353ff531a781a9ca0992b0aaa3d')
    version('0.9.1', 'c6cb57f3cae54f5157affd97ef7ef79e')

    depends_on('dyninst@8.2.1:')
    depends_on('hwloc')
    depends_on('mpi')
    depends_on('cmake@2.8:', type='build')
