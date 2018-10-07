# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xmodmap(AutotoolsPackage):
    """The xmodmap program is used to edit and display the keyboard modifier
    map and keymap table that are used by client applications to convert
    event keycodes into keysyms.  It is usually run from the user's
    session startup script to configure the keyboard according to personal
    tastes."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xmodmap"
    url      = "https://www.x.org/archive/individual/app/xmodmap-1.0.9.tar.gz"

    version('1.0.9', '771cf86bcdc3589e7add2e761f675099')

    depends_on('libx11')

    depends_on('xproto@7.0.25:', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
