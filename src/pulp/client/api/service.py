# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

from pulp.client.api.base import PulpAPI


class ServiceAPI(PulpAPI):
    '''
    Connection class to the services handler
    '''
    def search_packages(self, name=None, epoch=None, version=None, release=None,
                        arch=None, filename=None):
        data = {}
        if name:
            data["name"] = name
        if epoch:
            data["epoch"] = epoch
        if version:
            data["version"] = version
        if release:
            data["release"] = release
        if arch:
            data["arch"] = arch
        if filename:
            data["filename"] = filename
        path = "/services/search/packages/"
        return self.server.PUT(path, data)

    def dependencies(self, pkgnames, repoids, recursive=0):
        params = {'repoids': repoids,
                   'pkgnames': pkgnames,
                   'recursive': recursive}
        path = "/services/dependencies/"
        return self.server.POST(path, params)

    def upload(self, pkginfo, pkgstream):
        uploadinfo = {'pkginfo': pkginfo,
                      'pkgstream': pkgstream}
        path = "/services/upload/"
        return self.server.POST(path, uploadinfo)
