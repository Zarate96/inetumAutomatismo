from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from task import chat_bot, email, querys

def start():
    scheduler = BackgroundScheduler()
    #scheduler.add_job(chat_bot.telegram_api, 'interval', minutes=1)
    #scheduler.add_job(email.enviomail, 'interval', minutes=5)
    #scheduler.add_job(selenium.get_rstat, 'interval', minutes=30)
    #scheduler.add_job(selenium.get_onstar, 'interval', minutes=3)
    #scheduler.add_job(selenium.get_glpi, 'interval', minutes=45)
    #scheduler.add_job(selenium.get_santander, 'interval', minutes=1)
    #scheduler.add_job(querys.get_data, 'interval', minutes=1)
    scheduler.add_job(querys.get_data_problema, 'interval', minutes=1)
    scheduler.start()