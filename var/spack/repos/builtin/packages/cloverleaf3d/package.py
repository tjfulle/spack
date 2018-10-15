# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import glob

from spack import *


class Cloverleaf3d(MakefilePackage):
    """Proxy Application. CloverLeaf3D is 3D version of the
       CloverLeaf mini-app. CloverLeaf is a mini-app that solves
       the compressible Euler equations on a Cartesian grid,
       using an explicit, second-order accurate method.
    """

    homepage = "http://uk-mac.github.io/CloverLeaf3D/"
    url      = "http://mantevo.org/downloads/releaseTarballs/miniapps/CloverLeaf3D/CloverLeaf3D-1.0.tar.gz"

    tags = ['proxy-app']

    version('1.0', '2e86cadd7612487f9da4ddeb1a6de939')

    variant('openacc', default=False, description='Enable OpenACC Support')

    depends_on('mpi')

    @property
    def type_of_build(self):
        build = 'ref'

        if '+openacc' in self.spec:
            build = 'OpenACC'

        return build

    @property
    def build_targets(self):
        targets = [
            'MPI_COMPILER={0}'.format(self.spec['mpi'].mpifc),
            'C_MPI_COMPILER={0}'.format(self.spec['mpi'].mpicc),
            '--directory=CloverLeaf3D_{0}'.format(self.type_of_build)
        ]

        if '%gcc' in self.spec:
            targets.append('COMPILER=GNU')
        elif '%cce' in self.spec:
            targets.append('COMPILER=CRAY')
        elif '%intel' in self.spec:
            targets.append('COMPILER=INTEL')
        elif '%pgi' in self.spec:
            targets.append('COMPILER=PGI')
        elif '%xl' in self.spec:
            targets.append('COMPILER=XLF')

        return targets

    def install(self, spec, prefix):
        # Manual Installation
        mkdirp(prefix.bin)
        mkdirp(prefix.doc.samples)

        install('README.md', prefix.doc)

        install('CloverLeaf3D_{0}/clover_leaf'.format(self.type_of_build),
                prefix.bin)
        install('CloverLeaf3D_{0}/clover.in'.format(self.type_of_build),
                prefix.bin)

        for f in glob.glob(
                'CloverLeaf3D_{0}/*.in'.format(self.type_of_build)):
            install(f, prefix.doc.samples)
