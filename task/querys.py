from task import chat_bot
from problema.models import Entregable
from problema.models import Gestion as GestionProblema
from cambio_gics.models import Dalia, Notificacion_red, Notificacion_ti
from django.utils import  timezone
import datetime
import pandas as pd
from datetime import  timedelta

def get_data_problema():
    entregables = Entregable.objects.filter(estatus=False)
    now = datetime.date.today()
    for x in entregables:
        if x.compromiso is not None:
            diferencia = x.compromiso - now
            delta = pd.date_range(start=now, end =x.compromiso, freq='B')
            if len(delta)==4 and diferencia.days >0:
	            chat_id = -672204811
	            texto = """
	               \U00002757 Estimado Gesto(a)r {}!\nLa presente es para indicarle que el entregable \U0000066D\U0000066D{}\U0000066D\U0000066D del proyecto \U0000066D\U0000066D{}\U0000066D\U0000066D , tiene 3 dias para vencerse su fecha \nLa fecha compromiso es {}"\n
	               """
	            texto2 = texto.format(x.gestion.gestor.name, x.name, x.gestion.name_proyecto, x.compromiso)
	            chat_bot.telegram_api(texto2, chat_id)

            elif len(delta) == 9 and diferencia.days > 0:
	            chat_id = -672204811
	            texto = """
	                      \U00002757 Estimado Gesto(a)r {}!\nLa presente es para indicarle que el entregable \U0000066D\U0000066D{}\U0000066D\U0000066D del proyecto \U0000066D\U0000066D{}\U0000066D\U0000066D , tiene 8 dias para vencerse su fecha \nLa fecha compromiso es {}"\n
	                      """
	            texto2 = texto.format(x.gestion.gestor.name, x.name, x.gestion.name_proyecto, x.compromiso)
	            chat_bot.telegram_api(texto2, chat_id)

            elif len(delta) == 15 and diferencia.days > 0:
	            chat_id = -672204811
	            texto = """
	                      \U00002757 Estimado Gesto(a)r {}!\nLa presente es para indicarle que el entregable \U0000066D\U0000066D{}\U0000066D\U0000066D del proyecto \U0000066D\U0000066D{}\U0000066D\U0000066D , tiene 14 dias para vencerse su fecha \nLa fecha compromiso es {}"\n
	                      """
	            texto2 = texto.format(x.gestion.gestor.name, x.name, x.gestion.name_proyecto, x.compromiso)
	            chat_bot.telegram_api(texto2, chat_id)


def get_migraciones_dalia():
    now = datetime.date.today()
    migraciones = Dalia.objects.filter(fecha=now)
    print(len(migraciones))
    print(migraciones)
    chat_id = -1001322382371
    if len(migraciones) != 0:
        texto = 'Buenos días estimados, les comparto las actividades programadas para el día de hoy: {}\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)
        for x in migraciones:
            if x.fecha == now:
                texto5 = """          
                \U00002757 Cliente TEMM: {} {}\n
                Actividad: Migración Dalia\n
                OT: {}\n
                Fecha: {}\n
                Hora: {}\n
                Ticket Teyte: {}\n
                Asignación Teyte: {}\n
                """
                texto3 = texto5.format(x.name, x.sucursal, x.om, x.fecha, x.horario, x.numero, x.idcs)
                chat_bot.telegram_api(texto3, chat_id)
    else:
        texto = 'Buenos días estimados, para el dia de hoy {} no se cuenta con actividades de migraciones.\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)

###############################################################

def notificaciones(periodo, dias):
    now = datetime.date.today()
    delta = pd.date_range(start=now, periods=periodo, freq='B')
    fin = delta[-1]
    proyectos = GestionProblema.objects.filter(get_gestion__estatus=False, get_gestion__compromiso=fin)

    lista = []
    for x in proyectos:
        lista.append(x.id)

    id_unicos = list(dict.fromkeys(lista))

    for x in id_unicos:
        lista_nombre = []
        lista_entregables = []
        proyecto = GestionProblema.objects.get(pk=x)
        nombre = proyecto.name_proyecto
        gestor = proyecto.gestor.name
        lista_nombre.append(nombre)
        lista_nombre.append(gestor)
        entregables = Entregable.objects.filter(estatus=False, compromiso=fin, gestion_id=x)

        for y in entregables:
            lista_nombre.append(y.name)
            lista_entregables.append(y.name)
        chat_id = -1001763353987
        nombre_proyecto = lista_nombre[0]
        nombre_gestor = lista_nombre[1]
        texto = ", ".join(lista_entregables)

        texto2 = """
            \U000026A0 Notificación a {} días de Vencimiento:\n
            Nombre del Gestor(a): {}!\n
            Nombre del Proyecto: \U0000066D\U0000066D{}\U0000066D\U0000066D\n
            Entregable(s) a vencer: \U0000066D\U0000066D{}\U0000066D\U0000066D\n
            \U000023F0 Fecha Compromiso: {}\n
            """
        fecha = fin.strftime("%A, %d de %b, %Y")
        texto3 = texto2.format(dias, nombre_gestor, nombre_proyecto, texto, fecha)
        chat_bot.telegram_api(texto3, chat_id)

def get_data_problema_titulo():
    notificaciones(1, 0)
    notificaciones(4, 3)
    notificaciones(9, 8)
    notificaciones(15, 14)

##################################################################################

def get_ordenes_movil():
    now = datetime.date.today()
    tomorrow = datetime.date.today() + timedelta(days=1)
    redes = Notificacion_red.objects.filter(fecha_inicio=tomorrow)
    tis = Notificacion_ti.objects.filter(fecha_inicio=tomorrow)
    chat_id = -224944366
    print(f'Redes len: {len(redes)}')
    print(f'Redes: {redes}')
    print(f'Tis len: {len(tis)}')
    print(f'Tis: {tis}')
    if len(redes) != 0:
        texto = 'Buenas Noches estimados, les comparto las actividades de **RED** para ser validadas el día de hoy: {}\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)
        for x in redes:
            if x.fecha_inicio == tomorrow:
                texto5 = """
                *********************************************************\n          
                \U00002757 OM: {}\n
                Gerente: {}\n
                Categoria: {}\n
                Titulo: {}\n
                Descripción: {}\n
                Afectación: {}\n
                Criticidad: {}\n
                Impacto: {}\n
                Tiempo de Ejecución: {}\n
                Tiempo de Rollback: {}\n
                Tiempo de Afectación: {}\n
                Fecha y Hora Inicio: {} {}\n
                Fecha y Hora Fin: {} {}\n
                Horario de Afectación: {}\n
                Horario entre Afectación: {}\n
            
                """
                texto3 = texto5.format(x.om, x.gerente,x.categoria, x.titulo, x.descripcion, x.afectacion,
                                       x.criticidad, x.impacto, x.tiempo_ejecucion, x.tiempo_rollback,
                                       x.tiempo_afectacion, x.fecha_inicio, x.hora_inicio, x.fecha_fin,
                                       x.hora_fin, x.horario_afectacion, x.horario_entre_afectacion)
                chat_bot.telegram_api(texto3, chat_id)
    else:
        texto = 'Buenas Noches estimados, para el dia de hoy {} no se cuenta con actividades en la parte de **RED**.\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)

    if len(tis) != 0:
        texto = 'Buenas Noches estimados, les comparto las actividades de **TI** para ser validadas el día de hoy: {}\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)
        for x in tis:
            if x.fecha_inicio == tomorrow:
                texto5 = """
                   *********************************************************\n          
                   \U00002757 OM: {}\n
                   Gerente: {}\n
                   Titulo: {}\n
                   Descripción: {}\n
                   Afectación (B2B o B2C): {}\n
                   Criticidad: {}\n
                   Impacto: {}\n
                   Tiempo de Ejecución: {}\n
                   Tiempo de Rollback: {}\n
                   Tiempo de Afectación: {}\n
                   Fecha y Hora Inicio: {} {}\n
                   Fecha y Hora Fin: {} {}\n
                   Afectación: {}\n
                   Horario de Afectación: {}\n
                   Area: {}\n

                   """
                texto3 = texto5.format(x.om, x.gerente,  x.titulo, x.descripcion, x.afectacion,
                                       x.criticidad, x.impacto, x.tiempo_ejecucion, x.tiempo_rollback,
                                       x.tiempo_afectacion, x.fecha_inicio, x.hora_inicio, x.fecha_fin, x.hora_fin,
                                       x.detalle, x.horario_afectacion, x.area)
                chat_bot.telegram_api(texto3, chat_id)
    else:
        texto = 'Buenas Noches estimados, para el dia de hoy {} no se cuenta con actividades en la parte de **TI**.\n'
        texto2 = texto.format(now)
        chat_bot.telegram_api(texto2, chat_id)












