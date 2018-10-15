# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RApe(RPackage):
    """Functions for reading, writing, plotting, and manipulating phylogenetic
    trees, analyses of comparative data in a phylogenetic framework, ancestral
    character analyses, analyses of diversification and macroevolution,
    computing distances from DNA sequences, reading and writing nucleotide
    sequences as well as importing from BioConductor, and several tools such
    as Mantel's test, generalized skyline plots, graphical exploration of
    phylogenetic data (alex, trex, kronoviz), estimation of absolute
    evolutionary rates and clock-like trees using mean path lengths and
    penalized likelihood, dating trees with non-contemporaneous sequences,
    translating DNA into AA sequences, and assessing sequence alignments.
    Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
    triangle methods, and several methods handling incomplete distance
    matrices (NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some
    functions call external applications (PhyML, Clustal, T-Coffee, Muscle)
    whose results are returned into R."""

    homepage = "http://ape-package.ird.fr/"
    url      = "https://cran.r-project.org/src/contrib/ape_4.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/ape"

    version('5.0', '82fd2786a502f070ca020797f7b19fa4')
    version('4.1', 'a9ed416d6d172d4b9682556cf692d7c2')

    depends_on('r@3.2:')
    depends_on('r-nlme', type=('build', 'run'))
    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
