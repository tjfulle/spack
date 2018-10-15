# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lmdb(MakefilePackage):
    """Symas LMDB is an extraordinarily fast, memory-efficient database we
    developed for the Symas OpenLDAP Project. With memory-mapped files, it
    has the read performance of a pure in-memory database while retaining
    the persistence of standard disk-based databases."""

    homepage = "https://lmdb.tech/"
    url      = "https://github.com/LMDB/lmdb/archive/LMDB_0.9.21.tar.gz"

    version('0.9.21', '41a4f7b63212a00e53fabd8159008201')
    version('0.9.16', '0de89730b8f3f5711c2b3a4ba517b648')

    build_directory = 'libraries/liblmdb'

    @property
    def install_targets(self):
        return ['prefix={0}'.format(self.prefix), 'install']

    @run_after('install')
    def install_pkgconfig(self):
        mkdirp(self.prefix.lib.pkgconfig)

        with open(join_path(self.prefix.lib.pkgconfig, 'lmdb.pc'), 'w') as f:
            f.write('prefix={0}\n'.format(self.prefix))
            f.write('exec_prefix=${prefix}\n')
            f.write('libdir={0}\n'.format(self.prefix.lib))
            f.write('includedir={0}\n'.format(self.prefix.include))
            f.write('\n')
            f.write('Name: LMDB\n')
            f.write('Description: Symas LMDB is an extraordinarily fast, '
                    'memory-efficient database.\n')
            f.write('Version: {0}\n'.format(self.spec.version))
            f.write('Cflags: -I${includedir}\n')
            f.write('Libs: -L${libdir} -llmdb\n')
