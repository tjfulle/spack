# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bdftopcf(AutotoolsPackage):
    """bdftopcf is a font compiler for the X server and font server.  Fonts
    in Portable Compiled Format can be read by any architecture, although
    the file is structured to allow one particular architecture to read
    them directly without reformatting.  This allows fast reading on the
    appropriate machine, but the files are still portable (but read more
    slowly) on other machines."""

    homepage = "http://cgit.freedesktop.org/xorg/app/bdftopcf"
    url      = "https://www.x.org/archive/individual/app/bdftopcf-1.0.5.tar.gz"

    version('1.0.5', '456416d33e0d41a96b5a3725d99e1be3')

    depends_on('libxfont')

    depends_on('pkgconfig', type='build')
    depends_on('xproto', type='build')
    depends_on('fontsproto', type='build')
    depends_on('util-macros', type='build')
