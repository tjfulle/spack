# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLarkParser(PythonPackage):
    """Lark is a modern general-purpose parsing library for Python."""

    homepage = "https://github.com/lark-parser/lark/"
    url      = "https://pypi.io/packages/source/l/lark-parser/lark-parser-0.6.2.tar.gz"

    version('0.6.2', '675058937a7f41e661bcf2b3bfdb7ceb')

    depends_on('py-setuptools', type='build')
