from django.db import models





# Create your models here.
class Kpis_Fijos(models.Model):
    case_id = models.CharField(max_length=1000, verbose_name="Case ID+")
    category = models.CharField(max_length=1000, verbose_name="Category*")
    source = models.CharField(max_length=1000, verbose_name="Source*")
    status = models.CharField(max_length=1000, verbose_name="Status")
    closure_code = models.CharField(max_length=1000, verbose_name="Closure Code")
    case_type = models.CharField(max_length=1000, verbose_name="Case Type*")
    grupo = models.CharField(max_length=1000, verbose_name="Group+")
    sumary = models.CharField(max_length=1000, verbose_name="Sumary")
    arrival_time = models.DateTimeField( verbose_name="Arrival Time",blank=True, null=True)
    fecha_inicio_actual = models.DateTimeField(verbose_name="Fecha Inicio Actual(536871085)", blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="Create Date", blank=True, null=True)
    resolved = models.DateTimeField(verbose_name="Resolved", blank=True, null=True)
    closed_time = models.DateTimeField(verbose_name="Closed.Time", blank=True, null=True)
    pending_time = models.DateTimeField(verbose_name="Pending Time", blank=True, null=True)
    working_time = models.DateTimeField(verbose_name="Work in Progress Time", blank=True, null=True)
    assign_time = models.DateTimeField(verbose_name="Assigned Time", blank=True, null=True)
    tipo = models.CharField(max_length=1000, verbose_name="Tipo", blank=True, null=True)
    elemento = models.CharField(max_length=1000, verbose_name="Elemento", blank=True, null=True)
    ticket_suministrador = models.CharField(max_length=1000, verbose_name="Ticket Suministrador", blank=True, null=True)
    suministrador = models.CharField(max_length=1000, verbose_name="Suministrador", blank=True, null=True)
    work_log = models.TextField(verbose_name="Work log", blank=True, null=True)
    tiempo_sla = models.DurationField(verbose_name="Tiempo SLA", blank=True, null=True)
    paro_reloj = models.CharField(max_length=1000, verbose_name="Paro de Reloj", blank=True, null=True)
    tiempo_real_sin_paros = models.CharField(max_length=1000, verbose_name="Paro de Reloj", blank=True, null=True)
    sla = models.CharField(max_length=1000, verbose_name="SLA", blank=True, null=True)
    tiempo_apertura = models.DurationField(verbose_name="Tiempo Apertura", blank=True, null=True)
    sla_apertura = models.CharField(max_length=1000, verbose_name="SLA Apertura", blank=True, null=True)
    tiempo_diagnostico = models.DurationField(verbose_name="Tiempo Diagnóstico", blank=True, null=True)
    sla_diagnostico = models.CharField(max_length=1000, verbose_name="SLA Diagnóstico", blank=True, null=True)

    region = models.CharField(max_length=1000, verbose_name="Region", blank=True, null=True)
    estado = models.CharField(max_length=1000, verbose_name="Estado", blank=True, null=True)
    localidad = models.CharField(max_length=1000, verbose_name="Localidad", blank=True, null=True)
    cartera = models.CharField(max_length=1000, verbose_name="Tipo de Cartera", blank=True, null=True)
    holding = models.CharField(max_length=1000, verbose_name="Holding", blank=True, null=True)
    otro_cliente = models.CharField(max_length=1000, verbose_name="Otro Cliente", blank=True, null=True)
    nombre_cliente = models.CharField(max_length=1000, verbose_name="Nombre del Cliente", blank=True, null=True)
    sucursal = models.CharField(max_length=1000, verbose_name="Sucursal", blank=True, null=True)
    otra_sucursal = models.CharField(max_length=1000, verbose_name="Otra Sucursal", blank=True, null=True)
    folio_escalacion = models.CharField(max_length=1000, verbose_name="Folio Escalación", blank=True, null=True)
    id_gics = models.CharField(max_length=1000, verbose_name="Id Gics", blank=True, null=True)
    imputable = models.CharField(max_length=1000, verbose_name="Imputable", blank=True, null=True)
    id_proveedor = models.CharField(max_length=1000, verbose_name="Identificador del Circuito Proveedor", blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=1000, verbose_name="Nombre del Proveedor", blank=True, null=True)
    numero_proveedor = models.CharField(max_length=1000, verbose_name="Numero de TT Proveedor", blank=True, null=True)

    inicio_alarma = models.DateTimeField(verbose_name="Inicio de Alarma", blank=True, null=True)
    hora_apertura_proveedor = models.DateTimeField(verbose_name="Hora apertura reporte con Proveedor", blank=True, null=True)
    hora_cierre_proveedor = models.DateTimeField(verbose_name="Hora cierre reporte con Proveedor", blank=True, null=True)
    tiempo_real_afectacion = models.DurationField(verbose_name="Tiempo Real de Afectación", blank=True, null=True)

    tipo_reporte = models.CharField(max_length=1000, verbose_name="Tipo de Reporte", blank=True, null=True)
    red1 = models.CharField(max_length=1000, verbose_name="Red1", blank=True, null=True)
    causa1 = models.CharField(max_length=1000, verbose_name="Causa1", blank=True, null=True)
    subcausa = models.CharField(max_length=1000, verbose_name="Subcausa", blank=True, null=True)
    causafalla = models.CharField(max_length=1000, verbose_name="Causa Falla", blank=True, null=True)
    solucion1 = models.CharField(max_length=1000, verbose_name="Solucion1", blank=True, null=True)
    detalle_falla = models.CharField(max_length=1000, verbose_name="Detalle Falla", blank=True, null=True)
    area_resolutora = models.CharField(max_length=1000, verbose_name="Area Resolutora", blank=True, null=True)
    con_afectacion = models.CharField(max_length=1000, verbose_name="Con Afectación", blank=True, null=True)
    tipo_afectacion = models.CharField(max_length=1000, verbose_name="Tipo de Afectación", blank=True, null=True)
    tipo_enlace_afectado = models.CharField(max_length=1000, verbose_name="Tipo de Enlace Afectado", blank=True, null=True)
    id_nodo_temm = models.CharField(max_length=1000, verbose_name="Id nodo Temm", blank=True, null=True)
    nombre_nodo_temm = models.CharField(max_length=1000, verbose_name="Nombre nodo Temm", blank=True, null=True)
    tecnologia = models.CharField(max_length=1000, verbose_name="Tecnología", blank=True, null=True)
    marca = models.CharField(max_length=1000, verbose_name="Marca", blank=True,
                                            null=True)
    modelo = models.CharField(max_length=1000, verbose_name="Modelo", blank=True, null=True)
    pieza_danada = models.CharField(max_length=1000, verbose_name="Pieza Dañada", blank=True, null=True)

    causa_retraso = models.CharField(max_length=1000, verbose_name="Causa del Retraso", blank=True, null=True)
    tt_proactivo = models.CharField(max_length=1000, verbose_name="TT Proactivo", blank=True, null=True)

    nombre_cierre = models.CharField(max_length=1000, verbose_name="Nombre de Quien Cierra", blank=True, null=True)
    version_tabla = models.CharField(max_length=1000, verbose_name="Version tabla de cierre", blank=True, null=True)


    fecha_cierre = models.CharField(max_length=1000, verbose_name="Fecha de Cierre ", blank=True, null=True)
    mes = models.CharField(max_length=1000, verbose_name="Mes", blank=True,
                                            null=True)
    comentarios_fsla = models.CharField(max_length=1000, verbose_name="Comentarios FSLA", blank=True, null=True)
    numero_masiva = models.CharField(max_length=1000, verbose_name="N° Masiva", blank=True, null=True)

    causa_fsla = models.CharField(max_length=1000, verbose_name="Causa FSLA", blank=True, null=True)
    semana = models.IntegerField(verbose_name="Semana", blank=True, null=True)
    comentarios_calidad = models.CharField(max_length=1000, verbose_name="Comentarios Calidad", blank=True, null=True)
    comentarios_operacion = models.CharField(max_length=1000, verbose_name="Comentarios Operación", blank=True, null=True)
    top = models.CharField(max_length=1000, verbose_name="Top", blank=True, null=True)
    causa_final = models.CharField(max_length=1000, verbose_name="Causa Final", blank=True, null=True)
    contar_sla = models.CharField(max_length=1000, verbose_name="Contar SLA", blank=True, null=True)
    zona = models.CharField(max_length=1000, verbose_name="Zona", blank=True, null=True)
    rango = models.CharField(max_length=1000, verbose_name="Rangos", blank=True, null=True)
    masiva = models.CharField(max_length=1000, verbose_name="Masiva", blank=True, null=True)
    fsla_semanal = models.CharField(max_length=1000, verbose_name="FSLA Semanal", blank=True, null=True)
    sin_nombre = models.DurationField(verbose_name="Sin Nombre", blank=True, null=True)

    comentarios_fsla_apertura = models.CharField(max_length=1000, verbose_name="Comentarios Fsla Apertura", blank=True, null=True)
    sla_5horas = models.CharField(max_length=1000, verbose_name="SLA 5 horas", blank=True, null=True)
    sla_24horas = models.CharField(max_length=1000, verbose_name="SLA 24 horas", blank=True, null=True)
    sla_48horas = models.CharField(max_length=1000, verbose_name="SLA 48 horas", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Asistencia Fijo"
        verbose_name_plural = "Volumetria Asistencia Fijo"
        ordering = ('created',)

    def __str__(self):
        return self.case_id


class General_Kpis_Fijos(models.Model):
    fecha = models.DateField(verbose_name="Seleccione el dia", blank=True,
                                                 null=True)
    mes = models.CharField(max_length=1000, verbose_name="Mes", blank=True, null=True)
    semana = models.IntegerField(verbose_name="Semana", blank=True, null=True)
    ri = models.IntegerField(default=0, verbose_name="Cantidad de Ri", blank=True, null=True)
    correos = models.IntegerField(default=0, verbose_name="Correos", blank=True, null=True)
    chat = models.IntegerField(default=0, verbose_name="Chat", blank=True, null=True)
    disparos_falsos = models.IntegerField(default=0, verbose_name="Disparos en Falso", blank=True, null=True)


    class Meta:
        verbose_name = "General  Fijo"
        verbose_name_plural = "Generales Fijo"
        ordering = ('fecha',)

    def __str__(self):
        return str(self.fecha)





# Create your models here.
class Kpis_movil(models.Model):
    case_id = models.CharField(max_length=1000, verbose_name="Case ID+")
    category = models.CharField(max_length=1000, verbose_name="Category*")
    status = models.CharField(max_length=1000, verbose_name="Status")
    closure_code = models.CharField(max_length=1000, verbose_name="Closure Code")
    case_type = models.CharField(max_length=1000, verbose_name="Case Type*")
    grupo = models.CharField(max_length=1000, verbose_name="Group+")
    sumary = models.CharField(max_length=1000, verbose_name="Sumary")
    arrival_time = models.DateTimeField( verbose_name="Arrival Time",blank=True, null=True)
    fecha_inicio_actual = models.DateTimeField(verbose_name="Fecha Inicio Actual(536871085)", blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="Create Date", blank=True, null=True)
    resolved = models.DateTimeField(verbose_name="Resolved", blank=True, null=True)
    closed_time = models.DateTimeField(verbose_name="Closed.Time", blank=True, null=True)
    pending_time = models.DateTimeField(verbose_name="Pending Time", blank=True, null=True)
    working_time = models.DateTimeField(verbose_name="Work in Progress Time", blank=True, null=True)
    tipo = models.CharField(max_length=1000, verbose_name="Tipo", blank=True, null=True)
    elemento = models.CharField(max_length=1000, verbose_name="Elemento", blank=True, null=True)
    login = models.CharField(max_length=1000, verbose_name="Login", blank=True, null=True)

    work_log = models.TextField(verbose_name="Work log", blank=True, null=True)
    tiempo_sla = models.DurationField(verbose_name="Tiempo SLA", blank=True, null=True)
    paro_reloj = models.CharField(max_length=1000, verbose_name="Paro de Reloj", blank=True, null=True)
    tiempo_real_sin_paros = models.CharField(max_length=1000, verbose_name="Paro de Reloj", blank=True, null=True)
    sla = models.CharField(max_length=1000, verbose_name="SLA", blank=True, null=True)
    inicio_reporte = models.DateTimeField(verbose_name="Hora de Reporte", blank=True, null=True)

    tiempo_apertura = models.DurationField(verbose_name="Tiempo Apertura", blank=True, null=True)
    sla_apertura = models.CharField(max_length=1000, verbose_name="SLA Apertura", blank=True, null=True)
    tiempo_diagnostico = models.DurationField(verbose_name="Tiempo Diagnóstico", blank=True, null=True)
    sla_diagnostico = models.CharField(max_length=1000, verbose_name="SLA Diagnóstico", blank=True, null=True)

    tipo_servicio = models.CharField(max_length=1000, verbose_name="Tipo de Servicio", blank=True, null=True)
    servicio_afectado = models.CharField(max_length=1000, verbose_name="Servicio Afectado", blank=True, null=True)


    region = models.CharField(max_length=1000, verbose_name="Region", blank=True, null=True)
    estado = models.CharField(max_length=1000, verbose_name="Estado", blank=True, null=True)
    localidad = models.CharField(max_length=1000, verbose_name="Localidad", blank=True, null=True)
    cartera = models.CharField(max_length=1000, verbose_name="Tipo de Cartera", blank=True, null=True)
    holding = models.CharField(max_length=1000, verbose_name="Holding", blank=True, null=True)

    sucursal = models.CharField(max_length=1000, verbose_name="Sucursal", blank=True, null=True)
    origen_reporte = models.CharField(max_length=1000, verbose_name="Origen del Reportel", blank=True, null=True)

    escalado = models.CharField(max_length=1000, verbose_name="Escalado Con", blank=True, null=True)
    folio_escalacion = models.CharField(max_length=1000, verbose_name="Folio Escalación", blank=True, null=True)

    imputable = models.CharField(max_length=1000, verbose_name="Imputable", blank=True, null=True)
    id_proveedor = models.CharField(max_length=1000, verbose_name="Identificador del Circuito Proveedor", blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=1000, verbose_name="Nombre del Proveedor", blank=True, null=True)
    numero_proveedor = models.CharField(max_length=1000, verbose_name="Numero de TT Proveedor", blank=True, null=True)

    necesita_visita = models.CharField(max_length=1000, verbose_name="Se necesito Visita", blank=True, null=True)
    proveedor_tiempo = models.CharField(max_length=1000, verbose_name="El proveedor llego a tiempo", blank=True, null=True)
    causa_retraso_proveedor = models.CharField(max_length=1000, verbose_name="Causa retraso del proveedor", blank=True, null=True)

    hora_apertura_proveedor = models.DateTimeField(verbose_name="Hora apertura reporte con Proveedor", blank=True, null=True)
    hora_cierre_proveedor = models.DateTimeField(verbose_name="Hora cierre reporte con Proveedor", blank=True, null=True)
    tiempo_real_afectacion = models.DurationField(verbose_name="Tiempo Real de Afectación", blank=True, null=True)

    falla_real = models.CharField(max_length=1000, verbose_name="Falla Real", blank=True, null=True)
    tipo_reporte = models.CharField(max_length=1000, verbose_name="Tipo de reporte", blank=True, null=True)
    con_afectacion = models.CharField(max_length=1000, verbose_name="Con Afectación", blank=True, null=True)
    tipo_afectacion = models.CharField(max_length=1000, verbose_name="Tipo de Afectación", blank=True, null=True)
    nivel_afectacion = models.CharField(max_length=1000, verbose_name="Nivel de Afectación", blank=True, null=True)
    cantidad_dns = models.CharField(max_length=1000, verbose_name="Cantidad de Dns", blank=True, null=True)

    parque_total_dns = models.CharField(max_length=1000, verbose_name="Parque total Dns", blank=True, null=True)

    causafalla = models.CharField(max_length=1000, verbose_name="Causa Falla", blank=True, null=True)
    area = models.CharField(max_length=1000, verbose_name="Area", blank=True, null=True)


    solucion_falla = models.CharField(max_length=1000, verbose_name="Solución de la Falla", blank=True, null=True)
    causa_retraso = models.CharField(max_length=1000, verbose_name="Causa del Retraso", blank=True, null=True)

    tt_contable = models.CharField(max_length=1000, verbose_name="TT Contable", blank=True, null=True)
    cuenta_mt = models.CharField(max_length=1000, verbose_name="Cuenta con MT", blank=True, null=True)
    mt_actualizada = models.CharField(max_length=1000, verbose_name="Esta actualizada la MT", blank=True, null=True)

    correo_apertura = models.CharField(max_length=1000, verbose_name="Se envio Correo Apertura", blank=True, null=True)
    correo_cierre = models.CharField(max_length=1000, verbose_name="Se envio correo de cierre", blank=True, null=True)

    nombre_atiende = models.CharField(max_length=1000, verbose_name="Nombre de Quien Atiende", blank=True, null=True)
    nombre_cierre = models.CharField(max_length=1000, verbose_name="Nombre de Quien Cierra", blank=True, null=True)

    cliente_reporte = models.CharField(max_length=1000, verbose_name="Cliente que reporto el Servicio", blank=True, null=True)
    contacto_cliente = models.CharField(max_length=1000, verbose_name="Contacto del Cliente que reporto el servicio", blank=True, null=True)


    version = models.CharField(max_length=1000, verbose_name="Version", blank=True, null=True)
    categoria  = models.CharField(max_length=1000, verbose_name="Categoria", blank=True, null=True)


    fecha_cierre = models.CharField(max_length=1000, verbose_name="Fecha de Cierre ", blank=True, null=True)
    semana = models.IntegerField( verbose_name="Semana", blank=True, null=True)
    mes = models.CharField(max_length=1000, verbose_name="Mes", blank=True,
                                            null=True)

    comentarios_calidad = models.CharField(max_length=1000, verbose_name="Comentarios Calidad", blank=True, null=True)
    comentarios_operacion = models.CharField(max_length=1000, verbose_name="Comentarios Operación", blank=True,
                                             null=True)
    frecuencia = models.CharField(max_length=1000, verbose_name="Frecuencia", blank=True,
                                             null=True)
    caso_critico = models.CharField(max_length=1000, verbose_name="Caso Critico", blank=True,
                                             null=True)

    comentarios_fsla = models.CharField(max_length=1000, verbose_name="Comentarios FSLA", blank=True, null=True)

    rengo_m2m = models.CharField(max_length=1000, verbose_name="Rango M2M", blank=True, null=True)

    comentarios_fsla_kpis = models.CharField(max_length=1000, verbose_name="Comentarios FSLA KPIS", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Asistencia Móvil"
        verbose_name_plural = "Volumetria Asistencia Móvil"
        ordering = ('created',)

    def __str__(self):
        return self.case_id


class General_Kpis_movil(models.Model):
    fecha = models.DateField(verbose_name="Seleccione el dia", blank=True,
                                                 null=True)
    mes = models.CharField(max_length=1000, verbose_name="Mes", blank=True, null=True)
    semana = models.IntegerField(verbose_name="Semana", blank=True, null=True)
    ri = models.IntegerField(default=0, verbose_name="Cantidad de Ri", blank=True, null=True)
    correos = models.IntegerField(default=0, verbose_name="Correos", blank=True, null=True)
    chat = models.IntegerField(default=0, verbose_name="Chat", blank=True, null=True)
    disparos_falsos = models.IntegerField(default=0, verbose_name="Disparos en Falso", blank=True, null=True)


    class Meta:
        verbose_name = "General  Móvil"
        verbose_name_plural = "Generales Movil"
        ordering = ('fecha',)

    def __str__(self):
        return str(self.fecha)




class Kpis_GRTC(models.Model):
    mes_nombre = models.CharField(max_length=1000, verbose_name="MES", blank=True, null=True)
    estatus_guio = models.CharField(max_length=1000, verbose_name="ESTATUS GUIO", blank=True, null=True)
    folio = models.CharField(max_length=1000, verbose_name="Folio", blank=True, null=True)
    proveedor = models.CharField(max_length=1000, verbose_name="Proveedor", blank=True, null=True)
    tt_proveedor = models.CharField(max_length=1000, verbose_name="TT Proveedor", blank=True, null=True)
    cliente = models.CharField(max_length=1000, verbose_name="Cliente", blank=True, null=True)
    tt_cliente = models.CharField(max_length=1000, verbose_name="TT Cliente", blank=True, null=True)
    imputable = models.CharField(max_length=1000, verbose_name="Imputable", blank=True, null=True)
    fecha_inicio_cliente = models.DateTimeField(verbose_name="Fecha Inicio Cliente", blank=True, null=True)
    fecha_reporte_cliente = models.DateTimeField(verbose_name="Fecha Reporte Cliente", blank=True, null=True)
    fecha_reestablece_cliente = models.DateTimeField(verbose_name="Fecha Reestablece Cliente", blank=True, null=True)
    tiempo_afectacion_cliente = models.DurationField(verbose_name="Tiempo Afectacion Cliente", blank=True, null=True)
    tiempo_afectacion_cliente_desde_reporte = models.DurationField(verbose_name="Tiempo Afectacion Cliente Desde Reporte", blank=True, null=True)
    inicio_paro_reloj = models.DateTimeField(verbose_name="Inicio Paro de Reloj", blank=True, null=True)
    fin_paro_reloj = models.DateTimeField(verbose_name="Fin Paro de Reloj", blank=True, null=True)
    total_paro_reloj = models.DurationField(verbose_name="Total Paro Reloj", blank=True, null=True)
    justificacion_paro_reloj = models.CharField(max_length=1000, verbose_name="Justificación Paro Reloj", blank=True, null=True)



    segmento_proveedor = models.CharField(max_length=1000, verbose_name="Segmento Proveedor")
    segmento_cliente = models.CharField(max_length=1000, verbose_name="Segmento Cliente")
    ciudad = models.CharField(max_length=1000, verbose_name="Ciudad")
    id_cliente = models.CharField(max_length=1000, verbose_name="Id Cliente")
    id_unico =models.CharField(max_length=1000, verbose_name="Id Unico")

    sintoma = models.CharField(max_length=1000, verbose_name="Sintoma")
    causa = models.CharField(max_length=1000, verbose_name="Causa")
    subcausa = models.CharField(max_length=1000, verbose_name="SubCausa")

    coordenada = models.CharField(max_length=1000, verbose_name="Coordenada")
    solucion = models.CharField(max_length=1000, verbose_name="Solución")
    actividad_pendiente = models.CharField(max_length=1000, verbose_name="SubCausa")

    ot_que_provoca_afectacion = models.CharField(max_length=1000, verbose_name="Ot que Afectó Servicio")
    motivo_fuera_sla = models.CharField(max_length=1000, verbose_name="Motivo del Fsla")
    sla = models.CharField(max_length=1000, verbose_name="SLA")


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "GRTC"
        verbose_name_plural = "Volumetria GRTC"
        ordering = ('created',)

    def __str__(self):
        return self.folio



