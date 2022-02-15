#rom celery import task, shared_task
from django.core.mail import send_mail
from datetime import datetime
import requests


""" 
@task
def notificacion(proyecto_id):
    order = Gestion.objects.get(id=proyecto_id)
    
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
    f'You have successfully placed an order.' \
    f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
    message,
    'admin@myshop.com',
    [order.email])
    return mail_sent

"""

# @task
# def notificacion_telegram(proyecto_id, name_proyecto, old_estado, new_estado):
#     texto2 = """
#         SE HA ACTUALIZADO EL PROYECTO CON ID {} {}:\nESTABA CON EL ESTADO **{}**, Y AHORA TIENE ESTE NUEVO ESTADO **{}** 
#         """
#     texto = texto2.format(proyecto_id, name_proyecto, old_estado, new_estado)
#     requests.post('https://api.telegram.org/bot1660736119:AAFqlINNPtKGh_Ag5tZ4SUYfocaDH7n_60c/sendMessage',
#                   data={'chat_id': '1001763353987', 'text': texto})

