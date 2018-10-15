# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlStatisticsDescriptive(PerlPackage):
    """Module of basic descriptive statistical functions."""

    homepage = "http://search.cpan.org/~shlomif/Statistics-Descriptive-3.0612/lib/Statistics/Descriptive.pm"
    url      = "http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-3.0612.tar.gz"

    version('3.0612', 'e38cfbc1e3962d099b62a14a57a175f1')
