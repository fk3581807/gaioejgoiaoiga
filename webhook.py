import logging
from flask import Flask, request
from telegram.ext import BotHandler

app = Flask(__name__)

TOKEN = 'YOUR_BOT_TOKEN'  # replace with your bot token

bot = BotHandler(TOKEN)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    update = request.get_json()
    if update:
        bot.process_update(update)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)