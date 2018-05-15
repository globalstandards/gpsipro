# -*- coding: utf-8 -*-

from openerp import api, fields, models
from openerp.exceptions import ValidationError


class ResPartner(models.Model):
    '''
    Actualiza res.partner
    '''
    _inherit = 'res.partner'
    
    gps_cliente_id = fields.Many2one(comodel_name='gps.clientes', string='GPS Cliente')
    
    @api.model
    def create(self, vals):
        if 'category_id' in vals:
            self._set_branch_office_image()
        return super(ResPartner, self).create(vals)
    
    def _set_branch_office_image(self):
        pass

class ResUsers(models.Model):
    '''
    Actualiza res.users
    '''
    _inherit = 'res.users'
    
    gps_usuario_id = fields.Many2one(comodel_name='gps.usuarios')


class GnModelOfClient(models.Model):
    '''
    Class: GnModelOfClient
    '''
    _name = 'gps.gnmodelofclient'
    _description = 'gps.gnmodelofclient'
    
    # Original fields
    modelofclient = fields.Char('ModelOfClient')
    prosclienfk = fields.Char('ProsClienFk')
    modelfk = fields.Char('ModelFk')


class EncuestasClientes(models.Model):
    '''
    Class: EncuestasClientes
    '''
    _name = 'gps.encuestasclientes'
    _description = 'gps.encuestasclientes'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    fechaenviado = fields.Date('FechaEnviado')
    fecharesuelto = fields.Date('FechaResuelto')
    md5 = fields.Char('MD5')
    encuestaid = fields.Char('EncuestaId')
    acciones = fields.Char('Acciones')
    quejas = fields.Char('Quejas')


class NoConformidadesConsultadas(models.Model):
    '''
    Class: NoConformidadesConsultadas
    '''
    _name = 'gps.noconformidadesconsultadas'
    _description = 'gps.noconformidadesconsultadas'
    
    # Original fields
    consultadaskey = fields.Char('ConsultadasKey')
    numerotrabajo = fields.Char('NumeroTrabajo')
    instanteconsulta = fields.Date('InstanteConsulta')
    puntodenorma = fields.Char('PuntoDeNorma')


class ArchivoEnviado(models.Model):
    '''
    Class: ArchivoEnviado
    '''
    _name = 'gps.archivoenviado'
    _description = 'gps.archivoenviado'
    
    # Original fields
    archivoenviadokey = fields.Char('ArchivoEnviadoKey')
    numerotrabajo = fields.Char('NumeroTrabajo')
    nombrearchivo = fields.Char('NombreArchivo')
    instanteenviado = fields.Date('InstanteEnviado')
    instanteguardado = fields.Date('InstanteGuardado')
    existeerror = fields.Boolean('ExisteError')
    instanteerror = fields.Date('InstanteError')
    descripcionerror = fields.Char('DescripcionError')


class GnContactProspectClient(models.Model):
    '''
    Class: GnContactProspectClient
    '''
    _name = 'gps.gncontactprospectclient'
    _description = 'gps.gncontactprospectclient'
    
    # Original fields
    contactkey = fields.Char('ContactKey')
    prosclienfk = fields.Char('ProsClienFk')
    contactname = fields.Char('ContactName')
    contactlast = fields.Char('ContactLast')
    contactlastsecond = fields.Char('ContactLastSecond')
    position = fields.Char('Position')
    email = fields.Char('Email')
    emailsecondary = fields.Char('Emailsecondary')
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    typecontact = fields.Integer('TypeContact')


class EncuestasClientesRespuestas(models.Model):
    '''
    Class: EncuestasClientesRespuestas
    '''
    _name = 'gps.encuestasclientesrespuestas'
    _description = 'gps.encuestasclientesrespuestas'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    encuestarespuestaid = fields.Char('EncuestaRespuestaId')


class GnRegistrationCode(models.Model):
    '''
    Class: GnRegistrationCode
    '''
    _name = 'gps.gnregistrationcode'
    _description = 'gps.gnregistrationcode'
    
    # Original fields
    registrationcodekey = fields.Char('RegistrationCodeKey')
    prosclienfk = fields.Char('ProsClienFk')
    email = fields.Char('Email')
    code = fields.Char('Code')
    generationdate = fields.Date('GenerationDate')
    active = fields.Boolean('Active')
    loginemail = fields.Char('LoginEmail')
    supplierfk = fields.Char('SupplierFk')


class GnSubSection(models.Model):
    '''
    Class: GnSubSection
    '''
    _name = 'gps.gnsubsection'
    _description = 'gps.gnsubsection'
    
    # Original fields
    subsectionkey = fields.Char('SubSectionKey')
    subsectiondescription = fields.Char('SubSectionDescription')


class AuditorExpertoTecnico(models.Model):
    '''
    Class: AuditorExpertoTecnico
    '''
    _name = 'gps.auditorexpertotecnico'
    _description = 'gps.auditorexpertotecnico'
    
    # Original fields
    idcliente = fields.Char('IdCliente')
    idauditor = fields.Integer('IdAuditor')
    fecha = fields.Date('Fecha')


class EncuestasClientesRespuestasComentarios(models.Model):
    '''
    Class: EncuestasClientesRespuestasComentarios
    '''
    _name = 'gps.encuestasclientesrespuestascomentarios'
    _description = 'gps.encuestasclientesrespuestascomentarios'
    
    # Original fields
    encuestarespuestaid = fields.Char('EncuestaRespuestaId')
    comentario = fields.Char('Comentario')
    numerotrabajo = fields.Char('NumeroTrabajo')


class GnSupplier(models.Model):
    '''
    Class: GnSupplier
    '''
    _name = 'gps.gnsupplier'
    _description = 'gps.gnsupplier'
    _rec_name = 'providername'
    _inherit = 'mail.thread'
    
    # Original fields
    supplierkey = fields.Char('SupplierKey')
    prosclienfk = fields.Char('ProsClienFk')
    productfk = fields.Char('ProductFk')
    servicefk = fields.Char('ServiceFk')
    industrialsectorfk = fields.Char('IndustrialSectorFk')
    idestado = fields.Char('IdEstado')
    idpais = fields.Char('IdPais')
    modelfk = fields.Char('ModelFk')
    creationdate = fields.Date('CreationDate')
    numberofemployees = fields.Integer('NumberOfEmployees')
    providername = fields.Char('ProviderName')
    rfc = fields.Char('RFC')
    adresstax = fields.Text('AdressTax')
    zipcode = fields.Char('ZipCode')
    nickname = fields.Char('NickName')
    password = fields.Char('Password')
    googlepoint = fields.Char('GooglePoint')
    website = fields.Char('WebSite')
    numext = fields.Char('NumExt')
    numint = fields.Char('NumInt')
    colony = fields.Char('Colony')
    city = fields.Char('City')
    productservicedesc = fields.Char('ProductServiceDesc')
    inactive = fields.Boolean('Inactive')
    iscritical = fields.Boolean('IsCritical')
    numberofcomplaints = fields.Integer('NumberOfComplaints')
    themetext = fields.Char('ThemeText')
    themebackground = fields.Char('ThemeBackground')
    checklistconfirmdate = fields.Date('CheckListConfirmDate')
    qualityagreeconfirmdate = fields.Date('QualityAgreeConfirmDate')
    agreementletterconfirmdate = fields.Date('AgreementLetterConfirmDate')
    protocolconfirmdate = fields.Date('ProtocolConfirmDate')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')
    product_id = fields.Many2one(comodel_name='gps.gnproduct', string='Product')
    service_id = fields.Many2one(comodel_name='gps.gnservice', string='Service')
    industrialsector_id = fields.Many2one(comodel_name='gps.gnindustrialsector', string='Sector')
    estado_id = fields.Many2one(comodel_name='gps.estados', string='State')
    event_count = fields.Integer(compute='_get_event_count', string='Number events attached');
    complaint_count = fields.Integer(compute='_get_complaint_count', string='Number complaints attached');
    
    def _get_event_count(self):
        for event in self:
            events = self.env['gps.gnsupplierevent'].search([['supplier_id', '=', event.id]])
            event.event_count = len(events)
        
    def _get_complaint_count(self):
        for event in self:
            complaints = self.env['gps.gncomplaint'].search([['supplier_id', '=', event.id]])
            event.complaint_count = len(complaints)


class ContratosHistorial(models.Model):
    '''
    Class: ContratosHistorial
    '''
    _name = 'gps.contratoshistorial'
    _description = 'gps.contratoshistorial'
    
    # Original fields
    idcontratohistorial = fields.Char('IdContratoHistorial')
    idcontrato = fields.Char('IdContrato')
    usuarionickname = fields.Char('UsuarioNickName')
    accion = fields.Integer('Accion')
    fecha = fields.Date('Fecha')
    comentario = fields.Char('Comentario')
    cambios = fields.Char('Cambios')


class Roles(models.Model):
    '''
    Class: Roles
    '''
    _name = 'gps.roles'
    _description = 'gps.roles'
    
    # Original fields
    idrol = fields.Char('IdRol')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')


class GnCCC(models.Model):
    '''
    Class: GnCCC
    '''
    _name = 'gps.gnccc'
    _description = 'gps.gnccc'
    
    # Original fields
    ccckey = fields.Char('CCCKey')
    nombreccc = fields.Char('NombreCCC')
    fechaccc = fields.Date('FechaCCC')


class RolesUsuario(models.Model):
    '''
    Class: RolesUsuario
    '''
    _name = 'gps.rolesusuario'
    _description = 'gps.rolesusuario'
    
    # Original fields
    idrol = fields.Char('IdRol')
    idusuario = fields.Integer('IdUsuario')


class GnPregunta(models.Model):
    '''
    Class: GnPregunta
    '''
    _name = 'gps.gnpregunta'
    _description = 'gps.gnpregunta'
    
    # Original fields
    preguntakey = fields.Char('PreguntaKey')
    cccfk = fields.Char('CCCFk')
    pregunta = fields.Char('Pregunta')
    clavepregunta = fields.Integer('ClavePregunta')


class GnRespuesta(models.Model):
    '''
    Class: GnRespuesta
    '''
    _name = 'gps.gnrespuesta'
    _description = 'gps.gnrespuesta'
    
    # Original fields
    respnumericakey = fields.Char('RespNumericaKey')
    eventofk = fields.Char('EventoFk')
    cccfk = fields.Char('CCCFk')
    preguntafk = fields.Char('PreguntaFk')
    clavepreguntafk = fields.Integer('ClavePreguntaFk')


class Contactos(models.Model):
    '''
    Class: Contactos
    '''
    _name = 'gps.contactos'
    _description = 'gps.contactos'
    
    # Original fields
    idcliente = fields.Char('IdCliente')
    idcontrato = fields.Char('IdContrato')
    nombre = fields.Char('Nombre')
    puesto = fields.Char('Puesto')
    telefono = fields.Char('Telefono')
    correo = fields.Char('Correo')
    numemp = fields.Integer('NumEmp')
    fechaalta = fields.Date('FechaAlta')


class UsuariosContrasenas(models.Model):
    '''
    Class: UsuariosContrasenas
    '''
    _name = 'gps.usuarioscontrasenas'
    _description = 'gps.usuarioscontrasenas'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    passwordactualizado = fields.Date('PasswordActualizado')


class GnCuesInitialAlsea(models.Model):
    '''
    Class: GnCuesInitialAlsea
    '''
    _name = 'gps.gncuesinitialalsea'
    _description = 'gps.gncuesinitialalsea'
    
    # Original fields
    cuesinitialalseakey = fields.Char('CuesInitialAlseaKey')
    supplierfk = fields.Char('SupplierFk')
    qualitymanager = fields.Char('QualityManager')
    areasqualitymanager = fields.Char('AreasQualityManager')
    procedureandprograms = fields.Char('ProcedureAndPrograms')
    bprogramgoodpractices = fields.Boolean('BProgramGoodPractices')
    areasandpersonal = fields.Char('AreasAndPersonal')
    bcualitysystemimplemented = fields.Boolean('BCualitySystemImplemented')
    bcertification = fields.Boolean('BCertification')
    lastevaluationdate = fields.Date('LastEvaluationDate')
    bmanualhaccp = fields.Boolean('BManualHACCP')
    bprocedureforapproval = fields.Boolean('BProcedureForApproval')
    bcualitycertificatematerial = fields.Boolean('BCualityCertificateMaterial')
    blistsuppliersapproved = fields.Boolean('BListSuppliersApproved')
    originrawmaterials = fields.Integer('OriginRawMaterials')
    bchemicalscontrol = fields.Boolean('BChemicalsControl')
    chemicalssupplier = fields.Char('ChemicalsSupplier')
    brestingedareachemical = fields.Boolean('BRestingedAreaChemical')
    generalprocess = fields.Char('GeneralProcess')
    equipment = fields.Char('Equipment')
    monitorcriticalpoints = fields.Char('MonitorCriticalPoints')
    bdeviceexternalmatter = fields.Boolean('BDeviceExternalMatter')
    bmetaparticles = fields.Boolean('BMetaParticles')
    bmaintenanceprogram = fields.Boolean('BMaintenanceProgram')
    bcalibrationprogram = fields.Boolean('BCalibrationProgram')
    bprocedureclean = fields.Boolean('BProcedureClean')
    bfisical = fields.Boolean('BFisical')
    fisicalfrequency = fields.Char('FisicalFrequency')
    fisicallabname = fields.Char('FisicalLabName')
    bmicro = fields.Boolean('BMicro')
    microfrequency = fields.Char('MicroFrequency')
    microlabname = fields.Char('MicroLabName')
    bwater = fields.Boolean('BWater')
    waterfrequency = fields.Char('WaterFrequency')
    waterlabname = fields.Char('WaterLabName')
    bpestmanagementprogram = fields.Boolean('BPestManagementProgram')
    companylicence = fields.Char('CompanyLicence')
    unitsown = fields.Integer('UnitsOwn')
    unitstype = fields.Integer('UnitsType')
    bnotconforproductprocmatter = fields.Boolean('BNotConforProductProcMatter')
    bnotconforproductprocproductprocess = fields.Boolean('BNotConforProductProcProductProcess')
    bnotconforproductprocproductfinished = fields.Boolean('BNotConforProductProcProductFinished')
    btrakingprocedure = fields.Boolean('BTrakingProcedure')
    bcomplaintmanagement = fields.Boolean('BComplaintManagement')
    followcomplaint = fields.Char('FollowComplaint')
    bsignedqualityagreement = fields.Boolean('BSignedQualityAgreement')


class EventosContrato(models.Model):
    '''
    Class: EventosContrato
    '''
    _name = 'gps.eventoscontrato'
    _description = 'gps.eventoscontrato'
    
    # Original fields
    ideventocontrato = fields.Char('IdEventoContrato')
    idcontrato = fields.Char('IdContrato')
    tipoevento = fields.Integer('TipoEvento')
    dias = fields.Float('Dias')
    costo = fields.Float('Costo')
    idubicacion = fields.Char('IdUbicacion')
    
    # Extended fields
    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Contracts')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')
    tipoevento = fields.Selection(
        selection=[
          (1, 'None'),
          (2, 'PreAuditoria'),
          (3, 'Etapa I'),
          (4, 'Etapa II'),
          (5, 'Seguimiento I'),
          (6, 'Cars'),
          (7, 'Recertificacion'),
          (8, 'Seguimiento II'),
          (9, 'Seguimiento III'),
          (10, 'Seguimiento IV'),
          (11, 'Seguimiento V'),
          (12, 'Transferencia'),
          (13, 'Recertificacionto'),
          (14, 'Takeover'),
          (15, 'Undefined'),
          (16, 'Auditoria Especial')
        ],
        string='Tipo Evento Contrato')


class GnRespAbierta(models.Model):
    '''
    Class: GnRespAbierta
    '''
    _name = 'gps.gnrespabierta'
    _description = 'gps.gnrespabierta'
    
    # Original fields
    respabiertakey = fields.Char('RespAbiertaKey')
    webkey = fields.Integer('WebKey')
    eventofk = fields.Char('EventoFk')
    cccfk = fields.Char('CCCFk')
    bloqueado = fields.Boolean('Bloqueado')
    fechachecklist = fields.Date('FechaCheckList')
    auditoriainicial = fields.Boolean('AuditoriaInicial')
    auditoriaregistro = fields.Boolean('AuditoriaRegistro')
    res1 = fields.Integer('Res1')
    res2 = fields.Integer('Res2')
    res3 = fields.Integer('Res3')
    res4 = fields.Integer('Res4')
    res5 = fields.Integer('Res5')
    res6 = fields.Integer('Res6')
    res7 = fields.Integer('Res7')
    res8 = fields.Integer('Res8')
    res9 = fields.Integer('Res9')
    res10 = fields.Integer('Res10')
    res11 = fields.Integer('Res11')
    auditoriavigilancia = fields.Boolean('AuditoriaVigilancia')
    auditoriaespecial = fields.Boolean('AuditoriaEspecial')
    res12 = fields.Integer('Res12')
    res13 = fields.Integer('Res13')
    res14 = fields.Integer('Res14')
    res15 = fields.Integer('Res15')
    res16 = fields.Integer('Res16')
    res17 = fields.Integer('Res17')
    res18 = fields.Integer('Res18')
    res19 = fields.Integer('Res19')
    res20 = fields.Integer('Res20')
    asumregistro = fields.Boolean('AsumRegistro')
    res21 = fields.Integer('Res21')
    res22 = fields.Integer('Res22')
    res23 = fields.Integer('Res23')
    res24 = fields.Integer('Res24')
    res25 = fields.Integer('Res25')
    res26 = fields.Integer('Res26')
    res27 = fields.Integer('Res27')
    res28 = fields.Integer('Res28')
    paisoficinarevisor = fields.Char('PaisOficinaRevisor')
    paisoficinarevisorfecha = fields.Date('PaisOficinaRevisorFecha')
    personalrevisor = fields.Char('PersonalRevisor')
    personalrevisorfecha = fields.Date('PersonalRevisorFecha')
    audinicialcertreview = fields.Boolean('AudInicialCertReview')
    audregistrocertreview = fields.Boolean('AudRegistroCertReview')
    res29 = fields.Integer('Res29')
    res30 = fields.Integer('Res30')
    res31 = fields.Integer('Res31')
    res32 = fields.Integer('Res32')
    res33 = fields.Integer('Res33')
    res34 = fields.Integer('Res34')
    res35 = fields.Integer('Res35')
    res36 = fields.Integer('Res36')
    res37 = fields.Integer('Res37')
    res38 = fields.Integer('Res38')
    res39 = fields.Integer('Res39')
    res40 = fields.Integer('Res40')
    res41 = fields.Integer('Res41')
    res42 = fields.Integer('Res42')
    res43 = fields.Integer('Res43')
    res44 = fields.Integer('Res44')
    res45 = fields.Integer('Res45')
    res46 = fields.Integer('Res46')
    res47 = fields.Integer('Res47')
    res48 = fields.Integer('Res48')
    audivigilancia933 = fields.Boolean('AudiVigilancia933')
    audespecialcertreview = fields.Boolean('AudEspecialCertReview')
    res49 = fields.Integer('Res49')
    res50 = fields.Integer('Res50')
    res51 = fields.Integer('Res51')
    res52 = fields.Integer('Res52')
    res53 = fields.Integer('Res53')
    res54 = fields.Integer('Res54')
    res55 = fields.Integer('Res55')
    res56 = fields.Integer('Res56')
    res57 = fields.Integer('Res57')
    res58 = fields.Integer('Res58')
    res59 = fields.Integer('Res59')
    res60 = fields.Integer('Res60')
    asumregistrocertreview = fields.Boolean('AsumRegistroCertReview')
    res61 = fields.Integer('Res61')
    res62 = fields.Integer('Res62')
    res63 = fields.Integer('Res63')
    res64 = fields.Integer('Res64')
    res65 = fields.Integer('Res65')
    res66 = fields.Integer('Res66')
    res67 = fields.Integer('Res67')
    audit952 = fields.Boolean('Audit952')
    res68 = fields.Integer('Res68')
    res69 = fields.Integer('Res69')
    nomreviewer = fields.Char('NomReviewer')
    paternoreviewer = fields.Char('PaternoReviewer')
    maternoreviewer = fields.Char('MaternoReviewer')
    inicialesreviewer = fields.Char('InicialesReviewer')
    alcance951 = fields.Char('Alcance951')
    sectoractividad = fields.Char('SectorActividad')
    acredited = fields.Boolean('Acredited')
    iaf = fields.Integer('IAF')
    nace = fields.Integer('Nace')
    singlesite = fields.Integer('SingleSite')
    levelrisk = fields.Char('LevelRisk')
    nivelriesgo = fields.Char('NivelRiesgo')
    creadopor = fields.Integer('CreadoPor')
    res80 = fields.Integer('Res80')
    res81 = fields.Integer('Res81')
    res82 = fields.Integer('Res82')
    res83 = fields.Integer('Res83')
    res84 = fields.Integer('Res84')
    res85 = fields.Integer('Res85')
    res86 = fields.Integer('Res86')
    res87 = fields.Integer('Res87')
    res88 = fields.Integer('Res88')
    res89 = fields.Integer('Res89')
    approveddate = fields.Date('ApprovedDate')
    res90 = fields.Integer('Res90')
    res91 = fields.Integer('Res91')
    res92 = fields.Integer('Res92')
    res93 = fields.Integer('Res93')
    res94 = fields.Integer('Res94')
    res95 = fields.Integer('Res95')
    res96 = fields.Integer('Res96')
    res97 = fields.Integer('Res97')
    res98 = fields.Integer('Res98')
    res99 = fields.Integer('Res99')
    res100 = fields.Integer('Res100')
    res101 = fields.Integer('Res101')
    res102 = fields.Integer('Res102')
    res103 = fields.Integer('Res103')
    res104 = fields.Integer('Res104')
    res105 = fields.Integer('Res105')
    res106 = fields.Integer('Res106')
    res107 = fields.Integer('Res107')
    res108 = fields.Integer('Res108')
    res109 = fields.Integer('Res109')
    res110 = fields.Integer('Res110')
    res111 = fields.Integer('Res111')
    alcancesite = fields.Char('AlcanceSite')


class Recomendado(models.Model):
    '''
    Class: Recomendado
    '''
    _name = 'gps.recomendado'
    _description = 'gps.recomendado'
    
    # Original fields
    idrecomendado = fields.Char('IdRecomendado')
    nombre = fields.Char('Nombre')


class NaceCodesUsuariosSoporte(models.Model):
    '''
    Class: NaceCodesUsuariosSoporte
    '''
    _name = 'gps.nacecodesusuariossoporte'
    _description = 'gps.nacecodesusuariossoporte'
    
    # Original fields
    idnacecodesoporte = fields.Char('IdNaceCodeSoporte')
    idusuario = fields.Integer('IdUsuario')
    idnacecode = fields.Integer('IdNaceCode')
    tipoarchivo = fields.Char('TipoArchivo')
    nombrearchivo = fields.Char('NombreArchivo')
    extension = fields.Char('Extension')
    aprobado = fields.Boolean('Aprobado')
    calificacion = fields.Integer('Calificacion')
    comentariosauditor = fields.Char('ComentariosAuditor')
    comentariosadmin = fields.Char('ComentariosAdmin')
    fechacreado = fields.Date('FechaCreado')
    fechaactualizado = fields.Date('FechaActualizado')
    fechaaprobado = fields.Date('FechaAprobado')
    descripcion = fields.Char('Descripcion')


class GnContactSupplier(models.Model):
    '''
    Class: GnContactSupplier
    '''
    _name = 'gps.gncontactsupplier'
    _description = 'gps.gncontactsupplier'
    
    # Original fields
    contactsupplierkey = fields.Char('ContactSupplierKey')
    supplierfk = fields.Char('SupplierFk')
    typecontact = fields.Integer('TypeContact')
    phone = fields.Char('Phone')
    contactname = fields.Char('ContactName')
    contactlast = fields.Char('ContactLast')
    contactlastsecond = fields.Char('ContactLastSecond')
    position = fields.Char('Position')
    email = fields.Char('Email')
    emailsecondary = fields.Char('EmailSecondary')
    mobile = fields.Char('Mobile')


class Consultor(models.Model):
    '''
    Class: Consultor
    '''
    _name = 'gps.consultor'
    _description = 'gps.consultor'
    
    # Original fields
    idconsultor = fields.Integer('IdConsultor')
    nombre = fields.Char('Nombre')
    appaterno = fields.Char('ApPaterno')
    apmaterno = fields.Char('ApMaterno')
    consultoria = fields.Char('Consultoria')
    telefono = fields.Char('Telefono')
    correo = fields.Char('Correo')
    idusuario = fields.Integer('IdUsuario')


class TipoArchivo(models.Model):
    '''
    Class: TipoArchivo
    '''
    _name = 'gps.tipoarchivo'
    _description = 'gps.tipoarchivo'
    
    # Original fields
    tipoarchivo = fields.Char('TipoArchivo')
    modulo = fields.Integer('Modulo')
    idarchivo = fields.Char('IdArchivo')
    abrev = fields.Char('Abrev')


class GnAlert(models.Model):
    '''
    Class: GnAlert
    '''
    _name = 'gps.gnalert'
    _description = 'gps.gnalert'
    
    # Original fields
    alertkey = fields.Char('AlertKey')
    prosclienfk = fields.Char('ProsClienFk')
    message = fields.Char('Message')
    show = fields.Boolean('Show')
    datecreated = fields.Date('DateCreated')


class GnComentario(models.Model):
    '''
    Class: GnComentario
    '''
    _name = 'gps.gncomentario'
    _description = 'gps.gncomentario'
    
    # Original fields
    comentariokey = fields.Char('ComentarioKey')
    eventofk = fields.Char('EventoFk')
    cccfk = fields.Char('CCCFk')
    comentario = fields.Char('Comentario')
    fecha = fields.Date('Fecha')
    aprobado = fields.Boolean('Aprobado')


class ArchivosTracking(models.Model):
    '''
    Class: ArchivosTracking
    '''
    _name = 'gps.archivostracking'
    _description = 'gps.archivostracking'
    
    # Original fields
    idarchivot = fields.Char('IdArchivoT')
    numerotrabajo = fields.Char('NumeroTrabajo')
    nombre = fields.Char('Nombre')
    fecharegistro = fields.Date('fechaRegistro')
    tipoarchivo = fields.Selection(
        selection=[
          ('CliRepP', 'Client Report'),
          ('AudRep', 'Audit Report'),
          ('AudPlanP', 'Audit Plan'),
          ('OpeClos', 'Attendance/Opening and Closing Meeting'),
          ('ResShe', 'Results Sheet')
        ],
        string='Tipo Archivo')
    numeroarchivo = fields.Integer('NumeroArchivo')
    
    #Extended fields
    evento_id = fields.Many2one(comodel_name='gps.eventos', string='Event')


class Fuente(models.Model):
    '''
    Class: Fuente
    '''
    _name = 'gps.fuente'
    _description = 'gps.fuente'
    _rec_name = 'nombre'
    
    # Original fields
    idfuente = fields.Integer('IdFuente')
    nombre = fields.Char('Nombre')


class NaceCodesUsuariosSoporteCV(models.Model):
    '''
    Class: NaceCodesUsuariosSoporteCV
    '''
    _name = 'gps.nacecodesusuariossoportecv'
    _description = 'gps.nacecodesusuariossoportecv'
    
    # Original fields
    idnacecodesoporte = fields.Char('IdNaceCodeSoporte')
    idusuario = fields.Integer('IdUsuario')
    idnacecode = fields.Integer('IdNaceCode')
    tipoarchivo = fields.Char('TipoArchivo')
    nombrearchivo = fields.Char('NombreArchivo')
    extension = fields.Char('Extension')
    aprobado = fields.Boolean('Aprobado')
    calificacion = fields.Integer('Calificacion')
    comentariosauditor = fields.Char('ComentariosAuditor')
    comentariosadmin = fields.Char('ComentariosAdmin')
    fechacreado = fields.Date('FechaCreado')
    fechaactualizado = fields.Date('FechaActualizado')
    fechaaprobado = fields.Date('FechaAprobado')


class Ciudades(models.Model):
    '''
    Class: Ciudades
    '''
    _name = 'gps.ciudades'
    _description = 'gps.ciudades'
    
    # Original fields
    idciudad = fields.Char('IdCiudad')
    nombre = fields.Char('Nombre')
    noestado = fields.Integer('NoEstado')
    estado = fields.Char('Estado')
    idestado = fields.Char('IdEstado')


class GnSitio(models.Model):
    '''
    Class: GnSitio
    '''
    _name = 'gps.gnsitio'
    _description = 'gps.gnsitio'
    
    # Original fields
    sitiokey = fields.Char('SitioKey')
    eventofk = fields.Char('EventoFk')
    cccfk = fields.Char('CCCFk')
    sitio = fields.Char('Sitio')


class GnSupplierEventReport(models.AbstractModel):
    _name = 'report.gpsi.gsos_audit_final_report'
    
    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        docargs = {
            'docs': self._generate_docs()
        }
        return report_obj.render('gpsi.gsos_audit_final_report_template', docargs)
    
    def _generate_docs(self):
        docs = []
        for report in self:
            event = self.env['gps.gnsupplierevent'].search([['id', '=', report.id]])
            doc = {
                'supplier': self._generate_supplier_info(event),
                'summary_audit': event.auditnotes,
                'sections': self._generate_sections(event)
            }
            docs.append(doc)
        return docs
    
    def _generate_supplier_info(self, event):
        info = {
            'name': event.supplier_id.providername,
            'model': event.model_id.modelname,
            'address': event.supplier_id.adresstax
        }
        return info
    
    def _generate_sections(self, event):
        sections = []
        for section in event.model_id.section_ids:
            section_data = {
                'name': section.sectiondescription,
                'questions': self._generate_questions(section)
            }
            sections.append(section_data)
        return sections
        
    def _generate_questions(self, section):
        questions = []
        for question in section.question_ids:
            evidences = self.env['gps.gnevidence'].search([['question_id', '=', question.id]])
            evidence = evidences and evidences[0] or False
            question_data = {
                'description': question.questiondescription,
                'rating': evidence.initial,
                'nonconformance': evidence.evidence
            }
            questions.append(question_data)
        return questions
    
    
class GnSupplierEvent(models.Model):
    '''
    Class: GnSupplierEvent
    '''
    _name = 'gps.gnsupplierevent'
    _description = 'gps.gnsupplierevent'
    _inherit = 'mail.thread' 
    _order = 'startdate desc'
    _rec_name = 'id'
    
    # Original fields
    suppliereventkey = fields.Char('SupplierEventKey')
    supplierfk = fields.Char('SupplierFk')
    modelfk = fields.Char('ModelFk')
    creationdate = fields.Date('CreationDate')
    startdate = fields.Date('StartDate')
    enddate = fields.Date('EndDate')
    statusevent = fields.Integer('StatusEvent')
    scope = fields.Text('Scope')
    answerscompleted = fields.Boolean('AnswersCompleted')
    auditnotes = fields.Text('AuditNotes')
    productsorlinestoaudit = fields.Text('ProductsOrLinesToAudit')
    productsthatprovide = fields.Text('ProductsThatProvide')
    eventconfirmdate = fields.Date('EventConfirmDate')
    reviewed = fields.Boolean('Reviewed')
    
    # Extended fields
    supplier_id = fields.Many2one(comodel_name='gps.gnsupplier', string='Supplier')
    prosclient_id = fields.Many2one(related='supplier_id.prosclient_id', string='Client')
    model_id = fields.Many2one(comodel_name='gps.gnmodel', string='Model')
    auditor_ids = fields.One2many(comodel_name='gps.gnauditorinsupplierevent', inverse_name='event_id', string='Auditors')
    statusevent = fields.Selection(selection=[(1, 'Scheduled'), (2, 'Confirmed'), (3, 'Executed'), (4, 'Closed'), (5, 'Canceled')], 
        default=1, string='Event Status')
    evidence_count = fields.Integer(compute='_get_evidence_count', string='Number events attached');
    
    @api.model
    def create(self, vals):
        event = super(GnSupplierEvent, self).create(vals)
        event._create_evidences()
        return event
    
    @api.multi
    def write(self, vals):
        return super(GnSupplierEvent, self).write(vals)
    
    def _get_evidence_count(self):
        for event in self:
            evidences = self.env['gps.gnevidence'].search([['event_id', '=', event.id]])
            event.evidence_count = len(evidences)
    
    @api.multi
    def _create_evidences(self):
        for event in self:
            if event.evidence_count == 0 and event.model_id:
                models = self.env['gps.gnmodel'].search([['id', '=', event.model_id.id]])
                model_id = models and models[0] or False
                for section in model_id.section_ids:
                    for question in section.question_ids:
                        evidence = {
                            'event_id': event.id,
                            'question_id': question.id,
                            'section_id': section.id
                        }
                        self.env['gps.gnevidence'].create(evidence)


class Ubicaciones(models.Model):
    '''
    Class: Ubicaciones
    '''
    _name = 'gps.ubicaciones'
    _description = 'gps.ubicaciones'
    _rec_name = 'direccion'
    
    # Original fields
    idubicacion = fields.Char('IdUbicacion')
    idciudad = fields.Char('IdCiudad')
    direccion = fields.Text('Direccion')


class GnGraficar(models.Model):
    '''
    Class: GnGraficar
    '''
    _name = 'gps.gngraficar'
    _description = 'gps.gngraficar'
    
    # Original fields
    graficarkey = fields.Char('GraficarKey')
    clavegrupo = fields.Integer('ClaveGrupo')
    descripcion = fields.Char('Descripcion')
    valor = fields.Float('Valor')


class CorreosTrakingHistorial(models.Model):
    '''
    Class: CorreosTrakingHistorial
    '''
    _name = 'gps.correostrakinghistorial'
    _description = 'gps.correostrakinghistorial'
    
    # Original fields
    idcorreos = fields.Char('IdCorreos')
    numerotrabajo = fields.Char('NumeroTrabajo')
    fecha = fields.Date('fecha')
    numeroarchivo = fields.Integer('NumeroArchivo')


class UsuariosFoto(models.Model):
    '''
    Class: UsuariosFoto
    '''
    _name = 'gps.usuariosfoto'
    _description = 'gps.usuariosfoto'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    nombrearchivo = fields.Char('NombreArchivo')


class UbicacionesCliente(models.Model):
    '''
    Class: UbicacionesCliente
    '''
    _name = 'gps.ubicacionescliente'
    _description = 'gps.ubicacionescliente'
    
    # Original fields
    idcliente = fields.Char('IdCliente')
    idubicacion = fields.Char('IdUbicacion')
    descripcion = fields.Char('Descripcion')
    location = fields.Integer('Location')
    
    #Extended fields
    cliente_id = fields.Many2one(comodel_name='gps.clientes', string='Client')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')


class GnEvaluationQuestion(models.Model):
    '''
    Class: GnEvaluationQuestion
    '''
    _name = 'gps.gnevaluationquestion'
    _description = 'gps.gnevaluationquestion'
    
    # Original fields
    evaluationquestionkey = fields.Char('EvaluationQuestionKey')
    prosclienfk = fields.Char('ProsClienFk')
    question = fields.Char('Question')


class ArchivoHistorial(models.Model):
    '''
    Class: ArchivoHistorial
    '''
    _name = 'gps.archivohistorial'
    _description = 'gps.archivohistorial'
    
    # Original fields
    idarchivo = fields.Char('IdArchivo')
    numerotrabajo = fields.Char('NumeroTrabajo')
    nombre = fields.Char('Nombre')
    fecha = fields.Date('Fecha')
    numeroarchivo = fields.Integer('NumeroArchivo')


class UbicacionesContrato(models.Model):
    '''
    Class: UbicacionesContrato
    '''
    _name = 'gps.ubicacionescontrato'
    _description = 'gps.ubicacionescontrato'
    
    # Original fields
    idcontrato = fields.Char('IdContrato')
    idubicacion = fields.Char('IdUbicacion')
    location = fields.Integer('Location')
    
    # Extended fields
    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Contracts')
    ubicacion_id = fields.Many2one(comodel_name='gps.ubicaciones', string='Location')


class GnEvaluationAnswer(models.Model):
    '''
    Class: GnEvaluationAnswer
    '''
    _name = 'gps.gnevaluationanswer'
    _description = 'gps.gnevaluationanswer'
    
    # Original fields
    evaluationanswerkey = fields.Char('EvaluationAnswerKey')
    evaluationquestionfk = fields.Char('EvaluationQuestionFk')
    suppliereventfk = fields.Char('SupplierEventFk')
    answer = fields.Char('Answer')
    points = fields.Integer('Points')


class NaceCodesUsuariosSoporteArchivos(models.Model):
    '''
    Class: NaceCodesUsuariosSoporteArchivos
    '''
    _name = 'gps.nacecodesusuariossoportearchivos'
    _description = 'gps.nacecodesusuariossoportearchivos'
    
    # Original fields
    idnacecodesoporte = fields.Char('IdNaceCodeSoporte')
    idnacecodesoportearchivo = fields.Char('IdNaceCodeSoporteArchivo')


class LogUser(models.Model):
    '''
    Class: LogUser
    '''
    _name = 'gps.loguser'
    _description = 'gps.loguser'
    
    # Original fields
    idloguser = fields.Integer('IdLogUser')
    idusuario = fields.Integer('IdUsuario')
    nicknamecliente = fields.Char('NickNameCliente')
    contraseniaanterior = fields.Char('ContraseniaAnterior')
    contraseniaact = fields.Char('ContraseniaAct')
    contraseniaantermd5 = fields.Char('ContraseniaAntermd5')
    contraseniaactmd5 = fields.Char('ContraseniaActmd5')
    fechacreacion = fields.Date('FechaCreacion')
    fechaactualizacion = fields.Date('FechaActualizacion')
    idusuariomod = fields.Integer('IdUsuarioMod')


class UsuarioEnProceso(models.Model):
    '''
    Class: UsuarioEnProceso
    '''
    _name = 'gps.usuarioenproceso'
    _description = 'gps.usuarioenproceso'
    
    # Original fields
    usuarioenprocesokey = fields.Char('UsuarioEnProcesoKey')
    idprocesofk = fields.Integer('IdProcesoFk')
    idusuariofk = fields.Integer('IdUsuarioFk')


class GnEvidence(models.Model):
    '''
    Class: GnEvidence
    '''
    _name = 'gps.gnevidence'
    _description = 'gps.gnevidence'
    _rec_name='id'
    
    # Original fields
    evidencekey = fields.Char('EvidenceKey')
    suppliereventfk = fields.Char('SupplierEventFk')
    questionfk = fields.Char('QuestionFk')
    sectionfk = fields.Char('SectionFk')
    evidence = fields.Text('Evidence')
    initial = fields.Selection(selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('NA', 'NA')], string='Initial', default='NA')
    points = fields.Float('Points')
    modelfk = fields.Char('ModelFk')
    
    # Extended fields
    event_id = fields.Many2one(comodel_name='gps.gnsupplierevent', string='Event')
    question_id = fields.Many2one(comodel_name='gps.gnquestion', string='Question')
    section_id = fields.Many2one(comodel_name='gps.gnsection', string='Section')
    question_desc = fields.Text(related='question_id.questiondescription', string='Description')
    question_is_important = fields.Boolean(related='question_id.isimportant')
    
    @api.onchange('initial')
    def on_change_initial(self):
        values = {'A': 1, 'B': 0.8, 'C': 0.3, 'D': 0, 'NA': 0};
        if self.initial in values:
            self.points = values[self.initial]


class MD5QMSRange(models.Model):
    '''
    Class: MD5QMSRange
    '''
    _name = 'gps.md5qms.range'
    _description = 'gps.md5qms.range'
    
    md5qms_id = fields.Many2one(comodel_name='gps.md5qms', string='MD5QMS')
    min_employees = fields.Integer('Min Employees')
    max_employees = fields.Integer('Max Employees')
    md5 = fields.Float('MD5')
    stage1 = fields.Float('Stage 1')
    stage2 = fields.Float('Stage 2')
    biannual = fields.Float('Biannual')
    annual = fields.Float('Annual')
    
    
class MD5QMS(models.Model):
    '''
    Class: MD5QMS
    '''
    _name = 'gps.md5qms'
    _description = 'gps.md5qms'
    _rec_name='id'
    
    # Original fields
    idmd5qms = fields.Integer('IdMD5QMS')
    numempleados = fields.Char('NumEmpleados')
    diasauditor = fields.Float('DiasAuditor')
    
    # Extended fields
    standard_id = fields.Many2one(comodel_name='gps.habilidades', string='Standard')
    min_employees = fields.Integer('Min Employees')
    max_employees = fields.Integer('Max Employees')
    risk_level = fields.Selection(selection=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low'), ('limit', 'Limit')], string='Risk Level')
    code = fields.Text('Python Code')
    ranges = fields.One2many(comodel_name='gps.md5qms.range', inverse_name='md5qms_id', string='Ranges')
        
    @api.multi
    def get_audit_times(self, num_employees):
        audit_times = {
            'stage1': 0.5,
            'stage2': 1,
            'biannual': 1.5,
            'annual': 2.5
        }
        return audit_times


class ComentarioCliente(models.Model):
    '''
    Class: ComentarioCliente
    '''
    _name = 'gps.comentariocliente'
    _description = 'gps.comentariocliente'
    
    # Original fields
    idcliente = fields.Char('IdCliente')
    idoficina = fields.Char('IdOficina')
    idproceso = fields.Integer('IdProceso')
    comentario = fields.Char('Comentario')
    fecha = fields.Date('Fecha')
    iduserconnected = fields.Integer('IdUserConnected')
    comentarioclientekey = fields.Char('ComentarioClienteKey')


class RangoEstandaresCalidad(models.Model):
    '''
    Class: RangoEstandaresCalidad
    '''
    _name = 'gps.rangoestandarescalidad'
    _description = 'gps.rangoestandarescalidad'
    
    # Original fields
    idd = fields.Integer('Id')
    rango_inicial = fields.Integer('Rango_Inicial')
    rango_final = fields.Integer('Rango_Final')
    cve_estandar = fields.Integer('Cve_Estandar')
    descripcion = fields.Char('Descripcion')
    fechaalta = fields.Date('FechaAlta')
    fechabaja = fields.Date('FechaBaja')
    estatus = fields.Boolean('Estatus')


class GnSupplierContact(models.Model):
    '''
    Class: GnSupplierContact
    '''
    _name = 'gps.gnsuppliercontact'
    _description = 'gps.gnsuppliercontact'
    
    # Original fields
    suppliercontactkey = fields.Char('SupplierContactKey')
    supplierfk = fields.Char('SupplierFk')
    contactname = fields.Char('ContactName')
    contactemail = fields.Char('ContactEmail')
    contactphone = fields.Char('ContactPhone')


class log_track(models.Model):
    '''
    Class: log_track
    '''
    _name = 'gps.log_track'
    _description = 'gps.log_track'
    
    # Original fields
    step = fields.Char('step')
    fechalog = fields.Date('FechaLog')


class TrackingEjecuciones(models.Model):
    '''
    Class: TrackingEjecuciones
    '''
    _name = 'gps.trackingejecuciones'
    _description = 'gps.trackingejecuciones'
    
    # Original fields
    fechaejecucion = fields.Date('FechaEjecucion')
    step = fields.Char('Step')


class GnSupplierFileType(models.Model):
    '''
    Class: GnSupplierFileType
    '''
    _name = 'gps.gnsupplierfiletype'
    _description = 'gps.gnsupplierfiletype'
    
    # Original fields
    supplierfiletypekey = fields.Char('SupplierFileTypeKey')
    filedescription = fields.Char('FileDescription')
    filetype = fields.Integer('FileType')


class ErrLog(models.Model):
    '''
    Class: ErrLog
    '''
    _name = 'gps.errlog'
    _description = 'gps.errlog'
    
    # Original fields
    idlog = fields.Integer('IdLog')
    descripcion = fields.Char('Descripcion')
    mensajeerr = fields.Char('MensajeErr')
    fecha = fields.Date('Fecha')
    pagina_aspx = fields.Char('Pagina_Aspx')


class GnSupplierFile(models.Model):
    '''
    Class: GnSupplierFile
    '''
    _name = 'gps.gnsupplierfile'
    _description = 'gps.gnsupplierfile'
    
    # Original fields
    supplierfilekey = fields.Char('SupplierFileKey')
    supplierfk = fields.Char('SupplierFk')
    filename = fields.Char('FileName')
    supplierfiletypefk = fields.Char('SupplierFileTypeFk')


class GnComplaint(models.Model):
    '''
    Class: GnComplaint
    '''
    _name = 'gps.gncomplaint'
    _description = 'gps.gncomplaint'
    _inherit = 'mail.thread' 
    _rec_name = 'id'
    
    # Original fields
    complaintkey = fields.Char('ComplaintKey')
    supplierfk = fields.Char('SupplierFk')
    datecomplaint = fields.Date('DateComplaint')
    descriptioncomp = fields.Text('DescriptionComp')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')
    supplier_id = fields.Many2one(comodel_name='gps.gnsupplier', string='Service')


class Deseos(models.Model):
    '''
    Class: Deseos
    '''
    _name = 'gps.deseos'
    _description = 'gps.deseos'
    
    # Original fields
    iddeseo = fields.Char('IdDeseo')
    idsolicitante = fields.Integer('IdSolicitante')
    descripcion = fields.Char('Descripcion')
    porcentajeavance = fields.Integer('PorcentajeAvance')
    estado = fields.Integer('Estado')
    fechainicio = fields.Date('FechaInicio')
    orden = fields.Integer('Orden')
    archivodescripcion = fields.Char('archivoDescripcion')
    fechaultimocambio = fields.Date('FechaUltimoCambio')
    fechafinalizado = fields.Date('FechaFinalizado')
    fechacienporciento = fields.Date('FechaCienPorciento')


class GnSupplierEventsFile(models.Model):
    '''
    Class: GnSupplierEventsFile
    '''
    _name = 'gps.gnsuppliereventsfile'
    _description = 'gps.gnsuppliereventsfile'
    
    # Original fields
    suppliereventsfilekey = fields.Char('SupplierEventsFileKey')
    suppliereventfk = fields.Char('SupplierEventFk')
    filetype = fields.Integer('FileType')
    filename = fields.Char('FileName')
    filedescription = fields.Char('FileDescription')


class InformacionGeneral(models.Model):
    '''
    Class: InformacionGeneral
    '''
    _name = 'gps.informaciongeneral'
    _description = 'gps.informaciongeneral'
    
    # Original fields
    idinformaciongeneral = fields.Char('IdInformacionGeneral')
    item = fields.Char('Item')
    valor = fields.Char('Valor')
    descripcion = fields.Char('Descripcion')


class HistorialEnvioDeCorreos(models.Model):
    '''
    Class: HistorialEnvioDeCorreos
    '''
    _name = 'gps.historialenviodecorreos'
    _description = 'gps.historialenviodecorreos'
    
    # Original fields
    idenviocorreo = fields.Char('IdEnvioCorreo')
    idde = fields.Char('IdDe')
    idpara = fields.Integer('IdPara')
    tablatipo = fields.Integer('TablaTipo')
    fechaenvio = fields.Date('FechaEnvio')
    de = fields.Char('De')
    para = fields.Char('Para')
    asunto = fields.Char('Asunto')
    contenido = fields.Char('Contenido')
    status = fields.Integer('Status')
    importancia = fields.Integer('Importancia')


class GnAuditorSecondPart(models.Model):
    '''
    Class: GnAuditorSecondPart
    '''
    _name = 'gps.gnauditorsecondpart'
    _description = 'gps.gnauditorsecondpart'
    
    # Original fields
    auditorsecondpartkey = fields.Char('AuditorSecondPartKey')
    nickname = fields.Char('NickName')
    password = fields.Char('Password')
    name = fields.Char('Name')
    lastname = fields.Char('LastName')
    mothermaidenname = fields.Char('MotherMaidenName')


class NoConformidades(models.Model):
    '''
    Class: NoConformidades
    '''
    _name = 'gps.noconformidades'
    _description = 'gps.noconformidades'
    _rec_name = 'id'
    
    # Original fields
    idnoconformidad = fields.Char('IdNoConformidad')
    idcliente = fields.Char('IdCliente')
    numerotrabajo = fields.Char('NumeroTrabajo')
    sentencia = fields.Text('Sentencia')
    sentenciaarchivo = fields.Char('SentenciaArchivo')
    tipo = fields.Selection(selection=[(1, 'Low'), (2, 'High')], default=1, string='Severity')
    contencion = fields.Text('Contencion')
    contencionarchivo = fields.Char('ContencionArchivo')
    causaraiz = fields.Text('CausaRaiz')
    causaraizarchivo = fields.Char('CausaRaizArchivo')
    implementacion = fields.Text('Implementacion')
    implementacionarchivo = fields.Char('ImplementacionArchivo')
    status = fields.Integer('Status')
    notas = fields.Char('Notas')
    fechaapertura = fields.Date('FechaApertura')
    fechacierre = fields.Date('FechaCierre')
    cierrecount = fields.Integer('CierreCount')
    fechacambio = fields.Date('FechaCambio')
    insite = fields.Boolean('InSite')
    
    # Extended fields
    evento_id = fields.Many2one(comodel_name='gps.eventos', string='Event')
    cliente_id = fields.Many2one(comodel_name='gps.clientes', string='Client')


class GnModelOfEvent(models.Model):
    '''
    Class: GnModelOfEvent
    '''
    _name = 'gps.gnmodelofevent'
    _description = 'gps.gnmodelofevent'
    
    # Original fields
    modelofeventkey = fields.Char('ModelOfEventKey')
    suppliereventfk = fields.Char('SupplierEventFk')
    modelfk = fields.Char('ModelFk')


class GnAuditorModel(models.Model):
    '''
    Class: GnAuditorModel
    '''
    _name = 'gps.gnauditormodel'
    _description = 'gps.gnauditormodel'
    
    # Original fields
    auditormodelkey = fields.Char('AuditorModelKey')
    auditorsecondpartfk = fields.Char('AuditorSecondPartFk')
    modelfk = fields.Char('ModelFk')
    idusuario = fields.Integer('IdUsuario')
    
    # Extended fields
    usuario_id = fields.Many2one(comodel_name='res.users', string='Auditor')
    model_id = fields.Many2one(comodel_name='gps.gnmodel', string='Checklist')
    leader = fields.Boolean(string="Leader")


class Estados(models.Model):
    '''
    Class: Estados
    '''
    _name = 'gps.estados'
    _description = 'gps.estados'
    _rec_name = 'nombre'
    
    # Original fields
    idestado = fields.Char('IdEstado')
    idpais = fields.Char('IdPais')
    numero = fields.Integer('Numero')
    nombre = fields.Char('Nombre')
    abreviacion = fields.Char('Abreviacion')


class Paises(models.Model):
    '''
    Class: Paises
    '''
    _name = 'gps.paises'
    _description = 'gps.paises'
    
    # Original fields
    idpais = fields.Char('IdPais')
    numero = fields.Integer('Numero')
    nombre = fields.Char('Nombre')
    abreviacion = fields.Char('Abreviacion')
    continente = fields.Integer('Continente')


class GnAuditorInSupplierEvent(models.Model):
    '''
    Class: GnAuditorInSupplierEvent
    '''
    _name = 'gps.gnauditorinsupplierevent'
    _description = 'gps.gnauditorinsupplierevent'
    
    # Original fields
    auditorinsuppliereventkey = fields.Char('AuditorInSupplierEventKey')
    suppliereventfk = fields.Char('SupplierEventFk')
    auditorsecondpartfk = fields.Integer('AuditorSecondPartFk')
    
    #Extended fields
    usuario_id = fields.Many2one(comodel_name='res.users', string='Auditor')
    event_id = fields.Many2one(comodel_name='gps.gnsupplierevent', string='Auditors')
    leader = fields.Boolean(string="Leader")


class ArchivosEvento(models.Model):
    '''
    Class: ArchivosEvento
    '''
    _name = 'gps.archivosevento'
    _description = 'gps.archivosevento'
    
    # Original fields
    idarchivo = fields.Integer('IdArchivo')
    numerotrabajo = fields.Char('NumeroTrabajo')
    nombrearchivo = fields.Char('NombreArchivo')


class Cursos(models.Model):
    '''
    Class: Cursos
    '''
    _name = 'gps.cursos'
    _description = 'gps.cursos'
    
    # Original fields
    idcurso = fields.Integer('IdCurso')
    idnacecodesoporte = fields.Char('IdNaceCodeSoporte')
    idhabilidad = fields.Integer('IdHabilidad')
    idusuario = fields.Integer('IdUsuario')


class GnResolution(models.Model):
    '''
    Class: GnResolution
    '''
    _name = 'gps.gnresolution'
    _description = 'gps.gnresolution'
    
    # Original fields
    resolutionkey = fields.Char('ResolutionKey')
    supplierfk = fields.Char('SupplierFk')
    suppliereventfk = fields.Char('SupplierEventFk')
    dateregister = fields.Date('DateRegister')
    resolution = fields.Integer('Resolution')


class Oficinas(models.Model):
    '''
    Class: Oficinas
    '''
    _name = 'gps.oficinas'
    _description = 'gps.oficinas'
    
    # Original fields
    idoficina = fields.Char('IdOficina')
    idubicacion = fields.Char('IdUbicacion')
    codigo = fields.Integer('Codigo')
    nombre = fields.Char('Nombre')
    esprincipal = fields.Boolean('EsPrincipal')


class HistorialEnvioDeCorreos_bkp(models.Model):
    '''
    Class: HistorialEnvioDeCorreos_bkp
    '''
    _name = 'gps.historialenviodecorreos_bkp'
    _description = 'gps.historialenviodecorreos_bkp'
    
    # Original fields
    idenviocorreo = fields.Char('IdEnvioCorreo')
    idde = fields.Char('IdDe')
    idpara = fields.Integer('IdPara')
    tablatipo = fields.Integer('TablaTipo')
    fechaenvio = fields.Date('FechaEnvio')
    de = fields.Char('De')
    para = fields.Char('Para')
    asunto = fields.Char('Asunto')
    contenido = fields.Char('Contenido')
    status = fields.Integer('Status')
    importancia = fields.Integer('Importancia')


class ComentariosTracking(models.Model):
    '''
    Class: ComentariosTracking
    '''
    _name = 'gps.comentariostracking'
    _description = 'gps.comentariostracking'
    
    # Original fields
    comentariostrackingkey = fields.Char('ComentariosTrackingKey')
    comentarios = fields.Char('Comentarios')
    numerotrabajo = fields.Char('NumeroTrabajo')


class NoConformidadHistorial(models.Model):
    '''
    Class: NoConformidadHistorial
    '''
    _name = 'gps.noconformidadhistorial'
    _description = 'gps.noconformidadhistorial'
    
    # Original fields
    idnoconformidadhistorial = fields.Char('IdNoConformidadHistorial')
    idnoconformidad = fields.Char('IdNoConformidad')
    contencion = fields.Char('Contencion')
    contencionarchivo = fields.Char('ContencionArchivo')
    causaraiz = fields.Char('CausaRaiz')
    causaraizarchivo = fields.Char('CausaRaizArchivo')
    implementacion = fields.Char('Implementacion')
    implementacionarchivo = fields.Char('ImplementacionArchivo')
    fechaenvio = fields.Date('FechaEnvio')


class GnComplaintReached(models.Model):
    '''
    Class: GnComplaintReached
    '''
    _name = 'gps.gncomplaintreached'
    _description = 'gps.gncomplaintreached'
    
    # Original fields
    complaintreachedkey = fields.Char('ComplaintReachedKey')
    supplierfk = fields.Char('SupplierFk')
    datereached = fields.Date('DateReached')
    permmited = fields.Integer('Permmited')
    numbercomplaints = fields.Integer('NumberComplaints')


class Personas(models.Model):
    '''
    Class: Personas
    '''
    _name = 'gps.personas'
    _description = 'gps.personas'
    
    # Original fields
    idpersona = fields.Char('IdPersona')
    idcliente = fields.Char('IdCliente')
    nombres = fields.Char('Nombres')
    apellidopaterno = fields.Char('ApellidoPaterno')
    apellidomaterno = fields.Char('ApellidoMaterno')
    correo = fields.Char('Correo')
    telefono = fields.Char('Telefono')
    baja = fields.Boolean('Baja')
    fechabaja = fields.Date('FechaBaja')
    comentariospersona = fields.Char('ComentariosPersona')


class ArchivosUsuarios(models.Model):
    '''
    Class: ArchivosUsuarios
    '''
    _name = 'gps.archivosusuarios'
    _description = 'gps.archivosusuarios'
    
    # Original fields
    idarchivo = fields.Integer('IdArchivo')
    idnacecodesoporte = fields.Char('IdNaceCodeSoporte')
    idusuario = fields.Integer('IdUsuario')
    idnacecode = fields.Integer('IdNaceCode')
    tipoarchivo = fields.Char('TipoArchivo')
    nombrearchivo = fields.Char('NombreArchivo')


class GnDisableDayAuditor(models.Model):
    '''
    Class: GnDisableDayAuditor
    '''
    _name = 'gps.gndisabledayauditor'
    _description = 'gps.gndisabledayauditor'
    
    # Original fields
    disabledayauditorkey = fields.Char('DisableDayAuditorKey')
    auditorsecondpartfk = fields.Integer('AuditorSecondPartFk')
    day = fields.Date('Day')


class PersonasEvento(models.Model):
    '''
    Class: PersonasEvento
    '''
    _name = 'gps.personasevento'
    _description = 'gps.personasevento'
    
    # Original fields
    idevento = fields.Char('IdEvento')
    idpersona = fields.Char('IdPersona')
    costo = fields.Float('costo')
    tipomoneda = fields.Char('TipoMoneda')


class GnHolydays(models.Model):
    '''
    Class: GnHolydays
    '''
    _name = 'gps.gnholydays'
    _description = 'gps.gnholydays'
    
    # Original fields
    holydayskey = fields.Char('HolydaysKey')
    day = fields.Date('Day')


class GnAuditReport(models.Model):
    '''
    Class: GnAuditReport
    '''
    _name = 'gps.gnauditreport'
    _description = 'gps.gnauditreport'
    
    # Original fields
    auditreportkey = fields.Char('AuditReportKey')
    numtrabajo = fields.Char('NumTrabajo')
    reference41 = fields.Char('Reference41')
    result41 = fields.Char('Result41')
    reference42 = fields.Char('Reference42')
    result42 = fields.Char('Result42')
    reference421 = fields.Char('Reference421')
    result421 = fields.Char('Result421')
    reference422 = fields.Char('Reference422')
    result422 = fields.Char('Result422')


class EventosHistorial(models.Model):
    '''
    Class: EventosHistorial
    '''
    _name = 'gps.eventoshistorial'
    _description = 'gps.eventoshistorial'
    
    # Original fields
    ideventohistorial = fields.Char('IdEventoHistorial')
    idusuario = fields.Integer('IdUsuario')
    numerotrabajo = fields.Char('NumeroTrabajo')
    notaauditor = fields.Char('NotaAuditor')
    notarevisor = fields.Char('NotaRevisor')
    notacomite = fields.Char('NotaComite')
    fechaactualizacion = fields.Date('FechaActualizacion')
    estadoevento = fields.Integer('EstadoEvento')


class GnRight(models.Model):
    '''
    Class: GnRight
    '''
    _name = 'gps.gnright'
    _description = 'gps.gnright'
    
    # Original fields
    rightkey = fields.Char('RightKey')
    numberright = fields.Integer('NumberRight')
    rightname = fields.Char('RightName')
    numbercategory = fields.Integer('NumberCategory')


class Archivos(models.Model):
    '''
    Class: Archivos
    '''
    _name = 'gps.archivos'
    _description = 'gps.archivos'
    
    # Original fields
    idarchivo = fields.Char('IdArchivo')
    idpropietario = fields.Char('IdPropietario')
    nombre = fields.Char('Nombre')
    fecharegistro = fields.Date('FechaRegistro')
    descripcion = fields.Char('Descripcion')


class GnUsuariosRight(models.Model):
    '''
    Class: GnUsuariosRight
    '''
    _name = 'gps.gnusuariosright'
    _description = 'gps.gnusuariosright'
    
    # Original fields
    usuariosrightkey = fields.Char('UsuariosRightKey')
    idusuariofk = fields.Integer('IdUsuarioFk')
    rightfk = fields.Char('RightFk')


class EventosConfirmacion(models.Model):
    '''
    Class: EventosConfirmacion
    '''
    _name = 'gps.eventosconfirmacion'
    _description = 'gps.eventosconfirmacion'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    confirmado = fields.Boolean('Confirmado')
    fecha = fields.Date('Fecha')
    consultoriaprevia = fields.Boolean('ConsultoriaPrevia')
    comentarios = fields.Char('Comentarios')
    confirmaprogramacion = fields.Integer('ConfirmaProgramacion')
    conflictointereses = fields.Boolean('ConflictoIntereses')


class GnDepartment(models.Model):
    '''
    Class: GnDepartment
    '''
    _name = 'gps.gndepartment'
    _description = 'gps.gndepartment'
    
    # Original fields
    departmentkey = fields.Char('DepartmentKey')
    departmentname = fields.Char('DepartmentName')


class GnSourceClient(models.Model):
    '''
    Class: GnSourceClient
    '''
    _name = 'gps.gnsourceclient'
    _description = 'gps.gnsourceclient'
    
    # Original fields
    sourceclientkey = fields.Char('SourceClientKey')
    sourcename = fields.Char('SourceName')
    orden = fields.Integer('Orden')


class GnUsuariosDepartment(models.Model):
    '''
    Class: GnUsuariosDepartment
    '''
    _name = 'gps.gnusuariosdepartment'
    _description = 'gps.gnusuariosdepartment'
    
    # Original fields
    usuariosdepartmentkey = fields.Char('UsuariosDepartmentKey')
    idusuariofk = fields.Integer('IdUsuarioFk')
    departmentfk = fields.Char('DepartmentFk')


class GnIndustrialSector(models.Model):
    '''
    Class: GnIndustrialSector
    '''
    _name = 'gps.gnindustrialsector'
    _description = 'gps.gnindustrialsector'
    _rec_name = 'industrialsectorname'
    
    # Original fields
    industrialsectorkey = fields.Char('IndustrialSectorKey')
    industrialsectorname = fields.Char('IndustrialSectorName')
    orden = fields.Integer('Orden')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')


class GnStateContact(models.Model):
    '''
    Class: GnStateContact
    '''
    _name = 'gps.gnstatecontact'
    _description = 'gps.gnstatecontact'
    
    # Original fields
    statecontactkey = fields.Char('StateContactKey')
    statecontactname = fields.Char('StateContactName')
    orden = fields.Integer('Orden')


class EventosFacturacion(models.Model):
    '''
    Class: EventosFacturacion
    '''
    _name = 'gps.eventosfacturacion'
    _description = 'gps.eventosfacturacion'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    estatus = fields.Integer('Estatus')
    pagado = fields.Boolean('Pagado')
    fechapagado = fields.Date('FechaPagado')
    fechaactualizacion = fields.Date('FechaActualizacion')
    fechafacturado = fields.Date('FechaFacturado')
    idusuario = fields.Integer('IdUsuario')
    comentarios = fields.Text('Comentarios')
    
    # Extended fields
    evento_id = fields.Many2one(comodel_name='gps.eventos', string='Event')
    usuario_id = fields.Many2one(comodel_name='res.users', string='User')
    estatus2 = fields.Selection(selection=[('0', 'Pendiente de Facturar'), ('1', 'Facturado'), ('2', 'NA'),], string='Status')


class GnChatMessage(models.Model):
    '''
    Class: GnChatMessage
    '''
    _name = 'gps.gnchatmessage'
    _description = 'gps.gnchatmessage'
    
    # Original fields
    chatmessagekey = fields.Char('ChatMessageKey')
    message = fields.Char('Message')
    creationdate = fields.Date('CreationDate')
    nickname = fields.Char('NickName')


class GnGlobalService(models.Model):
    '''
    Class: GnGlobalService
    '''
    _name = 'gps.gnglobalservice'
    _description = 'gps.gnglobalservice'
    
    # Original fields
    servicekey = fields.Char('ServiceKey')
    servicename = fields.Char('ServiceName')
    orden = fields.Integer('Orden')


class GnCourse(models.Model):
    '''
    Class: GnCourse
    '''
    _name = 'gps.gncourse'
    _description = 'gps.gncourse'
    
    # Original fields
    coursekey = fields.Char('CourseKey')
    coursename = fields.Char('CourseName')
    orden = fields.Integer('Orden')


class GnStandar(models.Model):
    '''
    Class: GnStandar
    '''
    _name = 'gps.gnstandar'
    _description = 'gps.gnstandar'
    
    # Original fields
    standarkey = fields.Char('StandarKey')
    standarname = fields.Char('StandarName')
    orden = fields.Integer('Orden')


class Usuarios(models.Model):
    '''
    Class: Usuarios
    '''
    _name = 'gps.usuarios'
    _description = 'gps.usuarios'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    nickname = fields.Char('NickName')
    password = fields.Char('Password')
    nombres = fields.Char('Nombres')
    appaterno = fields.Char('ApPaterno')
    apmaterno = fields.Char('ApMaterno')
    domicilio = fields.Char('Domicilio')
    telefonos = fields.Char('Telefonos')
    correo = fields.Char('Correo')
    cuotapago = fields.Float('CuotaPago')
    auditorlider = fields.Boolean('AuditorLider')
    baja = fields.Boolean('Baja')
    tipo = fields.Integer('Tipo')
    bilingue = fields.Boolean('Bilingue')
    idoficina = fields.Char('IdOficina')


class Departamentos(models.Model):
    '''
    Class: Departamentos
    '''
    _name = 'gps.departamentos'
    _description = 'gps.departamentos'
    
    # Original fields
    iddepartamento = fields.Char('IdDepartamento')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')
    orden = fields.Integer('Orden')


class GnProduct(models.Model):
    '''
    Class: GnProduct
    '''
    _name = 'gps.gnproduct'
    _description = 'gps.gnproduct'
    _rec_name = 'productdescription'
    
    # Original fields
    productkey = fields.Char('ProductKey')
    productdescription = fields.Char('ProductDescription')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')


class Clientes(models.Model):
    '''
    Class: Clientes
    '''
    _name = 'gps.clientes'
    _description = 'gps.clientes'
    _order = 'nombrecliente'
    _rec_name = 'nombrecliente'
    
    # Original fields
    clavecliente = fields.Char('ClaveCliente')
    nombrecliente = fields.Char('NombreCliente')
    domicilio = fields.Char('Domicilio')
    telefonos = fields.Char('Telefonos')
    correos = fields.Char('Correos')
    rfc = fields.Char('Rfc')
    domiciliofiscal = fields.Text('DomicilioFiscal')
    ciudad = fields.Char('Ciudad')
    cp = fields.Char('CP')
    estado = fields.Char('Estado')
    sitioweb = fields.Char('SitioWeb')
    noempleados = fields.Integer('NoEmpleados')
    idreferencia = fields.Integer('IdReferencia')
    nombrecontacto = fields.Char('NombreContacto')
    correocontacto = fields.Char('CorreoContacto')
    puestocontacto = fields.Char('PuestoContacto')
    baja = fields.Boolean('Baja')
    idcliente = fields.Char('IdCliente')
    idclientepadre = fields.Char('IdClientePadre')
    perfil = fields.Text('Perfil')
    archivoperfil = fields.Char('archivoPerfil')
    nickname = fields.Char('NickName')
    password = fields.Char('Password')
    idoficina = fields.Char('IdOficina')
    idmd5qms = fields.Float('IdMD5QMS')
    idrefprog = fields.Integer('IdRefProg')
    recommended = fields.Char('Recommended')
    idleadersales = fields.Integer('IdLeaderSales')
    idfuente = fields.Integer('IdFuente')
    
    # Extended fields
    fuente_id = fields.Many2one(comodel_name='gps.fuente', string='Source')
    archivoperfil_id = fields.Many2one(comodel_name='ir.attachment', string='Profile')
    leadersales_id = fields.Many2one(comodel_name='res.users', string='Sales Executive')
    refprog_id = fields.Many2one(comodel_name='res.users', string='Scheduling Executive')
    referencia_id = fields.Many2one(comodel_name='res.users', string='Leader Business Model')
    ubicacion_cliente_ids = fields.One2many(comodel_name='gps.ubicacionescliente', inverse_name='cliente_id', string='Locations')
    nacecode_cliente_ids = fields.One2many(comodel_name='gps.nacecodescliente', inverse_name='cliente_id', string='NACE Codes')
    contract_count = fields.Integer(compute='_get_contract_count', string='Number contracts attached');
    
    @api.model
    def create(self, vals):
        return super(Clientes, self).create(vals)
    
    def _get_contract_count(self):
        self.ensure_one()
        contracts = self.env['gps.contratos'].search([['cliente_id', '=', self.id]])
        self.contract_count = len(contracts)


class DepartamentosObjetivos(models.Model):
    '''
    Class: DepartamentosObjetivos
    '''
    _name = 'gps.departamentosobjetivos'
    _description = 'gps.departamentosobjetivos'
    
    # Original fields
    iddepartamentoobjetivo = fields.Char('IdDepartamentoObjetivo')
    iddepartamento = fields.Char('IdDepartamento')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')
    orden = fields.Integer('Orden')
    formato = fields.Char('Formato')
    acumulameses = fields.Boolean('AcumulaMeses')
    calculoinverso = fields.Boolean('CalculoInverso')


class GnService(models.Model):
    '''
    Class: GnService
    '''
    _name = 'gps.gnservice'
    _description = 'gps.gnservice'
    _rec_name = 'servicedescription'
    
    # Original fields
    servicekey = fields.Char('ServiceKey')
    servicedescription = fields.Char('ServiceDescription')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')


class Eventos(models.Model):
    '''
    Class: Eventos
    '''
    _name = 'gps.eventos'
    _description = 'gps.eventos'
    _rec_name = 'numerotrabajo'
    _order = 'fechainicio desc'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo', default='New')
    idhabilidad = fields.Integer('IdHabilidad')
    domicilio = fields.Char('Domicilio')
    fechainicio = fields.Date('FechaInicio')
    fechatermino = fields.Date('FechaTermino')
    estadoevento = fields.Selection(selection=[(1, 'Scheduled'), (2, 'Confirmed'), (3, 'Executed'), (4, 'Review'), (5, 'Committee'), (6, 'Closed')], 
        default=1, string='Event Status')
    tipoevento = fields.Integer('TipoEvento')
    introduccion = fields.Char('Introduccion')
    pago = fields.Float('Pago')
    fechaaviso = fields.Date('FechaAviso')
    comentarios = fields.Text('Comentarios')
    idrevisor = fields.Integer('IdRevisor')
    estadorevisor = fields.Integer('EstadoRevisor')
    notarevisor = fields.Text('NotaRevisor')
    idcomite = fields.Integer('IdComite')
    estadocomite = fields.Integer('EstadoComite')
    notacomite = fields.Text('NotaComite')
    idclientservice = fields.Integer('IdClientService')
    noseguimientotrans = fields.Integer('NoSeguimientoTrans')
    idcontrato = fields.Char('IdContrato')
    idcliente = fields.Char('IdCliente')
    estadorepublica = fields.Integer('EstadoRepublica')
    discapacidad = fields.Boolean('Discapacidad')
    esconferencia = fields.Boolean('EsConferencia')
    archivoplanauditoria = fields.Char('archivoPlanAuditoria')
    idubicacion = fields.Char('IdUbicacion')
    archivoreporteauditoria = fields.Char('archivoReporteAuditoria')
    idoficina = fields.Char('IdOficina')
    ciudad = fields.Char('Ciudad')
    notaauditor = fields.Text('NotaAuditor')
    estatus = fields.Integer('estatus')
    fechaenviofssc = fields.Date('FechaEnvioFSSC')
    
    # Extended fields
    estadorevisor2 = fields.Selection(selection=[('0', 'None'), ('1', 'Approved'), ('2', 'Hold'), ('3', 'Review')],
        string='Review State')
    tipoevento2 = fields.Selection(selection=[('0', 'Todos'), ('1', 'Ninguno'), ('2', 'Pre-Auditoria'), ('3', 'Etapa I'), ('4', 'Etapa II'),
          ('5', 'Seguimiento 1'), ('6', 'CARS'), ('7', 'Recertificacion'), ('8', 'Seguimiento 2'), ('9', 'Seguimiento 3'), ('10', 'Seguimiento 4'),
          ('11', 'Seguimiento 5'), ('12', 'Transferencia'), ('13', 'Recertificacion'), ('14', 'Takeover'), ('16', 'Auditoria Especial'),
          ('17', 'RR Prior to Expiration')], string='Tipo Evento')
    contrato_id = fields.Many2one(comodel_name='gps.contratos', string='Contract')
    cliente_id = fields.Many2one(comodel_name='gps.clientes', string='Client')
    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Standard')
    revisor_id = fields.Many2one(comodel_name='res.users', string='Review')
    comite_id = fields.Many2one(comodel_name='res.users', string='Salesperson')
    client_service_id = fields.Many2one(comodel_name='res.users', string='Customer Service')
    usuarios_evento_ids = fields.One2many(comodel_name='gps.usuariosevento', inverse_name='evento_id', string='Auditors')
    noconformidades_ids = fields.One2many(comodel_name='gps.noconformidades', inverse_name='evento_id', string='Non Conformances')
    noconformidades_count = fields.Integer(compute='_get_noconformidades_count', string='Number non conformances attached')
    archivos_revisor_ids = fields.One2many(comodel_name='gps.archivostracking', inverse_name='evento_id', string='Documents')
    archivo_plan_auditoria_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Plan')
    archivo_reporte_auditoria_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Report')
    archivo_hoja_resultados_id = fields.Many2one(comodel_name='ir.attachment', string='Results Sheet')
    archivo_cierre_conferencia_id = fields.Many2one(comodel_name='ir.attachment', string='Opening and Closing Meeting')
    archivo_plan_auditoria_final_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Plan')
    archivo_reporte_auditoria_final_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Report')
    archivo_reporte_cliente_id = fields.Many2one(comodel_name='ir.attachment', string='Client Report')
    eventos_facturacion_id = fields.One2many(comodel_name='gps.eventosfacturacion', inverse_name='evento_id', string='Event Billing')
    
    @api.model
    def create(self, vals):
        return super(Eventos, self).create(vals)
    
    def _get_noconformidades_count(self):
        self.ensure_one()
        non_conformances = self.env['gps.noconformidades'].search([['evento_id', '=', self.id]])
        self.noconformidades_count = len(non_conformances)


class DepartamentosObjetivosMedidas(models.Model):
    '''
    Class: DepartamentosObjetivosMedidas
    '''
    _name = 'gps.departamentosobjetivosmedidas'
    _description = 'gps.departamentosobjetivosmedidas'
    
    # Original fields
    iddepartamentoobjetivo = fields.Char('IdDepartamentoObjetivo')
    anio = fields.Integer('Anio')
    mes = fields.Integer('Mes')
    meta = fields.Float('Meta')
    real = fields.Float('Real')
    soporte = fields.Char('Soporte')


class GnModel(models.Model):
    '''
    Class: GnModel
    '''
    _name = 'gps.gnmodel'
    _description = 'gps.gnmodel'
    _rec_name = 'modelname'
    
    # Original fields
    modelkey = fields.Char('ModelKey')
    modeldescription = fields.Text('ModelDescription')
    modelname = fields.Char('ModelName')
    daysaudit = fields.Integer('DaysAudit')
    
    # Extended fields
    prosclient_id = fields.Many2one(comodel_name='gps.gnprospectclient', string='Client')
    section_ids = fields.One2many(comodel_name='gps.gnsection', inverse_name='model_id', string='Sections')
    auditor_ids = fields.One2many(comodel_name='gps.gnauditormodel', inverse_name='model_id', string='Auditors')


class GnSection(models.Model):
    '''
    Class: GnSection
    '''
    _name = 'gps.gnsection'
    _description = 'gps.gnsection'
    _rec_name = 'sectiondescription'
    
    # Original fields
    sectionkey = fields.Char('SectionKey')
    modelfk = fields.Char('ModelFk')
    numsection = fields.Integer('NumSection')
    sectiondescription = fields.Char('SectionDescription')
    maxpoints = fields.Integer('MaxPoints')
    
    # Extended fields
    model_id = fields.Many2one(comodel_name='gps.gnmodel', string='Checklist')
    question_ids = fields.One2many(comodel_name='gps.gnquestion', inverse_name='section_id', string='Questions')


class Habilidades(models.Model):
    '''
    Class: Habilidades
    '''
    _name = 'gps.habilidades'
    _description = 'gps.habilidades'
    _rec_name = 'nombre'
    
    # Original fields
    idhabilidad = fields.Integer('IdHabilidad')
    nombre = fields.Char('Nombre')
    tipo = fields.Integer('Tipo')
    descripcion = fields.Text('Descripcion')
    idpadre = fields.Integer('IdPadre')
    nohoras = fields.Integer('NoHoras')
    costopersona = fields.Float('CostoPersona')
    tipomoneda = fields.Integer('TipoMoneda')
    esseminario = fields.Boolean('EsSeminario')
    abreviacion = fields.Char('Abreviacion')
    tipocurso = fields.Char('TipoCurso')
    manual = fields.Char('Manual')


class Derechos(models.Model):
    '''
    Class: Derechos
    '''
    _name = 'gps.derechos'
    _description = 'gps.derechos'
    
    # Original fields
    idderecho = fields.Integer('IdDerecho')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')


class GnQuestion(models.Model):
    '''
    Class: GnQuestion
    '''
    _name = 'gps.gnquestion'
    _description = 'gps.gnquestion'
    
    # Original fields
    questionkey = fields.Char('QuestionKey')
    sectionfk = fields.Char('SectionFk')
    numquestion = fields.Integer('NumQuestion')
    questiondescription = fields.Text('QuestionDescription')
    isimportant = fields.Boolean('IsImportant')
    category = fields.Integer('Category')
    subsectionfk = fields.Char('SubSectionFk')
    
    # Extended fields
    section_id = fields.Many2one(comodel_name='gps.gnsection', string='Section')


class NaceCodes(models.Model):
    '''
    Class: NaceCodes
    '''
    _name = 'gps.nacecodes'
    _description = 'gps.nacecodes'
    _rec_name = 'nombre'
    
    # Original fields
    idnacecode = fields.Integer('IdNaceCode')
    nombre = fields.Char('Nombre')
    descripcion = fields.Text('Descripcion')
    idhabilidad = fields.Integer('IdHabilidad')
    baja = fields.Boolean('Baja')
    acreditadoporanab = fields.Boolean('AcreditadoPorANAB')
    claseriesgo = fields.Char('ClaseRiesgo')
    iaf = fields.Integer('IAF')
    
    # Extended fields
    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Standards')


class ProcesoGlobal(models.Model):
    '''
    Class: ProcesoGlobal
    '''
    _name = 'gps.procesoglobal'
    _description = 'gps.procesoglobal'
    
    # Original fields
    idproceso = fields.Integer('IdProceso')
    idoficina = fields.Char('IdOficina')
    nombre = fields.Char('Nombre')
    fecha = fields.Date('Fecha')


class GnDiagnostic(models.Model):
    '''
    Class: GnDiagnostic
    '''
    _name = 'gps.gndiagnostic'
    _description = 'gps.gndiagnostic'
    
    # Original fields
    diagnostickey = fields.Char('DiagnosticKey')
    sectionfk = fields.Char('SectionFk')
    questionfk = fields.Char('QuestionFk')
    email = fields.Char('Email')
    initial = fields.Char('Initial')
    points = fields.Integer('Points')


class HabilidadesUsuario(models.Model):
    '''
    Class: HabilidadesUsuario
    '''
    _name = 'gps.habilidadesusuario'
    _description = 'gps.habilidadesusuario'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    idhabilidad = fields.Integer('IdHabilidad')


class PlanAuditoria9KEtapa1(models.Model):
    '''
    Class: PlanAuditoria9KEtapa1
    '''
    _name = 'gps.planauditoria9ketapa1'
    _description = 'gps.planauditoria9ketapa1'
    
    # Original fields
    idioma = fields.Char('Idioma')
    orden = fields.Integer('Orden')
    descripcion = fields.Char('Descripcion')
    permitearchivos = fields.Boolean('PermiteArchivos')
    descripcioninformacion = fields.Char('DescripcionInformacion')


class DerechosUsuario(models.Model):
    '''
    Class: DerechosUsuario
    '''
    _name = 'gps.derechosusuario'
    _description = 'gps.derechosusuario'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    idderecho = fields.Integer('IdDerecho')
    activo = fields.Boolean('Activo')


class Concepto(models.Model):
    '''
    Class: Concepto
    '''
    _name = 'gps.concepto'
    _description = 'gps.concepto'
    
    # Original fields
    idconcepto = fields.Integer('idConcepto')
    concepto = fields.Char('Concepto')


class GnProspectClient(models.Model):
    '''
    Class: GnProspectClient
    '''
    _name = 'gps.gnprospectclient'
    _description = 'gps.gnprospectclient'
    _rec_name = 'companyname'
    _inherit = 'mail.thread'
    
    # Original fields
    prosclienkey = fields.Char('ProsClienKey')
    modelfk = fields.Char('ModelFk')
    dateprosp = fields.Date('DateProsp')
    datecliente = fields.Date('DateCliente')
    iscliente = fields.Boolean('IsCliente')
    ownerposclient = fields.Integer('OwnerPosClient')
    sourceposclient = fields.Char('SourcePosClient')
    companyname = fields.Char('CompanyName')
    recommendedby = fields.Char('RecommendedBy')
    industrialsector = fields.Char('IndustrialSector')
    website = fields.Char('WebSite')
    statecontact = fields.Char('StateContact')
    isglobalclient = fields.Boolean('IsGlobalClient')
    interestedin = fields.Char('InterestedIn')
    standar = fields.Char('Standar')
    course = fields.Char('Course')
    daysauditorcourse = fields.Float('DaysAuditorCourse')
    adress = fields.Char('Adress')
    city = fields.Char('City')
    locationstate = fields.Char('LocationState')
    country = fields.Char('Country')
    descriptionclient = fields.Text('DescriptionClient')
    clientcode = fields.Char('ClientCode')
    rfc = fields.Char('RFC')
    adresstax = fields.Text('AdressTax')
    zipcode = fields.Char('ZipCode')
    employeenumber = fields.Integer('EmployeeNumber')
    inactive = fields.Boolean('Inactive')
    profileclient = fields.Text('ProfileClient')
    nickname = fields.Char('NickName')
    password = fields.Char('Password')
    idoficce = fields.Char('IdOficce')
    idusercustomerservice = fields.Integer('IdUserCustomerService')
    iduserplanning = fields.Integer('IdUserPlanning')
    thema = fields.Char('Thema')
    lastaccess = fields.Date('LastAccess')
    
    # Extended fields
    usercustomerservice_id = fields.Many2one(comodel_name='res.users', string='Customer Service')
    userplanning_id = fields.Many2one(comodel_name='res.users', string='Planning Executive')
    supplier_count = fields.Integer(compute='_get_supplier_count', string='Number suppliers attached');
    industrialsector_id = fields.Many2one(comodel_name='gps.gnindustrialsector', string='Industrial Sector')
    
    def _get_supplier_count(self):
        for prospect in self:
            suppliers = self.env['gps.gnsupplier'].search([['prosclient_id', '=', prospect.id]])
            prospect.supplier_count = len(suppliers)


class UsuariosEvento(models.Model):
    '''
    Class: UsuariosEvento
    '''
    _name = 'gps.usuariosevento'
    _description = 'gps.usuariosevento'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    idusuario = fields.Integer('IdUsuario')
    lider = fields.Boolean('Lider')
    traductor = fields.Boolean('Traductor')
    
    # Extended fields
    evento_id = fields.Many2one(comodel_name='gps.eventos', string='Event')
    usuario_id = fields.Many2one(comodel_name='res.users', string='User')


class PlanAuditoria9KEtapa1Detalle(models.Model):
    '''
    Class: PlanAuditoria9KEtapa1Detalle
    '''
    _name = 'gps.planauditoria9ketapa1detalle'
    _description = 'gps.planauditoria9ketapa1detalle'
    
    # Original fields
    numerotrabajo = fields.Char('NumeroTrabajo')
    orden = fields.Integer('Orden')
    referencia = fields.Char('Referencia')
    comentariosetapa1 = fields.Char('ComentariosEtapa1')
    comentariosetapa2 = fields.Char('ComentariosEtapa2')
    resultado = fields.Char('Resultado')


class Registro(models.Model):
    '''
    Class: Registro
    '''
    _name = 'gps.registro'
    _description = 'gps.registro'
    
    # Original fields
    idregistro = fields.Char('IdRegistro')
    idusuario = fields.Integer('IdUsuario')
    idconcepto = fields.Integer('IdConcepto')
    fechareg = fields.Date('fechaReg')
    horas = fields.Float('horas')
    cliente = fields.Char('Cliente')
    certificacion = fields.Char('Certificacion')
    curso = fields.Char('curso')
    observacion = fields.Char('observacion')
    idpermiso = fields.Integer('IdPermiso')


class NaceCodesUsuarios(models.Model):
    '''
    Class: NaceCodesUsuarios
    '''
    _name = 'gps.nacecodesusuarios'
    _description = 'gps.nacecodesusuarios'
    
    # Original fields
    idusuario = fields.Integer('IdUsuario')
    idnacecode = fields.Integer('IdNaceCode')
    calificacion = fields.Integer('Calificacion')


class Encuestas(models.Model):
    '''
    Class: Encuestas
    '''
    _name = 'gps.encuestas'
    _description = 'gps.encuestas'
    
    # Original fields
    idd = fields.Char('Id')
    revision = fields.Char('Revision')
    tipoevento = fields.Integer('TipoEvento')
    activo = fields.Boolean('Activo')
    fechacreado = fields.Date('FechaCreado')


class NaceCodesCliente(models.Model):
    '''
    Class: NaceCodesCliente
    '''
    _name = 'gps.nacecodescliente'
    _description = 'gps.nacecodescliente'
    
    # Original fields
    idnacecode = fields.Integer('IdNaceCode')
    idcliente = fields.Char('IdCliente')
    
    # Extended fields
    cliente_id = fields.Many2one(comodel_name='gps.clientes', string='Clients')
    nacecode_id = fields.Many2one(comodel_name='gps.nacecodes', string='NACE Code')
    nacecode_nombre = fields.Char(related='nacecode_id.nombre', string='Name')
    nacecode_descripcion = fields.Text(related='nacecode_id.descripcion', string='Descripcion')
    nacecode_habilidad = fields.Many2one(related='nacecode_id.habilidad_id', comodel_name='gps.habilidades', string='Standard')


class NoConformidadesAcciones(models.Model):
    '''
    Class: NoConformidadesAcciones
    '''
    _name = 'gps.noconformidadesacciones'
    _description = 'gps.noconformidadesacciones'
    
    # Original fields
    accioneskey = fields.Char('AccionesKey')
    numerotrabajo = fields.Char('NumeroTrabajo')
    seccion = fields.Integer('Seccion')
    nombrearchivo = fields.Char('NombreArchivo')
    ocurrioerror = fields.Boolean('OcurrioError')
    descripcionerror = fields.Char('DescripcionError')
    instanteaccion = fields.Date('InstanteAccion')


class Contratos(models.Model):
    '''
    Class: Contratos
    '''
    _name = 'gps.contratos'
    _description = 'gps.contratos'
    _inherit = ['mail.thread']
    _order = 'fechacontrato desc'
    _rec_name = 'nocontrato'
    
    # Original fields
    nocontrato = fields.Char('NoContrato', default='New')
    idhabilidad = fields.Integer('IdHabilidad')
    esquema = esquema = fields.Selection(selection=[('0', 'Biannual'),('1', 'Annual'),('2', 'Mixed')], default='1', string='Esquema')
    apdiseno = fields.Boolean('ApDiseno')
    multisitio = fields.Boolean('Multisitio')
    bilingue = fields.Boolean('Bilingue')
    nivelriesgo = fields.Char('NivelRiesgo')
    duracion = fields.Selection(selection=[(1, '1 Year'), (2, '2 Year'), (3, '3 Year')], default=1, string='Duracion')
    fechacontrato = fields.Date('FechaContrato')
    notas = fields.Text('Notas')
    cancelado = fields.Boolean('Cancelado')
    transferencia = fields.Boolean('Transferencia')
    archivocontrato = fields.Char('archivoContrato')
    archivocuestionario = fields.Char('archivoCuestionario')
    archivocarta = fields.Char('archivoCarta')
    archivocotizacion = fields.Char('archivoCotizacion')
    archivotransferencia = fields.Char('archivoTransferencia')
    idcontrato = fields.Char('IdContrato')
    idcliente = fields.Char('IdCliente')
    idrevisor = fields.Integer('IdRevisor')
    estadorevisor = fields.Integer('EstadoRevisor')
    notarevisor = fields.Char('NotaRevisor')
    idventas = fields.Integer('IdVentas')
    fee01 = fields.Float('Fee01')
    fee02 = fields.Float('Fee02')
    fee03 = fields.Float('Fee03')
    ciclocontrato = fields.Integer('CicloContrato')
    monedatipo = fields.Integer('MonedaTipo')
    monedatipocambio = fields.Float('MonedaTipoCambio')
    recertificacion = fields.Boolean('Recertificacion')
    finalizado = fields.Boolean('Finalizado')
    archivocertificado = fields.Char('archivoCertificado')
    informacionavance = fields.Text('InformacionAvance')
    fechainicio = fields.Date('fechainicio')
    fechafin = fields.Date('fechafin')
    tipocertificacion = fields.Integer('tipocertificacion')
    mostrarnace = fields.Boolean('mostrarnace')
    tipoesquema = fields.Integer('tipoesquema')
    bloquearcontrato = fields.Boolean('bloquearcontrato')
    estatuscertificado = fields.Integer('EstatusCertificado')
    haccp = fields.Integer('Haccp')
    aplicaviaticos = fields.Integer('AplicaViaticos')
    idmd5qms = fields.Float('IdMd5Qms')
    observacionesviaticos = fields.Char('ObservacionesViaticos')
    reporttime = fields.Float('ReportTime')
    archivorevauditor = fields.Char('archivoRevAuditor')
    multilocalidad = fields.Boolean('Multilocalidad')
    
    # Extended fields
    monedatipo2 = fields.Selection(selection=[('0', 'Peso'), ('1', 'Dollar'), ('2', 'Euro'), ('3', 'Canadian Dollar')],
        default='0', string='Tipo Moneda')
    estadorevisor2 = fields.Selection(selection=[('0', 'Draft'), ('1', 'Approved'), ('2', 'Hold'), ('3', 'Review')],
        default='0', string='Estado Revisor')
    tipocertificacion = fields.Selection(selection=[(1, 'Initial'), (2, 'Recertification'), (3, 'Takeover')], 
        default=1, string='Tipo Certificación')
    estatuscertificado2 = fields.Selection(selection=[('0', 'Active'), ('1', 'Expired'), ('2', 'Suspended'), ('3', 'Canceled')], 
        string='Estatus Certificado')
    aplicaviaticos2 = fields.Selection(selection=[('0', 'Dont Apply'), ('1', 'Apply'), ('2', 'Special')], string='Aplica Viaticos')
    cliente_id = fields.Many2one(comodel_name='gps.clientes', string='Client')
    habilidad_id = fields.Many2one(comodel_name='gps.habilidades', string='Standard')
    revisor_id = fields.Many2one(comodel_name='res.users', string='Review')
    ventas_id = fields.Many2one(comodel_name='res.users', string='Salesperson')
    md5_qms_id = fields.Many2one(comodel_name='gps.md5qms', string='MD5QMS')
    archivo_contrato_id = fields.Many2one(comodel_name='ir.attachment', string='Contract File')
    archivo_rev_auditor_id = fields.Many2one(comodel_name='ir.attachment', string='Audit Review File')
    archivo_certificado_id = fields.Many2one(comodel_name='ir.attachment', string='Certificate File')
    ubicacion_contrato_ids = fields.One2many(comodel_name='gps.ubicacionescontrato', inverse_name='contrato_id', string='Locations')
    eventos_contrato_ids = fields.One2many(comodel_name='gps.eventoscontrato', inverse_name='contrato_id', string='Order Lines')
    event_count = fields.Integer(compute='_get_event_count', string='Number events attached');
    amount_total = fields.Float(compute='_get_amount_total', string='Total')
    vigente = fields.Boolean(compute='_get_vigente', string='Currently active')
    no_empleados = fields.Integer()
    
    # Banderas usadas para disparar acciones usando metodos 'onchange'
    flag_action_gen_scheme = fields.Boolean('Generate Scheme')
    
    @api.model
    def create(self, vals):
        vals['nocontrato'] = self._generate_nocontrato(vals)
        if 'cliente_id' in vals and vals['cliente_id']:
            cliente = self.env['gps.clientes'].browse(vals['cliente_id'])
            vals['no_empleados'] = cliente and cliente.noempleados or 0
        return super(Contratos, self).create(vals)
    
    @api.multi
    def write(self, vals):
        return super(Contratos, self).write(vals)
    
    @api.v7
    def read(self, cr, user, ids, fields=None, context=None, load='_classic_read'):
        return super(Contratos, self).read(cr, user, ids, fields, context, load)
    
    @api.v8
    def read(self, fields=None, load='_classic_read'):  # @DuplicatedSignature
        return super(Contratos, self).read(fields=fields, load=load)
    
    @api.model
    def default_get(self, fields):
        return super(Contratos, self).default_get(fields)
    
    @api.constrains('ciclocontrato')
    def _check_cycle(self):
        for r in self:
            if r.ciclocontrato <= 0:
                raise ValidationError(_('Cycle must be greater than zero.'))
            
    @api.onchange('flag_action_gen_scheme')
    def on_change_flag_action_gen_scheme(self):
        if not self.habilidad_id:
            return
    
        audit_time_ids = self.env['gps.md5qms'].search([['standard_id', '=', self.habilidad_id.id]])
        audit_time_id = audit_time_ids and audit_time_ids[0] or False
        if audit_time_id and self.id:
            audit_times_res = audit_time_id.get_audit_times(self.no_empleados)
            audit_times = []
            audit_times.append((0, 0, {'contrato_id': self.id, 'tipoevento': 3, 'dias': audit_times_res['stage1'], 'costo': 900}))
            audit_times.append((0, 0, {'contrato_id': self.id, 'tipoevento': 4, 'dias': audit_times_res['stage2'], 'costo': 900}))
            audit_times.append((0, 0, {'contrato_id': self.id, 'tipoevento': 5, 'dias': audit_times_res['annual'], 'costo': 900}))
            audit_times.append((0, 0, {'contrato_id': self.id, 'tipoevento': 8, 'dias': audit_times_res['annual'], 'costo': 900}))
            self.eventos_contrato_ids = audit_times
        
    def _get_event_count(self):
        self.ensure_one()
        contracts = self.env['gps.eventos'].search([['contrato_id', '=', self.id]])
        self.event_count = len(contracts)
            
    @api.depends('eventos_contrato_ids')
    def _get_amount_total(self):
        self.ensure_one()
        amount_total = 0;
        for evento_contrato in self.eventos_contrato_ids:
            amount_total += evento_contrato.costo
        self.amount_total = amount_total
        
    @api.depends('cancelado', 'finalizado')
    def _get_vigente(self):
        for contrato in self:
            if (contrato.finalizado or contrato.cancelado):
                contrato.vigente = False
            else:
                contrato.vigente = True
                        
    def _generate_nocontrato(self, vals):
        if 'cliente_id' in vals:
            cliente = self.env['gps.clientes'].browse(vals['cliente_id'])
            standard = self.env['gps.habilidades'].browse(vals['habilidad_id'])
            return '{}{}-{}'.format(cliente.clavecliente, standard.abreviacion, vals['ciclocontrato'])
        return vals['nocontrato']


class EncuestasPreguntas(models.Model):
    '''
    Class: EncuestasPreguntas
    '''
    _name = 'gps.encuestaspreguntas'
    _description = 'gps.encuestaspreguntas'
    
    # Original fields
    idd = fields.Char('Id')
    encuestaid = fields.Char('EncuestaId')
    idioma = fields.Char('Idioma')
    pregunta = fields.Char('Pregunta')
    orden = fields.Integer('Orden')


class IngresoCOS(models.Model):
    '''
    Class: IngresoCOS
    '''
    _name = 'gps.ingresocos'
    _description = 'gps.ingresocos'
    
    # Original fields
    ingresokey = fields.Char('IngresoKey')
    nickname = fields.Char('NickName')
    instanteingreso = fields.Date('InstanteIngreso')


class LastNC(models.Model):
    '''
    Class: LastNC
    '''
    _name = 'gps.lastnc'
    _description = 'gps.lastnc'
    
    # Original fields
    idlastnc = fields.Char('IdLastNC')
    idnoconformidad = fields.Char('IdNoConformidad')
    numerotrabajo = fields.Char('NumeroTrabajo')
    fechaapertura = fields.Date('FechaApertura')


class EncuestasRespuestas(models.Model):
    '''
    Class: EncuestasRespuestas
    '''
    _name = 'gps.encuestasrespuestas'
    _description = 'gps.encuestasrespuestas'
    
    # Original fields
    idd = fields.Char('Id')
    encuestapreguntaid = fields.Char('EncuestaPreguntaId')
    respuesta = fields.Char('Respuesta')
    valor = fields.Integer('Valor')
    orden = fields.Integer('Orden')

