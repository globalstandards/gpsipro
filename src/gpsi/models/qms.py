# -*- coding: utf-8 -*-

from openerp import api
from openerp import fields, models
from openerp.osv import osv


class Process(models.Model):
    _name = 'gpsi.qms.process'
    _description = 'Process Description'

    name = fields.Char('Name')
    parent_id = fields.Many2one('gpsi.qms.process', 'Parent')


class ProcessIndicator(models.Model):
    _name = 'gpsi.qms.process.indicator'
    _description = 'Process Indicator'

    name = fields.Char('Name')
    process_id = fields.Many2one('gpsi.qms.process', 'Process')
    risk = fields.Float('Risk Value')


class ProcessMeasure(models.Model):
    _name = 'gpsi.qms.process.measure'
    _description = 'Process Measure'


class Checklist(models.Model):
    _name = 'gpsi.qms.checklist'
    _description = 'Checklist'
    _inherit = 'mail.thread'

    name = fields.Char('Name')
    version = fields.Char('Version')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get())
    question_ids = fields.One2many('gpsi.qms.checklist.question', 'checklist_id', 'Questions')


class ChecklistQuestion(models.Model):   
    _name = 'gpsi.qms.checklist.question'
    _description = 'Checklist Question'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    checklist_id = fields.Many2one('gpsi.qms.checklist', 'Checklist', ondelete='cascade')
    company_id = fields.Many2one(related='checklist_id.company_id', string='Company')
    doc_ref_id = fields.Many2one('ir.attachment', 'Doc. Reference')
    question = fields.Text('Question')
    requirement = fields.Html('Requirement')
    tips = fields.Html('Tips')
    sequence = fields.Integer('Sequence')
    section_id = fields.Many2one('gpsi.qms.checklist.question.category', 'Category')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.checklist.question') or 'New'

        result = super(ChecklistQuestion, self).create(vals)
        return result


class ChecklistQuestionCategory(models.Model):
    _name = 'gpsi.qms.checklist.question.category'
    _description = 'Checklist Question Tags'

    name = fields.Char('Category Name', required=True, translate=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get())
    parent_id = fields.Many2one('gpsi.qms.checklist.question.category', 'Parent Tag', select=True, ondelete='cascade')
    child_ids = fields.One2many('gpsi.qms.checklist.question.category', 'parent_id', 'Child Tag')

    _constraints = [
        (osv.osv._check_recursion, 'Error ! You can not create recursive tags.', ['parent_id'])
    ]            


class AuditOrder(models.Model):
    _name = 'gpsi.qms.audit.order'
    _description = 'Audit Order'
    _inherit = 'mail.thread'
    

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get())
    state = fields.Selection([
        ('new', 'New'),
        ('qualify', 'Qualify'),
        ('schedule', 'Schedule'),
        ('execute', 'Execute'),
        ('review', 'Review'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')],
        string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='new')
    kind = fields.Selection([
        ('internal', 'Internal Audit'),
        ('vendor', 'Vendor Audit'), 
        ('certification', 'Certification Audit')],
        string='Type', default='internal')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    notes = fields.Html('Notes')
    checklist_id = fields.Many2one('gpsi.qms.checklist', 'Checklist')
    vendor_id = fields.Many2one('res.partner', 'Vendor', domain=lambda self: [('supplier', '=', True)])
    facility_id = fields.Many2one('res.partner', 'Facility', domain=lambda self: [('type', '=', 'facility')])
    plan_id = fields.Many2one('gpsi.qms.audit.plan', 'Plan')
    assessment_id = fields.Many2one('gpsi.qms.audit.assessment', 'Assessment')
    opportunity_id = fields.Many2one('crm.lead', 'Opportunity')
    saleorder_id = fields.Many2one('sale.order', 'SaleOrder')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.order') or 'New'

        result = super(AuditOrder, self).create(vals)
        return result       


class AuditPlan(models.Model):
    _name = 'gpsi.qms.audit.plan'
    _description = 'Audit Plan'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    order_id = fields.Many2one('gpsi.qms.audit.order', 'Audit Order', ondelete='cascade')
    company_id = fields.Many2one(related='order_id.company_id', comodel_name='res.company')
    state = fields.Selection([
        ('new', 'New'),
        ('approved', 'Approved')], 
        string='Status', copy=False, index=True, track_visibility='onchange', default='new')
    leader_id = fields.Many2one('res.users', 'Auditor Leader')
    team_ids = fields.One2many('gpsi.qms.audit.team.member', 'plan_id', 'Audit Team')
    schedule_ids = fields.One2many('gpsi.qms.audit.plan.schedule', 'plan_id', 'Schedule')
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.plan') or 'New'

        result = super(AuditPlan, self).create(vals)
        return result


class AuditTeamMember(models.Model):
    _name = 'gpsi.qms.audit.team.member'
    _description = 'Team Member'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    plan_id = fields.Many2one('gpsi.qms.audit.plan', 'Audit Plan', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'User')
    role = fields.Selection(selection=[
        ('auditor', 'Auditor'), 
        ('witness', 'Witness'), 
        ('observer', 'Observer')], 
        default='auditor', string='Role')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.team.member') or 'New'

        result = super(AuditTeamMember, self).create(vals)
        return result 


class AuditPlanSchedule(models.Model):
    _name = 'gpsi.qms.audit.plan.schedule'
    _description = 'Audit Plan Schedule'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    plan_id = fields.Many2one('gpsi.qms.audit.plan', 'Audit Plan', ondelete='cascade')
    date = fields.Date('Date')
    hour = fields.Float('Hour')
    auditor_id = fields.Many2one('res.users', 'Auditor')
    description = fields.Html('Description')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.plan.schedule') or 'New'

        result = super(AuditPlanSchedule, self).create(vals)
        return result


class AuditAssessment(models.Model):
    _name = 'gpsi.qms.audit.assessment'
    _description = 'Audit Assessment'
    _inherit = 'mail.thread'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    order_id = fields.Many2one('gpsi.qms.audit.order', 'Audit Order', ondelete='cascade')
    company_id = fields.Many2one(related='order_id.company_id')
    observation_ids = fields.One2many('gpsi.qms.audit.observation', 'assessment_id', 'Observations')
    notes = fields.Html('Notes')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.assessment') or 'New'

        assessment = super(AuditAssessment, self).create(vals)
        observations = []
        if assessment.order_id.checklist_id:
            for question in assessment.order_id.checklist_id.question_ids:
                observations.append((0, False, {
                    'assessment_id': assessment.id,
                    'question_id': question.id
                }))
            assessment.write({'observation_ids': observations})

        return assessment


class AuditObservation(models.Model):
    _name = 'gpsi.qms.audit.observation'
    _description = 'Audit Observation'
    _inherit = 'mail.thread'


    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    assessment_id = fields.Many2one('gpsi.qms.audit.assessment', 'Assessment', ondelete='cascade')
    company_id = fields.Many2one(related='assessment_id.company_id')
    question_id = fields.Many2one('gpsi.qms.checklist.question', 'Question')
    question_text = fields.Text(related='question_id.question')
    question_section_id = fields.Many2one(related='question_id.section_id')
    question_sequence = fields.Integer(related='question_id.sequence')
    question_doc_ref_id = fields.Many2one(related='question_id.doc_ref_id')
    question_requirement = fields.Html(related='question_id.requirement')
    question_tips = fields.Html(related='question_id.tips')
    kind = fields.Selection(selection=[
        ('conformance', 'Conformance'), 
        ('improvement', 'Improvement'), 
        ('nc', 'Nonconformity')],
        string='Type', default='conformance')
    evidence = fields.Html('Evidence')
    nc_rating = fields.Selection(selection=[
        ('nc_minor', 'Minor'), 
        ('nc_major', 'Major'), 
        ('nc_critical', 'Critical')],
        string='Rating', default='nc_minor')
    nc_evidence = fields.Html('NC Evidence')
    nc_statement = fields.Html('NC Statement')
    required_action = fields.Boolean('Required Action')
    car_id = fields.Many2one('gpsi.qms.audit.car', 'Action Request', help='Corrective Action Request')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.observation') or 'New'

        result = super(AuditObservation, self).create(vals)
        return result


class CorrectiveActionRequest(models.Model):
    _name = 'gpsi.qms.audit.car'
    _description = 'Corrective Action Request'
    _inherit = 'mail.thread'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get())
    assigned_company_id = fields.Many2one('res.company', 'Assigned To')
    observation_id = fields.Many2one('gpsi.qms.audit.observation', 'Observation')
    due_date = fields.Date('Due Date')
    state = fields.Selection(selection=[
        ('open', 'Open'), 
        ('progress', 'In progress'), 
        ('review', 'Review'), 
        ('resolved', 'Resolved'), 
        ('cancelled', 'Cancelled')], 
        string='Status', default='open')
    root_cause = fields.Html('Root Cause')
    inmediate_correction = fields.Html('Inmediate Correction')
    root_cause_correction = fields.Html('Root Cause Correction')
    action_ids = fields.One2many('gpsi.qms.audit.ca', 'car_id', 'Corrective Actions')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.car') or 'New'

        result = super(CorrectiveActionRequest, self).create(vals)
        return result


class CorrectiveAction(models.Model):
    _name = 'gpsi.qms.audit.ca'
    _description = 'Corrective Action'
    _inherit = 'mail.thread'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, index=True, default='New')
    car_id = fields.Many2one('gpsi.qms.audit.car', 'Corrective Action Request')
    company_id = fields.Many2one(related='car_id.company_id', comodel_name='res.company')
    description = fields.Html('Description')
    responsible = fields.Char('Responsible')
    date = fields.Date('Date')
    kind = fields.Selection(selection=[
        ('corrective', 'Corrective'), 
        ('preventive', 'Preventive'), 
        ('verification', 'Verification')],
        string='Type', default='corrective')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('gpsi.qms.audit.ca') or 'New'

        result = super(CorrectiveAction, self).create(vals)
        return result
