# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RReordercluster(RPackage):
    """Tools for performing the leaf reordering for the dendrogram
    that preserves the hierarchical clustering result and at the
    same time tries to group instances from the same class together."""

    homepage = "https://cran.r-project.org/package=ReorderCluster"
    url      = "https://cran.rstudio.com/src/contrib/ReorderCluster_1.0.tar.gz"

    version('1.0', '67ba34acb15dda75389a822bd2fdd31a')

    depends_on('r-gplots', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
