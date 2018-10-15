# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTestinfra(PythonPackage):
    """With Testinfra you can write unit tests in Python to test actual state
    of your servers configured by management tools like Salt, Ansible, Puppet,
    Chef and so on."""

    homepage = "https://testinfra.readthedocs.io"
    url      = "https://pypi.python.org/packages/source/t/testinfra/testinfra-1.11.1.tar.gz"

    version('1.13.0', '1e0a135c784207f8609e7730901f1291')
    version('1.12.0', '9784c01d7af3d624c6ec3cd25cce2011')
    version('1.11.1', 'c64ce6b16661d647c62c9508de419f5f')

    depends_on('py-setuptools', type='build')
    depends_on('py-importlib', when='^python@2.6.0:2.6.999', type=('build', 'run'))
    depends_on('py-pytest@:3.0.1,3.0.3:', type=('build', 'run'))
    depends_on('py-six@1.4:', type=('build', 'run'))

    # Required for testing remote systems
    depends_on('py-paramiko', type=('build', 'run'))

    # Required for parallel execution
    depends_on('py-pytest-xdist', type=('build', 'run'))
