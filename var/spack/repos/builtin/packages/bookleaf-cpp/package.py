# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class BookleafCpp(CMakePackage):
    """BookLeaf is a 2D unstructured hydrodynamics mini-app."""

    homepage = "https://github.com/UK-MAC/BookLeaf_Cpp"
    url      = "https://github.com/UK-MAC/BookLeaf_Cpp/archive/v2.0.tar.gz"
    git      = "https://github.com/UK-MAC/BookLeaf_Cpp.git"

    version('develop', branch='develop')
    version('2.0.1', '34a5a9e7b2b5ffc98562656a4406ba5b')
    version('2.0',   '69819ebcbae5eaa63d1a4de2c77cac85')

    variant('typhon', default=True, description='Use Typhon')
    variant('parmetis', default=False, description='Use ParMETIS')
    variant('silo', default=False, description='Use Silo')
    variant('caliper', default=False, description='Use Caliper')

    depends_on('caliper', when='+caliper')
    depends_on('parmetis', when='+parmetis')
    depends_on('silo', when='+silo')
    depends_on('typhon', when='+typhon')
    depends_on('mpi', when='+typhon')
    depends_on('yaml-cpp@0.6.0:')

    def cmake_args(self):
        spec = self.spec
        cmake_args = []

        if '+typhon' in spec:
            cmake_args.append('-DENABLE_TYPHON=ON')

        if '+parmetis' in spec:
            cmake_args.append('-DENABLE_PARMETIS=ON')

        if '+silo' in spec:
            cmake_args.append('-DENABLE_SILO=ON')

        if '+caliper' in spec:
            cmake_args.append('-DENABLE_CALIPER=ON')

        return cmake_args
