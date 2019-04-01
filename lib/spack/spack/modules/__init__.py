# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""This package contains code for creating environment modules, which can
include TCL non-hierarchical modules, LUA hierarchical modules, and others.
"""

from __future__ import absolute_import

from .tcl import TclModulefileWriter
from .lmod import LmodModulefileWriter
from .pymod import PymodModulefileWriter

__all__ = [
    'TclModulefileWriter',
    'LmodModulefileWriter',
    'PymodModulefileWriter'
]

module_types = {
    'tcl': TclModulefileWriter,
    'lmod': LmodModulefileWriter,
    'pymod': PymodModulefileWriter
}
