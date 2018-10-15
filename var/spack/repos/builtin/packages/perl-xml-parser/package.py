# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#
from spack import *


class PerlXmlParser(PerlPackage):
    """XML::Parser - A perl module for parsing XML documents"""

    homepage = "http://search.cpan.org/perldoc/XML::Parser"
    url      = "http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz"

    version('2.44', 'af4813fe3952362451201ced6fbce379')

    depends_on('expat')

    def configure_args(self):
        args = []

        p = self.spec['expat'].prefix.lib
        args.append('EXPATLIBPATH={0}'.format(p))
        p = self.spec['expat'].prefix.include
        args.append('EXPATINCPATH={0}'.format(p))

        return args
