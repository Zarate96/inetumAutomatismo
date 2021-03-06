from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from task import chat_bot, email, querys, selenium

def start():
    scheduler = BackgroundScheduler(timezone="America/Mexico_City")
    #scheduler.add_job(querys.get_migraciones_dalia, 'cron', day_of_week='0-6', hour='7')
    #scheduler.add_job(querys.get_data_problema_titulo, 'interval', minutes=1)
    scheduler.add_job(querys.get_data_problema_titulo, 'cron', day_of_week='0-4', hour='10')
    #scheduler.add_job(selenium.get_hcAPN, 'cron', day_of_week='0-6', hour='9')
    #scheduler.add_job(selenium.get_hcRutasInter, 'cron', day_of_week='0-6', hour='7')
    #scheduler.add_job(selenium.get_hcRutasInter, 'cron', day_of_week='0-6', hour='15')
    #scheduler.add_job(selenium.get_hcRutasInter, 'cron', day_of_week='0-6', hour='23')
    #scheduler.add_job(querys.get_migraciones_dalia, 'interval', minutes=60)
    #scheduler.add_job(querys.get_ordenes_movil, 'cron', day_of_week='0-6', hour='20')
    #scheduler.add_job(querys.get_migraciones_dalia, 'interval', minutes=1)
    #scheduler.add_job(chat_bot.telegram_api, 'interval', minutes=1)
    #scheduler.add_job(email.enviomail, 'interval', minutes=5)
    #scheduler.add_job(selenium.get_rstat, 'interval', minutes=30)
    #scheduler.add_job(selenium.get_onstar, 'interval', minutes=3)
    #scheduler.add_job(selenium.get_glpi, 'interval', minutes=45)
    #scheduler.add_job(selenium.get_santander, 'interval', minutes=1)
    #scheduler.add_job(querys.get_data, 'interval', minutes=1)
    #scheduler.add_job(querys.get_data_problema_titulo, 'cron', day_of_week='0-4', hour='10')
    #scheduler.add_job(querys.get_ordenes_movil, 'interval', minutes=1)
    #scheduler.add_job(querys.get_migraciones_dalia, 'interval', minutes=1)
    #scheduler.add_job(selenium.get_hcInterATT, 'interval', minutes=1)
    scheduler.start()
