# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libuuid(AutotoolsPackage):
    """Portable uuid C library"""

    homepage = "http://sourceforge.net/projects/libuuid/"
    url      = "http://downloads.sourceforge.net/project/libuuid/libuuid-1.0.3.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Flibuuid%2F&ts=1433881396&use_mirror=iweb"

    version('1.0.3', 'd44d866d06286c08ba0846aba1086d68')
