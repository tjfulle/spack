# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fastqvalidator(MakefilePackage):
    """The fastQValidator validates the format of fastq files."""

    homepage = "http://genome.sph.umich.edu/wiki/FastQValidator"
    git      = "https://github.com/statgen/fastQValidator.git"

    version('2017-01-10', commit='6d619a34749e9d33c34ef0d3e0e87324ca77f320')

    resource(
        name='libStatGen',
        git='https://github.com/statgen/libStatGen.git',
        commit='9db9c23e176a6ce6f421a3c21ccadedca892ac0c'
    )

    @property
    def build_targets(self):
        return ['LIB_PATH_GENERAL={0}'.format(
                join_path(self.stage.source_path, 'libStatGen'))]

    @property
    def install_targets(self):
        return [
            'INSTALLDIR={0}'.format(self.prefix.bin),
            'LIB_PATH_GENERAL={0}'.format(
                join_path(self.stage.source_path, 'libStatGen')),
            'install'
        ]
