# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterClient(PythonPackage):
    """Jupyter protocol client APIs"""

    homepage = "https://github.com/jupyter/jupyter_client"
    url      = "https://github.com/jupyter/jupyter_client/archive/4.4.0.tar.gz"

    version('4.4.0', 'a0bd6fe6ba7c504fbc962a88a2a56a90')
    version('4.3.0', '257d9f5429dac4d9511db84d201d3a9e')
    version('4.2.2', '988ea87554215a83c6ad52e554d8d8c4')
    version('4.2.1', '16994e5cace322c777456bc5a26502d7')
    version('4.2.0', '61c43c9f243e42f1945fae5d56d0d23c')
    version('4.1.1', '8436e4a3266a442f576cdfef39dc0e19')
    version('4.1.0', 'cf42048b889c8434fbb5813a9eec1d34')
    version('4.0.0', '00fa63c67cb3adf359d09dc4d803aff5')

    depends_on('python@2.7:2.8,3.3:')
    depends_on('py-traitlets', type=('build', 'run'))
    depends_on('py-jupyter-core', type=('build', 'run'))
    depends_on('py-zmq@13:', type=('build', 'run'))
