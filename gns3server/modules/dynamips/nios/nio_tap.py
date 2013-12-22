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
Interface for TAP NIOs (UNIX based OSes only).
"""

from .nio import NIO


class NIO_TAP(NIO):
    """
    Dynamips TAP NIO.

    :param hypervisor: Dynamips hypervisor object
    :param tap_device: TAP device name (e.g. tap0)
    """

    _instance_count = 0

    def __init__(self, hypervisor, tap_device):

        NIO.__init__(self, hypervisor)

        # create an unique ID
        self._id = NIO_TAP._instance_count
        NIO_TAP._instance_count += 1
        self._name = 'nio_tap' + str(self._id)
        self._tap_device = tap_device

        self._hypervisor.send("nio create_tap {name} {tap}".format(name=self._name,
                                                                   tap=tap_device))

    @property
    def tap_device(self):
        """
        Returns the TAP device used by this NIO.

        :returns: the TAP device name
        """

        return self._tap_device
