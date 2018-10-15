# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RJomo(RPackage):
    """Similarly to Schafer's package 'pan', 'jomo' is a package for multilevel
    joint modelling multiple imputation (Carpenter and Kenward, 2013)
    <doi:10.1002/9781119942283>. Novel aspects of 'jomo' are the possibility of
    handling binary and categorical data through latent normal variables, the
    option to use cluster-specific covariance matrices and to impute compatibly
    with the substantive model.
    """

    homepage = "https://cran.r-project.org/package=jomo"
    url      = "https://cran.r-project.org/src/contrib/jomo_2.6-2.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/jomo"

    version('2.6-2', 'eff4a6c1a971708959d65b3224c98a25')

    depends_on('r-lme4', type=('build', 'run'))
    depends_on('r-survival', type=('build', 'run'))
