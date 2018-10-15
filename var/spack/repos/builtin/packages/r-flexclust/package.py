# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFlexclust(RPackage):
    """The main function kcca implements a general framework for k-centroids
    cluster analysis supporting arbitrary distance measures and centroid
    computation. Further cluster methods include hard competitive learning,
    neural gas, and QT clustering. There are numerous visualization methods for
    cluster results (neighborhood graphs, convex cluster hulls, barcharts of
    centroids, ...), and bootstrap methods for the analysis of cluster
    stability."""

    homepage = "https://cran.r-project.org/package=flexclust"
    url      = "https://cran.rstudio.com/src/contrib/flexclust_1.3-5.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/flexclust"

    version('1.3-5', '90226a0e3a4f256f392a278e9543f8f4')

    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-modeltools', type=('build', 'run'))
