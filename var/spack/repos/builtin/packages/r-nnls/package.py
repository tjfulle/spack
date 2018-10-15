# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RNnls(RPackage):
    """An R interface to the Lawson-Hanson implementation of an
    algorithm for non-negative least squares (NNLS). Also allows
    the combination of non-negative and non-positive constraints."""

    homepage = "https://cran.r-project.org/package=nnls"
    url      = "https://cran.rstudio.com/src/contrib/nnls_1.4.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/nnls"

    version('1.4', 'cdb3640120f73e0ccb6079108e0ef361')
