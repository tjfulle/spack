# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from six.moves.urllib.parse import urlparse
from os.path import split


class Miniconda3(Package):
    """The minimalist bootstrap toolset for conda and Python3."""

    homepage = "https://conda.io/miniconda.html"
    url      = "https://repo.continuum.io/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh"

    version('4.5.4', 'a946ea1d0c4a642ddf0c3a26a18bb16d', expand=False)
    version('4.3.30', '0b80a152332a4ce5250f3c09589c7a81', expand=False)
    version('4.3.14', 'fc6fc37479e3e3fcf3f9ba52cae98991', expand=False)
    version('4.3.11', '1924c8d9ec0abf09005aa03425e9ab1a', expand=False)

    def install(self, spec, prefix):
        # peel the name of the script out of the url
        result = urlparse(self.url)
        dir, script = split(result.path)
        bash = which('bash')
        bash(script, '-b', '-f', '-p', self.prefix)
