# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pplacer(Package):
    """Pplacer places query sequences on a fixed reference phylogenetic tree
       to maximize phylogenetic likelihood or posterior probability according
       to a reference alignment. Pplacer is designed to be fast, to give
       useful information about uncertainty, and to offer advanced
       visualization and downstream analysis.
    """

    homepage = "http://matsen.fhcrc.org/pplacer/"
    url      = "https://github.com/matsen/pplacer/releases/download/v1.1.alpha19/pplacer-linux-v1.1.alpha19.zip"

    version('1.1.alpha19', 'e6b78604882d41d4bf13592c7edebfa2')

    def install(self, spec, prefix):
        install_tree('scripts', prefix.bin)
        force_remove(join_path(prefix.bin, 'setup.py'))
        install('guppy', prefix.bin)
        install('pplacer', prefix.bin)
        install('rppr', prefix.bin)
