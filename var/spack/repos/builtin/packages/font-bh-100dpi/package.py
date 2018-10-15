# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FontBh100dpi(Package):
    """X.org bh-100dpi font."""

    homepage = "http://cgit.freedesktop.org/xorg/font/bh-100dpi"
    url      = "https://www.x.org/archive/individual/font/font-bh-100dpi-1.0.3.tar.gz"

    version('1.0.3', '09e63a5608000531179e1ab068a35878')

    depends_on('font-util')

    depends_on('fontconfig', type='build')
    depends_on('mkfontdir', type='build')
    depends_on('bdftopcf', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    def install(self, spec, prefix):
        configure('--prefix={0}'.format(prefix))

        make()
        make('install')

        # `make install` copies the files to the font-util installation.
        # Create a fake directory to convince Spack that we actually
        # installed something.
        mkdir(prefix.lib)
