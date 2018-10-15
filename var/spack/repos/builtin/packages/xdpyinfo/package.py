# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xdpyinfo(AutotoolsPackage):
    """xdpyinfo is a utility for displaying information about an X server.

    It is used to examine the capabilities of a server, the predefined
    values for various parameters used in communicating between clients
    and the server, and the different types of screens, visuals, and X11
    protocol extensions that are available."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xdpyinfo"
    url      = "https://www.x.org/archive/individual/app/xdpyinfo-1.3.2.tar.gz"

    version('1.3.2', 'dab410719d36c9df690cf3a8cd7d117e')

    depends_on('libxext')
    depends_on('libx11')
    depends_on('libxtst')
    depends_on('libxcb')

    depends_on('xproto@7.0.22:', type='build')
    depends_on('recordproto', type='build')
    depends_on('inputproto', type='build')
    depends_on('fixesproto', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
