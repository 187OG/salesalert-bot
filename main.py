from flask import Flask, request
import telegram
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    message = data.get("message", "No message provided")
    bot.send_message(chat_id=CHAT_ID, text=message)
    return "Alert sent", 200

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
