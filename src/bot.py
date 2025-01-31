import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from api.pumpfun_api import check_pumpfun_migrations
from utils.validators import validate_conditions
from utils.alert_manager import send_alert
from config import settings
import schedule
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class MemecoinBot:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.job_queue = self.updater.job_queue

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("🚨 Bot en ligne ! Surveillance des migrations Pump.fun → Raydium")

    def check_migrations(self, context: CallbackContext):
        try:
            migrations = check_pumpfun_migrations()
            for coin in migrations:
                if validate_conditions(coin):
                    send_alert(context.bot, coin)
        except Exception as e:
            logging.error(f"Erreur de vérification : {str(e)}")

    def run(self):
        self.job_queue.run_repeating(self.check_migrations, interval=300, first=10)  # Vérifie toutes les 5 min
        self.updater.start_polling()
        self.updater.idle()

if __name__ == "__main__":
    bot = MemecoinBot(settings.TELEGRAM_TOKEN)
    bot.run()
