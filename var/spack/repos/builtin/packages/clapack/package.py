# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Clapack(MakefilePackage):
    """CLAPACK is a f2c'ed version of LAPACK.

       The CLAPACK library was built using a Fortran to C conversion utility
    called f2c.  The entire Fortran 77 LAPACK library is run through f2c to
    obtain C code, and then modified to improve readability.  CLAPACK's goal
    is to provide LAPACK for someone who does not have access to a Fortran
    compiler."""

    homepage = "http://www.netlib.org/clapack/"
    url      = "http://www.netlib.org/clapack/clapack.tgz"

    version('3.2.1', '040da31f3a7d4fbc9ac376c748d18d1f')

    variant('external-blas', default=True,
            description='Build with external BLAS (ATLAS here).')

    depends_on('atlas', when='+external-blas')

    def edit(self, spec, prefix):
        copy('make.inc.example', 'make.inc')
        if '+external-blas' in spec:
            make_inc = FileFilter('make.inc')
            make_inc.filter(r'^BLASLIB.*',
                            'BLASLIB = ../../libcblaswr.a -lcblas -latlas')
            makefile = FileFilter('Makefile')
            makefile.filter(r'^lib.*',
                            'lib: variants lapacklib tmglib')

    def build(self, spec, prefix):
        make('f2clib')
        make('cblaswrap' if '+external-blas' in spec else 'blaslib')
        make('lib')

    def install(self, spec, prefix):
        install_tree('.', prefix)
