# -*- coding: utf-8 -*-

from openerp import api
from openerp import fields, models


class Organization(models.Model):
    _name = 'gpsi.standarization.organization'
    _description = 'Standard Organization'

    name = fields.Char('Name')
    code = fields.Char('Code')


class Standard(models.Model):
    '''
    '''

    _name = 'gpsi.standarization.standard'
    _description = 'Standard'

    name = fields.Char('Name')
    organization_id = fields.Many2one('gpsi.standarization.organization', 'Organization')
    version = fields.Char('Version')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name + ':' + record.version))
        return result
