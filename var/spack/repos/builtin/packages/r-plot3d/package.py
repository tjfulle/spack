# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPlot3d(RPackage):
    """Functions for viewing 2-D and 3-D data, including perspective plots,
       slice plots, surface plots, scatter plots, etc. Includes data sets from
       oceanography."""

    homepage = "https://CRAN.R-project.org/package=plot3D"
    url      = "https://cran.r-project.org/src/contrib/plot3D_1.1.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/plot3D"

    version('1.1.1', '5135aa1f3cf6106f2ded3f393a24e75d')

    depends_on('r-misc3d', type=('build', 'run'))
