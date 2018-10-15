# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Diamond(CMakePackage):
    """DIAMOND is a sequence aligner for protein and translated DNA searches,
    designed for high performance analysis of big sequence data."""

    homepage = "https://ab.inf.uni-tuebingen.de/software/diamond"
    url      = "https://github.com/bbuchfink/diamond/archive/v0.9.14.tar.gz"

    version('0.9.21', '6f3c53520f3dad37dfa3183d61f21dd5')
    version('0.9.20', 'd73f4955909d16456d83b30d9c294b2b')
    version('0.9.19', '8565d2d3bfe407ee778eeabe7c6a7fde')
    version('0.9.14', 'b9e1d0bc57f07afa05dbfbb53c31aae2')
    version('0.8.38', 'd4719c8a7947ba9f743446ac95cfe644')
    version('0.8.26', '0d86305ab25cc9b3bb3564188d30fff2')

    depends_on('zlib')
