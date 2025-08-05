import logging
import os
from telegram.ext import Updater, CommandHandler

# Lese Umgebungsvariablen von Railway
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Logging (hilfreich für Fehlersuche)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start-Befehl
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ Bot läuft!")

# Funktion zum Senden eines Alerts
def alert(context):
    context.bot.send_message(chat_id=CHAT_ID, text="📈 Token-Sale erkannt!")

# Manuelles Auslösen eines Alerts per /alert
def trigger_alert(update, context):
    alert(context)

# Hauptfunktion
def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("alert", trigger_alert))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
