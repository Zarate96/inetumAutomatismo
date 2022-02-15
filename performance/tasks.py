from celery import shared_shared_task
from django.core.mail import send_mail
from datetime import datetime
import requests


@shared_task
def notificacion_correo_rechado(estatus, cliente, sucursal, oi,motivo, name_ingeniero,correo_destino):
    subject = 'ESTATUS {}  SOBRE LA MT | {} | {} | {}'.format(estatus,cliente, sucursal, oi)
    message = """
        Estimando Ing{}\nSu MT fue rechazada por el siguiente motivo:\n{} \nPor Favor de corregirlos a la brevedad posible.
         
        """
    message2 = message.format(name_ingeniero,motivo)
    from_email = 'rodrigo-josue.rodriguez@inetum.com'
    recipient_list = [correo_destino]

    send_mail(subject,message2,from_email,recipient_list,)


@shared_task
def notificacion_correo_aceptado(estatus, cliente, sucursal, oi,name_ingeniero, correo_destino):
    subject = 'ESTATUS {}  SOBRE LA MT | {} | {} | {}'.format(estatus, cliente, sucursal, oi)
    message = """
    Estimado Ing {}
        Felicidades su MT fue aceptada.

        """
    message2 = message.format(name_ingeniero)
    from_email = 'rodrigo-josue.rodriguez@inetum.com'
    recipient_list = [correo_destino]

    send_mail(subject, message2, from_email, recipient_list, )




@shared_task
def notificacion_telegram(proyecto_id, name_proyecto, old_estado, new_estado):
    texto2 = """
        SE HA ACTUALIZADO EL PROYECTO CON ID {} {}:\nESTABA CON EL ESTADO **{}**, Y AHORA TIENE ESTE NUEVO ESTADO **{}** 
        """
    texto = texto2.format(proyecto_id, name_proyecto, old_estado, new_estado)
    requests.post('https://api.telegram.org/bot1660736119:AAFqlINNPtKGh_Ag5tZ4SUYfocaDH7n_60c/sendMessage',
                  data={'chat_id': '1663958489', 'text': texto})
