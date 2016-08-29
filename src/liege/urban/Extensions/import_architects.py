# -*- coding: utf-8 -*-

from plone import api

import csv


def do_import():
    site = api.portal.get()
    archi_folder = site.urban.architects

    rows = csv.DictReader(open('architectes_listing.csv', 'r'), delimiter=';')
    for row in rows:
        row.pop('')
        for k, v in row.iteritems():
            row[k] = v.decode('iso-8859-1')
        archi_id = site.plone_utils.normalizeString(u'{}-{}'.format(row['name1'], row['name2']))
        archi_folder.invokeFactory('Architect', id=site.generateUniqueId(archi_id), **row)
