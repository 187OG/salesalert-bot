from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/')
def home():
    return '✅ Bot läuft!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == "/start":
            send_message(chat_id, "👋 Willkommen! Ich bin dein SalesAlert Bot.")
        elif text == "/alert":
            send_message(chat_id, "📈 Token-Sale erkannt!")
        else:
            send_message(chat_id, "✅ Deine Chat-ID: " + str(chat_id))

    return '', 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
