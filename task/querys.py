from task import chat_bot
from problema.models import Entregable
from django.utils import  timezone
import datetime
import pandas as pd

def get_data_problema():
    entregables = Entregable.objects.filter(estatus=False)
    for x in entregables:
        if x.compromiso is not None:
            print("no data")
        now = datetime.date.today()
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















