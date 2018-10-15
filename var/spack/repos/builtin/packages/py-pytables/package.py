# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPytables(PythonPackage):
    """PyTables is a package for managing hierarchical datasets and designed to
    efficiently and easily cope with extremely large amounts of data."""
    homepage = "http://www.pytables.org/"
    url      = "https://github.com/PyTables/PyTables/archive/v.3.2.2.tar.gz"

    version('3.3.0', '056c161ae0fd2d6e585b766adacf3b0b',
            url='https://github.com/PyTables/PyTables/archive/v3.3.0.tar.gz')
    version('3.2.2', '7cbb0972e4d6580f629996a5bed92441')

    depends_on('hdf5@1.8.0:1.8.999')
    depends_on('py-numpy@1.8.0:', type=('build', 'run'))
    depends_on('py-numexpr@2.5.2:', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-setuptools', type='build')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('HDF5_DIR', self.spec['hdf5'].prefix)
