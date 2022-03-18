from celery import task, shared_task
from django.core.mail import send_mail
from datetime import datetime
import requests


@task
def notificacion_correo_rechado(estatus, cliente, sucursal, oi,motivo, name_ingeniero,correo_destino):
    subject = 'ESTATUS {}  SOBRE LA MT | {} | {} | {}'.format(estatus,cliente, sucursal, oi)
    message = """
        Estimando Ing {}\nSu MT fue rechazada por el siguiente motivo:\n{} \nPor Favor de corregirlos a la brevedad posible.
         
        """
    message2 = message.format(name_ingeniero,motivo)
    from_email = 'rodrigo-josue.rodriguez@inetum.com'
    recipient_list = [correo_destino]

    send_mail(subject,message2,from_email,recipient_list,)


@task
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




@task
def notificacion_telegram(name_ingeniero, estatus, cliente, sucursal, oi):
    texto2 = """
        \U00002714 Estimado Ingeniero {}\n
        La presente es para indicarle  que su MT  {} | {} | {}  fue {}.
        """
    texto = texto2.format(name_ingeniero,  cliente, sucursal, oi,estatus,)
    requests.post('https://api.telegram.org/bot2114681560:AAGPlALNSj-TWi2ipYkkyJ7r6oKbKkJGdz0/sendMessage',
                  data={'chat_id': '-224944366', 'text': texto})

def notificacion_telegram_rechazado(name_ingeniero, estatus, cliente, sucursal, oi, motivo):
    texto2 = """
       \U0000274c Estimado Ingeniero {}\n
        La presente es para indicarle que su MT  {} | {} | {}  fue {}.\n
        Los motivos del rechazo fueron:\n
        {}
        """
    texto = texto2.format(name_ingeniero,  cliente, sucursal, oi,estatus,motivo)
    requests.post('https://api.telegram.org/bot2114681560:AAGPlALNSj-TWi2ipYkkyJ7r6oKbKkJGdz0/sendMessage',
                  data={'chat_id': '-224944366', 'text': texto})

