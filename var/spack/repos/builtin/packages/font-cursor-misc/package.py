# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FontCursorMisc(Package):
    """X.org cursor-misc font."""

    homepage = "http://cgit.freedesktop.org/xorg/font/cursor-misc"
    url      = "https://www.x.org/archive/individual/font/font-cursor-misc-1.0.3.tar.gz"

    version('1.0.3', 'a0bf70c7e498f1cd8e3fdf6154f2bb00')

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
