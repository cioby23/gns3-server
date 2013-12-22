# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Interface for UNIX NIOs (Unix based OSes only).
"""

from .nio import NIO


class NIO_UNIX(NIO):
    """
    Dynamips UNIX NIO.

    :param hypervisor: Dynamips hypervisor object
    :param local_file: local UNIX socket filename
    :param remote_file: remote UNIX socket filename
    """

    _instance_count = 0

    def __init__(self, hypervisor, local_file, remote_file):

        NIO.__init__(self, hypervisor)

        # create an unique ID
        self._id = NIO_UNIX._instance_count
        NIO_UNIX._instance_count += 1
        self._name = 'nio_unix' + str(self._id)
        self._local_file = local_file
        self._remote_file = remote_file

        self._hypervisor.send("nio create_unix {name} {local} {remote}".format(name=self._name,
                                                                               local=local_file,
                                                                               remote=remote_file))

    @property
    def local_file(self):
        """
        Returns the local UNIX socket.

        :returns: local UNIX socket filename
        """

        return self._local_file

    @property
    def remote_file(self):
        """
        Returns the remote UNIX socket.

        :returns: remote UNIX socket filename
        """

        return self._remote_file
