# -*- coding: utf-8 -*-

from openerp import tools, api
from openerp import fields, models


class Partner(models.Model):
    '''
    Extiende res.partner para agregar campos necesarios de venta.
    '''

    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[('facility', 'Facility address'), ('locality', 'Locality address')])
    gpsi_rfc = fields.Char('RFC')


class Lead(models.Model):
    _inherit = 'crm.lead'

    gpsi_sale_application_id = fields.Many2one('gpsi.sale.certification.application', 'Application')


class CertificationApplication(models.Model):
    '''
    Formulario de aplicación para certificación.
    '''

    _name = 'gpsi.sale.certification.application'
    _description = 'Application Form'

    name = fields.Char('Name')
    facility_ids = fields.One2many('gpsi.sale.certification.application.site', 'application_id', 'Facilities')
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=24, change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", 'State', ondelete='restrict')
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    email = fields.Char('Email')
    phone1 = fields.Char('Phone 1')
    phone2 = fields.Char('Phone 2')
    website = fields.Char('Website', help='Website of Partner or Company')
    rfc = fields.Char('RFC')
    fiscal_address = fields.Char('Fiscal Address')
    contact_name = fields.Char('Name')
    contact_position = fields.Char('Job Position')
    contact_email1 = fields.Char('Email 1')
    contact_email2 = fields.Char('Email 2')
    standard_id = fields.Many2one('gpsi.standarization.standard', 'Standard')
    co_profile = fields.Selection(
        selection=[
            ('manufacture', 'Manufacture'),
            ('education', 'Education'),
            ('service', 'Service'),
            ('other', 'Other')], default='manufacture', string='Profile')
    co_profile_desc = fields.Text('Description')
    scope = fields.Text('Scope')
    apply_design = fields.Boolean('Apply Design')
    exclusions = fields.Text('Exclusions')
    certified = fields.Boolean('Certified')
    certified_desc = fields.Text('Certified Description')
    audit_type = fields.Selection(
        selection=[
            ('separated', 'Separated'), 
            ('combined', 'Combined'), 
            ('integrated', 'Integrated'), 
            ('mixed', 'Mixed')], default='separated', string='Audit Type')
    customers = fields.Char('Customers')
    suppliers = fields.Char('Suppliers')
    has_external_proc = fields.Boolean('Has External Process?')
    external_proc = fields.Char('Name')
    external_proc_outsource = fields.Char('Outsourcing Name')
    has_consultant = fields.Boolean('Has Consultant?')
    consultant_name = fields.Char('Name')
    consultant_phone = fields.Char('Phone')
    language = fields.Char('Language')
    good_practices = fields.Char('Good Practices')
    technologies = fields.Char('Technologies')
    company_know = fields.Char('Company Know')
    has_internal_audits = fields.Boolean('Has Internal Audits?')
    has_management_reviews = fields.Boolean('Management Reviews?')
    has_quality_manual = fields.Boolean('Has Quality Manual?')
    preaudit_date = fields.Date('Pre-Audit Date')
    audit_stage1_date = fields.Date('Document Review Date')
    audit_stage2_date = fields.Date('Certification Audit')
    audit_surveillance1_date = fields.Date('Surveillance 1')
    audit_surveillance2_date = fields.Date('Surveillance 2')


class CertificationApplicationSite(models.Model):
    '''
    Sitio de certificación.
    '''
    
    _name = 'gpsi.sale.certification.application.site'
    _description = 'Site'

    application_id = fields.Many2one('gpsi.sale.certification.application', 'Application', ondelete="cascade")
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=24, change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", 'State', ondelete='restrict')
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    shift1 = fields.Integer('Shift 1')
    shift2 = fields.Integer('Shift 2')
    shift3 = fields.Integer('Shift 3')
    shift4 = fields.Integer('Shift 4')
    description = fields.Text('Description')
