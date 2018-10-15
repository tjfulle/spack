# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libcap(MakefilePackage):
    """Libcap implements the user-space interfaces to the POSIX 1003.1e
    capabilities available in Linux kernels. These capabilities are a
    partitioning of the all powerful root privilege into a set of
    distinct privileges."""

    homepage = "https://sites.google.com/site/fullycapable/"
    url      = "https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.25.tar.gz"

    version('2.25', '4b18f7166a121138cca0cdd8ab64df4c')

    patch('libcap-fix-the-libcap-native-building-failure-on-CentOS-6.7.patch')

    def install(self, spec, prefix):
        make_args = [
            'RAISE_SETFCAP=no',
            'lib=lib',
            'prefix={0}'.format(prefix),
            'install'
        ]
        make(*make_args)

        chmod = which('chmod')
        chmod('+x', join_path(prefix.lib, 'libcap.so'))
