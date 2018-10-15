# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Pgmath(CMakePackage):
    """Flang's math library"""

    homepage = "https://github.com/flang-compiler/flang"
    url      = "https://github.com/flang-compiler/flang/archive/flang_20180612.tar.gz"
    git      = "https://github.com/flang-compiler/flang.git"

    version('develop', branch='master')
    version('20180612', '62284e26214eaaff261a922c67f6878c')

    conflicts("%gcc@:7.1.9999")

    root_cmakelists_dir = 'runtime/libpgmath'
