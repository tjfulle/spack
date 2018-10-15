# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMock(PythonPackage):
    """mock is a library for testing in Python. It allows you to replace parts
    of your system under test with mock objects and make assertions about how
    they have been used."""

    homepage = "https://github.com/testing-cabal/mock"
    url      = "https://pypi.io/packages/source/m/mock/mock-1.3.0.tar.gz"

    version('2.0.0', '0febfafd14330c9dcaa40de2d82d40ad')
    version('1.3.0', '73ee8a4afb3ff4da1b4afa287f39fdeb')

    depends_on('py-pbr', type=('build', 'run'))
    depends_on('py-setuptools@17.1:', type='build')
