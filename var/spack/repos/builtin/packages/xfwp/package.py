# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xfwp(AutotoolsPackage):
    """xfwp proxies X11 protocol connections, such as through a firewall."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xfwp"
    url      = "https://www.x.org/archive/individual/app/xfwp-1.0.3.tar.gz"

    version('1.0.3', 'e23cc01894ae57e5959ca6a56d0f4f94')

    depends_on('libice')

    depends_on('xproto', type='build')
    depends_on('xproxymanagementprotocol', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    # FIXME: fails with the error message:
    # io.c:1039:7: error: implicit declaration of function 'swab'
