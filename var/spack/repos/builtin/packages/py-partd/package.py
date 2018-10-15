# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPartd(PythonPackage):
    """Key-value byte store with appendable values."""

    homepage = "http://github.com/dask/partd/"
    url      = "https://pypi.io/packages/source/p/partd/partd-0.3.8.tar.gz"

    import_modules = ['partd']

    version('0.3.8', '554d0e6511c0df4c907f034858be847f')

    depends_on('py-setuptools', type='build')
    depends_on('py-locket', type=('build', 'run'))
    depends_on('py-toolz', type=('build', 'run'))
