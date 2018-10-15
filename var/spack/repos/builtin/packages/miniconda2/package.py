# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from six.moves.urllib.parse import urlparse
from os.path import split


class Miniconda2(Package):
    """The minimalist bootstrap toolset for conda and Python2."""

    homepage = "https://conda.io/miniconda.html"
    url      = "https://repo.continuum.io/miniconda/Miniconda2-4.3.11-Linux-x86_64.sh"

    version('4.5.4', '8a1c02f6941d8778f8afad7328265cf5', expand=False)
    version('4.3.30', 'bd1655b4b313f7b2a1f2e15b7b925d03', expand=False)
    version('4.3.14', '8cb075cf5462480980ef2373ad9fad38', expand=False)
    version('4.3.11', 'd573980fe3b5cdf80485add2466463f5', expand=False)

    def install(self, spec, prefix):
        # peel the name of the script out of the url
        result = urlparse(self.url)
        dir, script = split(result.path)
        bash = which('bash')
        bash(script, '-b', '-f', '-p', self.prefix)
