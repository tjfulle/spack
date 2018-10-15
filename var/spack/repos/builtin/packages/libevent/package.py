# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libevent(AutotoolsPackage):
    """The libevent API provides a mechanism to execute a callback function
       when a specific event occurs on a file descriptor or after a
       timeout has been reached. Furthermore, libevent also support
       callbacks due to signals or regular timeouts.

    """

    homepage = "http://libevent.org"
    url      = "https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz"
    list_url = "http://libevent.org/old-releases.html"

    version('2.0.21', 'b2405cc9ebf264aa47ff615d9de527a2')
    version('2.0.20', '94270cdee32c0cd0aa9f4ee6ede27e8e')
    version('2.0.19', '91111579769f46055b0a438f5cc59572')
    version('2.0.18', 'aa1ce9bc0dee7b8084f6855765f2c86a')
    version('2.0.17', 'dad64aaaaff16b5fbec25160c06fee9a')
    version('2.0.16', '899efcffccdb3d5111419df76e7dc8df')
    version('2.0.15', '2643abe7ba242df15c08b2cc14ec8759')
    version('2.0.14', 'cac0f379da35d3b98f83ac16fcfe1df4')
    version('2.0.13', 'af786b4b3f790c9d3279792edf7867fc')
    version('2.0.12', '42986228baf95e325778ed328a93e070')

    # Does not build with OpenSSL 1.1.0
    variant('openssl', default=True,
            description="Build with encryption enabled at the libevent level.")
    depends_on('openssl @:1.0', when='+openssl')

    def configure_args(self):
        spec = self.spec
        configure_args = []
        if '+openssl' in spec:
            configure_args.append('--enable-openssl')
        else:
            configure_args.append('--disable-openssl')

        return configure_args
