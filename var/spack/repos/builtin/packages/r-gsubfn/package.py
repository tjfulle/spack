# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGsubfn(RPackage):
    """gsubfn is like gsub but can take a replacement function or
    certain other objects instead of the replacement string. Matches
    and back references are input to the replacement function and
    replaced by the function output. gsubfn can be used to split
    strings based on content rather than delimiters and for
    quasi-perl-style string interpolation. The package also has
    facilities for translating formulas to functions and allowing
    such formulas in function calls instead of functions. This can
    be used with R functions such as apply, sapply, lapply, optim,
    integrate, xyplot, Filter and any other function that expects
    another function as an input argument or functions like cat or
    sql calls that may involve strings where substitution is
    desirable."""

    homepage = "https://cran.r-project.org/package=gsubfn"
    url      = "https://cran.r-project.org/src/contrib/gsubfn_0.6-6.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/gsubfn"

    version('0.6-6', '94195ff3502706c736d9c593c07252bc')

    depends_on('r-proto', type=('build', 'run'))
