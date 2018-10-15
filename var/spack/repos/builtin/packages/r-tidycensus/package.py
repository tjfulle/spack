# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RTidycensus(RPackage):
    """An integrated R interface to the decennial US Census and American
    Community Survey APIs and the US Census Bureau's geographic boundary
    files. Allows R users to return Census and ACS data as tidyverse-ready
    data frames, and optionally returns a list-column with feature
    geometry for many geographies."""

    homepage = "https://cran.r-project.org/package=tidycensus"
    url      = "https://cran.rstudio.com/src/contrib/tidycensus_0.3.1.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/tidycensus"

    version('0.3.1', '420d046b5a408d321e775c3d410e7699')

    depends_on('r-httr', type=('build', 'run'))
    depends_on('r-sf', type=('build', 'run'))
    depends_on('r-dplyr', type=('build', 'run'))
    depends_on('r-tigris', type=('build', 'run'))
    depends_on('r-stringr', type=('build', 'run'))
    depends_on('r-jsonlite', type=('build', 'run'))
    depends_on('r-purrr', type=('build', 'run'))
    depends_on('r-rvest', type=('build', 'run'))
    depends_on('r-tidyr', type=('build', 'run'))
    depends_on('r-rappdirs', type=('build', 'run'))
    depends_on('r-readr', type=('build', 'run'))
    depends_on('r-xml2', type=('build', 'run'))
    depends_on('r-units', type=('build', 'run'))
