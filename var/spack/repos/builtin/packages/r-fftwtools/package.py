# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFftwtools(RPackage):
    """Provides a wrapper for several 'FFTW' functions. This package provides
       access to the two-dimensional 'FFT', the multivariate 'FFT', and the
       one-dimensional real to complex 'FFT' using the 'FFTW3' library. The
       package includes the functions fftw() and mvfftw() which are designed
       to mimic the functionality of the R functions fft() and mvfft().
       The 'FFT' functions have a parameter that allows them to not return
       the redundant complex conjugate when the input is real data."""

    homepage = "https://github.com/krahim/fftwtools"
    url      = "https://cran.r-project.org/src/contrib/fftwtools_0.9-8.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/fftwtools"

    version('0.9-8', '2d1258fbaf0940b57ed61c8d6cd6694d')

    depends_on('fftw')
