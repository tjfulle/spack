# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRcpp(RPackage):
    """The 'Rcpp' package provides R functions as well as C++ classes which
    offer a seamless integration of R and C++. Many R data types and objects
    can be mapped back and forth to C++ equivalents which facilitates both
    writing of new code as well as easier integration of third-party libraries.
    Documentation about 'Rcpp' is provided by several vignettes included in
    this package, via the 'Rcpp Gallery' site at <http://gallery.rcpp.org>, the
    paper by Eddelbuettel and Francois (2011, JSS), and the book by
    Eddelbuettel (2013, Springer); see 'citation("Rcpp")' for details on these
    last two."""

    homepage = "http://dirk.eddelbuettel.com/code/rcpp.html"
    url      = "https://cran.rstudio.com/src/contrib/Rcpp_0.12.13.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/Rcpp"

    version('0.12.16', 'ab5107766c63d66065ed1a92a4cab1b7')
    version('0.12.15', 'bebac0782862c15c2944764343e55582')
    version('0.12.14', '89a3dbad0aa3e345b9d0b862fa1fc56a')
    version('0.12.13', '5186d119132bfe07f66da74c50b190a4')
    version('0.12.12', '97b36a3b567e3438067c4a7d0075fd90')
    version('0.12.11', 'ea1710213cbb1d91b1d0318e6fa9aa37')
    version('0.12.9', '691c49b12794507288b728ede03668a5')
    version('0.12.6', 'db4280fb0a79cd19be73a662c33b0a8b')
    version('0.12.5', 'f03ec05b4e391cc46e7ce330e82ff5e2')
