from django.db import models
import datetime
from .tasks import notificacion_telegram
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.

SUBESTADO = (
        ('Maqueta', 'Maqueta'),
        ('Servicio', 'Servicio'),
        ('Regularización', 'Regularización'),
    )

AMBIENTE_SOC = (
        ('Pre-Producción', 'Pre-Producción'),
        ('Producción', 'Producción'),
    )

ENTREGABLES = (
        ('GESTIÓN DE CUENTAS', 'GESTIÓN DE CUENTAS'),
        ('PRUEBAS DE REDUNDANCIA', 'PRUEBAS DE REDUNDANCIA'),
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
        ('REVALIDACION SS', 'REVALIDACION SS'),
        ('REVALIDACION ALARMAS', 'REVALIDACION ALARMAS'),
        ('ACTUALIZACION DTS', 'ACTUALIZACION DTS'),
        ('CHECKLIST SO', 'CHECKLIST SO'),
        ('CHECKLIST BD', 'CHECKLIST BD'),
        ('Otros', 'Otros'),
    )

class Gestor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Gestor")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Gestor")
    mrn = models.CharField(max_length=100, verbose_name="MRN del Gestor")
    telefono = models.CharField(max_length=100, verbose_name="Teléfono del Gestor", default="")
    email = models.EmailField(max_length=100, verbose_name="Email del Gestor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor Inetum"
        verbose_name_plural = "Gestores Inetum"
        ordering = ('created',)

    def __str__(self):
        return f'{self.name} {self.apellido}' 

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
    telefono = models.CharField(max_length=100, verbose_name="Numero de Telefono", default="")
    email = models.EmailField(max_length=100, verbose_name="Email del Gerente")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gerente de TEMM"
        verbose_name_plural = "Gerentes de TEMM"
        ordering = ('created',)

    def __str__(self):
        return f'{self.name} {self.apellido}' 

class LiderTecnicoTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Lider")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Lider")
    telefono = models.CharField(max_length=100, verbose_name="Numero de Telefono", default="")
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
        return f'{self.name} {self.apellido}' 


class GerenciaSoporteTemm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Gerente")
    area = models.CharField(max_length=100, verbose_name="Nombre del area de soporte", default="")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Gerente")
    telefono = models.CharField(max_length=100, verbose_name="Numero de Telefono", default="")
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
    area = models.CharField(max_length=100, verbose_name="Nombre del area", default="")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Soporte")
    telefono = models.CharField(max_length=100, verbose_name="Numero de Telefono", default="")
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
        return f'{self.area}, {self.name}'


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
    ip_soc = models.GenericIPAddressField(default=" ", verbose_name="Ip del SOC", blank=True, null=True)
    ambiente = models.CharField(choices=AMBIENTE_SOC, max_length=200, verbose_name="Ambiente SOC", blank=True, null=True)
    tecnologia = models.ForeignKey(TecnologiaCatalogo, on_delete=models.CASCADE, related_name="get_tecnologia_soc",
                                verbose_name="Tecnología Soc", blank=True)


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
    #unique = True
    id_grupo = models.PositiveIntegerField(default=0, verbose_name="ID del Workflow")
    alta_workflow = models.DateField( verbose_name="Fecha de Alta WORKFLOW",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"
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
    id_proyecto = models.PositiveIntegerField(default=0, verbose_name="ID de grupo")
    name_proyecto = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    detencion = models.BooleanField(verbose_name="Detencion de proyecto", blank=True, null=True, default=False)
    fecha_detencion = models.DateField(verbose_name="Fecha de detencion", blank=True, null=True)
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
    ot = models.ManyToManyField(Ot, verbose_name="Orden de Trabajo", related_name="get_ots", blank=True)
    impacto = models.BooleanField(verbose_name="Impacto al Negocio", blank=True, null=True, default=False)
    comentarios = models.TextField(verbose_name="Comentarios generales", default="")
    comentarios_vista = models.TextField(verbose_name="Comentarios vista", default="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    cumplimiento = models.BooleanField(verbose_name="Cumplimiento para vista", blank=True, null=True, default=False)
    backlog = models.BooleanField(verbose_name="Backlog", blank=True, null=True, default=False)

    class Meta:
        verbose_name = "Gestion de Proyectos"
        verbose_name_plural = "Gestion de Proyectos"
        ordering = ('created',)

    def getEntregables(self):
        entregables =  Entregable.objects.filter(gestion_id=self.pk).order_by("created").filter(estatus=False)
        lista =[]

        for entregable in entregables:
            lista.append(entregable.name)
        return lista
    
    def get_fechasEntregado(self):
        entregables =  Entregable.objects.filter(gestion_id=self.pk).order_by("created").filter(estatus=True)
        lista =[]

        for entregable in entregables:
            if entregable.otros:
                name = f'{entregable.name}/{entregable.otros}'
            else:
                name = f'{entregable.name}'
            lista.append(name)
            x = entregable.compromiso
            lista.append(x.strftime("%d-%m-%Y"))
        return lista
    
    def get_fechasNoEntregado(self):
        entregables =  Entregable.objects.filter(gestion_id=self.pk).order_by("created").filter(estatus=False)
        lista =[]

        for entregable in entregables:
            if entregable.otros:
                name = f'{entregable.name}/{entregable.otros}'
            else:
                name = f'{entregable.name}'
            lista.append(name)
            x = entregable.compromiso
            if x:
                lista.append(x.strftime("%d-%m-%Y"))
        return lista
    
    def getFechaProxima(self):
        entregables =  Entregable.objects.filter(gestion_id=self.pk).order_by("created").filter(estatus=False)
        lista =[]

        for entregable in entregables:
            if entregable.compromiso != None:
                lista.append(entregable.compromiso)
        
        if len(lista) <= 0:
            return "N/A"
        else:
            final = sorted(lista)
            return final[0]

        # if len(lista) == 0:
        #     return "N/A"

        # if lista:
        #     results = [d for d in sorted(lista) if d > input_date]
        #     listaFinal = results[0] if results else lista[-1]
        # else:
        #     listaFinal = "N/A"

        

    def __str__(self):
        return self.name_proyecto

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Entregable(models.Model):
    name = models.CharField(choices=ENTREGABLES, max_length=200, verbose_name="Escoja el entregable")
    otros = models.CharField(verbose_name="Especificar nombre", max_length=75, blank=True, null=True, default="", help_text="Solo en caso de escoger 'Otros'")
    compromiso = models.DateField( verbose_name="Fecha Compromiso del Entregable",blank=True, null=True)
    comentario = models.CharField(max_length=100, verbose_name="Comentario", blank=True, null=True)
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, related_name="get_gestion",
                                   verbose_name="Proyecto", blank=True, null=True)
    estatus = models.BooleanField(verbose_name="Entregado", default=False) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Entregable"
        verbose_name_plural = "Entregables"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Historico(models.Model):
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, related_name="get_gestion_historico", blank=True, null=True)
    name = models.CharField(choices=ENTREGABLES, max_length=200, verbose_name="Escoja el entregable")
    compromiso = models.DateField( verbose_name="Fecha Compromiso del Entregable",blank=True, null=True)
    comentario = models.CharField(max_length=100, verbose_name="Comentario", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"
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

@receiver(pre_save, sender=Entregable)
def historico(sender,instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.compromiso != instance.compromiso:
            Historico.objects.create(gestion_id=instance.gestion.id, name=instance.name, compromiso=old_instance.compromiso,
                                 comentario=instance.comentario)
    except sender.DoesNotExist:
       Historico.objects.create(gestion_id=instance.gestion.id,name=instance.name,compromiso= instance.compromiso,comentario= instance.comentario)