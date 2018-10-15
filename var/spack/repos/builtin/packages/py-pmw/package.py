# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPmw(PythonPackage):
    """Pmw is a toolkit for building high-level compound widgets, or
       megawidgets, constructed using other widgets as component parts."""
    homepage = "https://pypi.python.org/pypi/Pmw"
    url      = "https://pypi.io/packages/source/P/Pmw/Pmw-2.0.0.tar.gz"

    version('2.0.0', 'c7c3f26c4f5abaa99807edefee578fc0')
