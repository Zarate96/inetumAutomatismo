from datetime import datetime
import requests

def telegram_api():
    texto2 = """
    Tema: {} {} {} {}.\nEstatus: Se notifica al proveedor {} 
    """
    now = datetime.now()
    texto = texto2.format(now, "holding", "sucursal", "afectacion", "proveedor")
    requests.post('https://api.telegram.org/bot1660736119:AAFqlINNPtKGh_Ag5tZ4SUYfocaDH7n_60c/sendMessage',
                  data={'chat_id': '-1001463611893', 'text': texto})

