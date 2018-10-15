# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Iozone(MakefilePackage):
    """IOzone is a filesystem benchmark tool. The benchmark generates and
    measures a variety of file operations. Iozone has been ported to many
    machines and runs under many operating systems."""

    homepage = "http://www.iozone.org/"
    url      = "http://www.iozone.org/src/current/iozone3_465.tar"

    version('3_465', 'c924e5e46fb1cf8145f420e8e57eb954')

    # TODO: Add support for other architectures as necessary
    build_targets = ['linux-AMD64']

    build_directory = 'src/current'

    def edit(self, spec, prefix):
        with working_dir(self.build_directory):
            filter_file(r'^CC\t= cc',
                        r'CC\t= {0}'.format(spack_cc),
                        'makefile')

    def install(self, spec, prefix):
        install_tree('docs', join_path(prefix, 'docs'))

        with working_dir(self.build_directory):
            install_tree('.', prefix.bin)
