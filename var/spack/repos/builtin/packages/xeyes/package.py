# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xeyes(AutotoolsPackage):
    """xeyes - a follow the mouse X demo, using the X SHAPE extension"""

    homepage = "http://cgit.freedesktop.org/xorg/app/xeyes"
    url      = "https://www.x.org/archive/individual/app/xeyes-1.1.1.tar.gz"

    version('1.1.1', '2c0522bce5c61bbe784d2b3491998d31')

    depends_on('libx11')
    depends_on('libxt')
    depends_on('libxext')
    depends_on('libxmu')
    depends_on('libxrender@0.4:')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
