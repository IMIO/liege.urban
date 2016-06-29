# -*- coding: utf-8 -*-

from Products.urban.services.base import SQLService
from Products.urban.services.base import SQLSession


class UnreferencedParcelError(Exception):
    """
    This parcel reference cannot be found in the official cadastre.
    """


class LiegeAddressService(SQLService):
    """
    """

    def __init__(self, dialect='postgresql+psycopg2', user='urb_xxx', host='', db_name='urb_xxx', password=''):
        super(LiegeAddressService, self).__init__(dialect, user, host, db_name, password)

        if self.can_connect():
            self._init_table('ptadresses_vdl', column_names=['secteururb', 'num_cad_a_'])


class LiegeAddressSession(SQLSession):
    """
    Implements all the sql queries of cadastre DB with sqlalchemy methods
    """

    def get_shore(self, capakey):
        """Return all divisions records of da table"""
        pt_adresses = self.tables.ptadresses_vdl
        query = self.session.query(pt_adresses.secteururb)
        query = query.filter(pt_adresses.num_cad_a_.like(capakey))

        result = query.distinct().all()
        return result
