# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGtools(RPackage):
    """Functions to assist in R programming, including: - assist in developing,
    updating, and maintaining R and R packages ('ask', 'checkRVersion',
    'getDependencies', 'keywords', 'scat'), - calculate the logit and inverse
    logit transformations ('logit', 'inv.logit'), - test if a value is missing,
    empty or contains only NA and NULL values ('invalid'), - manipulate R's
    .Last function ('addLast'), - define macros ('defmacro'), - detect odd and
    even integers ('odd', 'even'), - convert strings containing non-ASCII
    characters (like single quotes) to plain ASCII ('ASCIIfy'), - perform a
    binary search ('binsearch'), - sort strings containing both numeric and
    character components ('mixedsort'), - create a factor variable from the
    quantiles of a continuous variable ('quantcut'), - enumerate permutations
    and combinations ('combinations', 'permutation'), - calculate and convert
    between fold-change and log-ratio ('foldchange', 'logratio2foldchange',
    'foldchange2logratio'), - calculate probabilities and generate random
    numbers from Dirichlet distributions ('rdirichlet', 'ddirichlet'), - apply
    a function over adjacent subsets of a vector ('running'), - modify the
    TCP\_NODELAY ('de-Nagle') flag for socket objects, - efficient 'rbind' of
    data frames, even if the column names don't match ('smartbind'), - generate
    significance stars from p-values ('stars.pval'), - convert characters
    to/from ASCII codes."""

    homepage = "https://cran.r-project.org/package=gtools"
    url      = "https://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/gtools"

    version('3.5.0', '45f8800c0336d35046641fbacc56bdbb')
