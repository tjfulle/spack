# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRappdirs(RPackage):
    """An easy way to determine which directories on the users computer
    you should use to save data, caches and logs. A port of Python's
    'Appdirs' to R."""

    homepage = "https://cran.r-project.org/package=rappdirs"
    url      = "https://cran.rstudio.com/src/contrib/rappdirs_0.3.1.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/rappdirs"

    version('0.3.1', 'fbbdceda2aa49374e61c7d387bf9ea21')

    depends_on('r@2.14:', type=('build', 'run'))
