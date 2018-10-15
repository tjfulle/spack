# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Precice(CMakePackage):
    """preCICE (Precise Code Interaction Coupling Environment) is a
    coupling library for partitioned multi-physics simulations.
    Partitioned means that preCICE couples existing programs (solvers)
    capable of simulating a subpart of the complete physics involved in
    a simulation."""

    homepage = 'https://www.precice.org'
    git      = 'https://github.com/precice/precice.git'

    # Skip version 1.1.1 entirely, the cmake was lacking install.
    version('develop', branch='develop')

    variant('mpi', default=True, description='Enable MPI support')
    variant('petsc', default=False, description='Enable PETSc support')
    variant('python', default=False, description='Enable Python support')
    variant('shared', default=True, description='Build shared libraries')

    # Not yet
#    variant(
#        'float', default=False,
#        description='Use single precision for field data exchange')
#    variant(
#        'int64',
#        default=False, description='Use 64-bit integers for indices')

    depends_on('cmake@3.5:', type='build')
    depends_on('boost@1.60.0:')
    depends_on('eigen@3.2:')
    # Implicit via eigen, don't over-constrain: depends_on('libxml2')
    depends_on('mpi', when='+mpi')
    depends_on('petsc', when='+petsc')
    depends_on('python@2.7', when='+python', type=('build', 'run'))

    def cmake_args(self):
        """Populate cmake arguments for precice."""
        spec = self.spec

        def variant_bool(feature, on='ON', off='OFF'):
            """Ternary for spec variant to ON/OFF string"""
            if feature in spec:
                return on
            return off

        cmake_args = [
            '-DMPI:BOOL=%s' % variant_bool('+mpi'),
            '-DPETSC:BOOL=%s' % variant_bool('+petsc'),
            '-DPYTHON:BOOL=%s' % variant_bool('+python'),
            '-DBUILD_SHARED_LIBS:BOOL=%s' % variant_bool('+shared'),
        ]
        return cmake_args
