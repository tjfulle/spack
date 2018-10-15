# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlSwissknife(PerlPackage):
    """An object-oriented Perl library to handle Swiss-Prot entries"""

    homepage = "http://swissknife.sourceforge.net"
    url      = "https://downloads.sourceforge.net/project/swissknife/swissknife/1.75/Swissknife_1.75.tar.gz"

    version('1.75', '09d008cb1d1d211ae4eb9f087c213edf')

    depends_on('perl-module-build', type='build')
