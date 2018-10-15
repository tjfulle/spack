# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libbeato(AutotoolsPackage):
    """libbeato is a C library containing routines for various uses in Genomics,
    and includes a copy of the freeware portion of the C library
    from UCSC's Genome Browser Group."""

    homepage = "https://github.com/CRG-Barcelona/libbeato"
    url      = "https://github.com/CRG-Barcelona/libbeato/archive/master.tar.gz"

    version('master', 'ee6f0f0f3f09c4f601fcfed3b13e7395')
