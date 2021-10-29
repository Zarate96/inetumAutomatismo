import requests

def telegram_api(texto,numero_chat):
    requests.post('https://api.telegram.org/bot1660736119:AAFqlINNPtKGh_Ag5tZ4SUYfocaDH7n_60c/sendMessage',
                  data={'chat_id': numero_chat, 'text': texto})



