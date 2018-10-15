# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xphelloworld(AutotoolsPackage):
    """Xprint sample applications."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xphelloworld"
    url      = "https://www.x.org/archive/individual/app/xphelloworld-1.0.1.tar.gz"

    version('1.0.1', 'b1851337a8e850d5c8e5a5ca5e3033da')

    depends_on('libx11')
    depends_on('libxaw')
    depends_on('libxprintapputil')
    depends_on('libxprintutil')
    depends_on('libxp')
    depends_on('libxt')

    # FIXME: xphelloworld requires libxaw8, but libxaw only provides 6 and 7.
    # It looks like xprint support was removed from libxaw at some point.
    # But even the oldest version of libxaw doesn't build libxaw8.

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
