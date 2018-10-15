# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NcbiMagicblast(AutotoolsPackage):
    """Magic-BLAST is a tool for mapping large next-generation RNA or DNA
    sequencing runs against a whole genome or transcriptome. """

    homepage = "https://ncbi.github.io/magicblast/"
    url      = "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/1.3.0/ncbi-magicblast-1.3.0-src.tar.gz"

    version('1.3.0', '2615b919c1fe1bf7dc3d816392ab4420')

    depends_on('lmdb')
    configure_directory = 'c++'

    def configure_args(self):
        return ['--without-internal']
