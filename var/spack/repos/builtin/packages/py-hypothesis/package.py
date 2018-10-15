# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyHypothesis(PythonPackage):
    """A library for property based testing."""

    homepage = "https://github.com/HypothesisWorks/hypothesis-python"
    url      = "https://pypi.io/packages/source/h/hypothesis/hypothesis-3.7.0.tar.gz"

    import_modules = [
        'hypothesis', 'hypothesis.searchstrategy', 'hypothesis.extra',
        'hypothesis.tools', 'hypothesis.utils', 'hypothesis.vendor',
        'hypothesis.internal', 'hypothesis.internal.conjecture'
    ]

    # TODO: Add missing dependency required to import hypothesis.extra.django

    version('3.7.0', '4afb25fa6785fceac034b63eaa2dfe28')

    depends_on('py-setuptools', type='build')
    depends_on('py-enum34', type=('build', 'run'), when='^python@:2')
