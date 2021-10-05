from django.db import models
from .tasks import notificacion_telegram
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.

SUBESTADO = (
        ('Maqueta', 'Maqueta'),
        ('Servicio', 'Servicio'),

    )

AMBIENTE_SOC = (
        ('Pre-Producción', 'Pre-Producción'),
        ('Producción', 'Producción'),

    )

ENTREGABLES = (
        ('KO', 'KO'),
        ('COMITÉ ARQ.', 'COMITÉ ARQ.'),
        ('PLAN PROYECTO', 'PLAN PROYECTO'),
        ('MINUTA KO', 'MINUTA KO'),
        ('SS', 'SS'),
        ('ALTA EN GESTORES', 'ALTA EN GESTORES'),
        ('RESPALDOS', 'RESPALDOS'),
        ('ESTADÍSTICAS', 'ESTADÍSTICAS'),
        ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'),
        ('MT', 'MT'),
        ('ATP', 'ATP'),
        ('MO', 'MO'),
        ('SLA', 'SLA'),
        ('TOPOLOGÍA', 'TOPOLOGÍA'),
        ('CAPACITACIÓN', 'CAPACITACIÓN'),
        ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'),
        ('CERTIFICADO SSL', 'CERTIFICADO SSL'),
        ('MANUALES', 'MANUALES'),
        ('RUTINAS O&M', 'RUTINAS O&M'),
        ('RM', 'RM'),
        ('DTS', 'DTS'),
        ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'),
        ('OT FORMATO ABC', 'OT FORMATO ABC'),
        ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'),
        ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'),
        ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'),
        ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'),
        ('AE', 'AE'),
        ('AA', 'AA'),

    )

class Gestor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Gestor")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Gestor")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Gestor")
    email = models.EmailField(max_length=100, verbose_name="Email del Gestor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor Inetum"
        verbose_name_plural = "Gestores Inetum"
        ordering = ('created',)

    def __str__(self):
        return self.name

class TipoProyecto(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tipo de Proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tipo de Proyecto"
        verbose_name_plural = "Tipos de Proyectos"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Estatus(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Estatus")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"
        ordering = ('created',)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Area de Ingeniería")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Area de Ingeniería"
        verbose_name_plural = "Areas de Ingenierías"
        ordering = ('created',)

    def __str__(self):
        return self.name


class GerenciaTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Gerente")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Gerente")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Gerente")
    email = models.EmailField(max_length=100, verbose_name="Email del Gerente")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gerente de TEMM"
        verbose_name_plural = "Gerentes de TEMM"
        ordering = ('created',)

    def __str__(self):
        return self.name

class LiderTecnicoTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Lider")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Lider")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Lider")
    email = models.EmailField(max_length=100, verbose_name="Email del Lider")
    gerente = models.ForeignKey(GerenciaTemm, on_delete=models.CASCADE, related_name="get_gerente",
                                     verbose_name="Gerente del Proyecto")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Lider Técnico de TEMM"
        verbose_name_plural = "Lideres Técnicos de TEMM"
        ordering = ('created',)

    def __str__(self):
        return self.name


class GerenciaSoporteTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Gerente")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Gerente")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Gerente")
    email = models.EmailField(max_length=100, verbose_name="Email del Gerente")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gerente Soporte de TEMM"
        verbose_name_plural = "Gerentes Soportes de TEMM"
        ordering = ('created',)

    def __str__(self):
        return self.name

class SoporteTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Sorpote")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Soporte")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Soporte")
    email = models.EmailField(max_length=100, verbose_name="Email del Soporte")
    gerente = models.ForeignKey(GerenciaSoporteTemm, on_delete=models.CASCADE, related_name="get_gerente",
                                     verbose_name="Gerente del Proyecto")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Soporte de TEMM"
        verbose_name_plural = "Soportes de TEMM"
        ordering = ('created',)

    def __str__(self):
        return self.name


class TecnologiaCatalogo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de Tecnología")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Catalogo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hostname")
    id_soc = models.PositiveIntegerField(default=0, verbose_name="ID del SOC")
    elemento_soc = models.CharField(max_length=100, verbose_name="Elemento")
    ip_soc = models.GenericIPAddressField(default=0, verbose_name="Ip del SOC")
    ambiente = models.CharField(choices=AMBIENTE_SOC, max_length=200, verbose_name="Ambiente SOC", blank=True, null=True)
    tecnologia = models.ForeignKey(TecnologiaCatalogo, on_delete=models.CASCADE, related_name="get_tecnologia_soc",
                                verbose_name="Tecnología Soc")


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Catálogo"
        verbose_name_plural = "Catálogos"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Grupo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Elemento")
    elemento_soc = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name="get_grupo",
                                     verbose_name="Elemento",blank=True, null=True)
    id_grupo = models.PositiveIntegerField(default=0, verbose_name="ID del Grupo")
    alta_workflow = models.DateField( verbose_name="Fecha de Alta WORKFLOW",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ('created',)

    def __str__(self):
        return self.name


class Ot(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titulo de la Ot")
    numero = models.PositiveIntegerField(default=0, verbose_name="Numero de la OT")
    elemento_soc = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name="get_ot",
                                     verbose_name="Elemento")
    ejecucion = models.DateField( verbose_name="Fecha de Ejecución de la OT",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Orden de Trabajo"
        verbose_name_plural = "Ordenes de Trabajos"
        ordering = ('created',)

    def __str__(self):
        return self.name




class Gestion(models.Model):
    id_proyecto = models.PositiveIntegerField(default=0, verbose_name="ID del proyecto")
    name_proyecto = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    tipoProyecto = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE, related_name="get_tipo",
                                verbose_name="Tipo de Proyecto")
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, related_name="get_estatus",
                                verbose_name="Estatus")
    sub_estado = models.CharField(choices=SUBESTADO, max_length=200, verbose_name="Sub-Estado", blank=True, null=True)
    liberado = models.BooleanField(verbose_name="Liberado por Temm", blank=True, null=True, default=False)
    produccion = models.BooleanField(verbose_name="Puesto en Produccion", blank=True, null=True, default=False)
    gestor = models.ForeignKey(Gestor, on_delete=models.CASCADE, related_name="get_gestor",
                                verbose_name="Gestor")
    grupo = models.ManyToManyField(Grupo, verbose_name="Grupos", related_name="get_elementos")
    kick_off = models.DateField(verbose_name="Fecha Kick Off", blank=True, null=True)
    planificada = models.DateField(verbose_name="Fecha Planificada", blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="get_area",
                               verbose_name="Area de Ingeniería")
    lider = models.ForeignKey(LiderTecnicoTemm, on_delete=models.CASCADE, related_name="get_lider",
                             verbose_name="Lider Técnico")
    soporte = models.ForeignKey(SoporteTemm, on_delete=models.CASCADE, related_name="get_soporte",
                              verbose_name="Soporte Técnico")
    pmo = models.CharField(max_length=100, verbose_name="Nombre del PMO")
    catalogo = models.ManyToManyField(Catalogo, verbose_name="Catalogo", related_name="get_catalogo")
    ot = models.ManyToManyField(Ot, verbose_name="Orden de Trabajo", related_name="get_ots")
    impacto = models.BooleanField(verbose_name="Impacto al Negocio", blank=True, null=True, default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestión de Proyecto"
        verbose_name_plural = "Gestión de Proyectos"
        ordering = ('created',)

    def __str__(self):
        return self.name_proyecto

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Entregable(models.Model):
    name = models.CharField(choices=ENTREGABLES, max_length=200, verbose_name="Escoja el entregable")
    compromiso = models.DateField( verbose_name="Fecha Compromiso del Entregable",blank=True, null=True)
    comentario = models.CharField(max_length=100, verbose_name="Comentario", blank=True, null=True)
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, related_name="get_gestion",
                                   verbose_name="Proyecto", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
        ordering = ('created',)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Gestion)
def validador(sender,instance, **kwargs):
    prueba = instance
    print(prueba)
    try:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.estatus != instance.estatus:
            notificacion_telegram(instance.id_proyecto,instance.name_proyecto,str(old_instance.estatus).upper(), str(instance.estatus).upper())
            print(old_instance.name_proyecto, instance.name_proyecto)
    except sender.DoesNotExist:
        pass