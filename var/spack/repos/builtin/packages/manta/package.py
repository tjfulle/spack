# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Manta(CMakePackage):
    """Structural variant and indel caller for mapped sequencing data"""

    homepage = "https://github.com/Illumina/manta"
    url      = "https://github.com/Illumina/manta/releases/download/v1.3.2/manta-1.3.2.release_src.tar.bz2"

    depends_on('boost@1.58.0:', type='build')
    depends_on('cmake@2.8.12:', type='build')
    depends_on('python@2.7.0:2.7.999', type=('build', 'run'))

    version('1.4.0', '582d10f3bc56aecfa5c24931af3742b4')
    version('1.3.2', '83f43fe1a12605c1e9803d1020b24bd1')
    version('1.3.1', 'e315caff775878872ee300ed34e8adae')
    version('1.3.0', '1243e2bb58ca7c9d69bbfbe528f492ec')
