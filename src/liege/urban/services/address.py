# -*- coding: utf-8 -*-

from Products.urban.services.base import SQLService
from Products.urban.services.base import SQLSession

IGNORE = []


class UnreferencedParcelError(Exception):
    """
    This parcel reference cannot be found in the official cadastre.
    """


class LiegeAddressService(SQLService):
    """
    """

    def __init__(self, dialect='postgresql+psycopg2', user='', host='', db_name='', password=''):
        super(LiegeAddressService, self).__init__(dialect, user, host, db_name, password)

        if self.can_connect():
            self._init_table(
                'ptadresses_vdl',
                column_names=[
                    'gid',
                    'g_legnum',
                    'secteururb',
                    'num_cad_a_',
                    'coderue',
                    'ref_rue',
                    'adresse',
                    'num_police',
                    'lishab_cp',
                ]
            )


class LiegeAddressSession(SQLSession):
    """
    Implements all the sql queries of cadastre DB with sqlalchemy methods
    """

    def query_addresses(self, street_name=IGNORE, INS_code=IGNORE, street_number=IGNORE):
        """
        """
        table = self.tables.ptadresses_vdl
        query = self._base_query_address()

        # search on street if name if only if there's no INS code
        if INS_code is IGNORE:
            query = street_name is IGNORE and query or query.filter(table.adresse.ilike(u'%{}%'.format(street_name)))

        query = street_number is IGNORE and query or query.filter(table.num_police == int(street_number))

        while INS_code != IGNORE and len(INS_code) < 4:
            INS_code = '0' + INS_code
        query = INS_code is IGNORE and query or query.filter(table.coderue == INS_code)

        records = query.distinct().all()

        return records

    def query_address_by_gid(self, gid):
        """
        Return the unique 'gid' address point .
        """
        table = self.tables.ptadresses_vdl
        query = self._base_query_address()

        query = query.filter(table.gid == gid)
        try:
            address = query.distinct().one()
            return address
        except:
            return

    def query_address_by_legnum(self, legnum):
        """
        Return the unique 'gid' address point .
        """
        table = self.tables.ptadresses_vdl
        query = self._base_query_address()

        query = query.filter(table.g_legnum == legnum)
        try:
            address = query.distinct().one()
            return address
        except:
            return

    def _base_query_address(self):
        """
        """
        table = self.tables.ptadresses_vdl
        # columns to return
        query = self.session.query(
            table.gid.label('address_point'),
            table.coderue.label('street_code'),
            table.num_cad_a_.label('capakey'),
            table.adresse.label('street_name'),
            table.num_police.label('street_number'),
            table.secteururb.label('shore'),
            table.lishab_cp.label('zip_code'),
        )
        return query
