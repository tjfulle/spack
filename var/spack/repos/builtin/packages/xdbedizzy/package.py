# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xdbedizzy(AutotoolsPackage):
    """xdbedizzy is a demo of the X11 Double Buffer Extension (DBE)
    creating a double buffered spinning scene."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xdbedizzy"
    url      = "https://www.x.org/archive/individual/app/xdbedizzy-1.1.0.tar.gz"

    version('1.1.0', '969be2f6bc62455431ab027f99720dc3')

    depends_on('libx11')
    depends_on('libxext')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
