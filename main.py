import logging
from telegram.ext import Updater, CommandHandler

# Bot-Token und Chat-ID
BOT_TOKEN = 
          7331834305:AAGZMbAH3eElxbQOpKXpPD5ZLnXbQHEYaNQ
        
CHAT_ID = 7715882549

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot läuft!")

def alert(context):
    context.bot.send_message(chat_id=CHAT_ID, text="📈 Token-Sale erkannt!")

def trigger_alert(update, context):
    alert(context)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("alert", trigger_alert))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
