import os
import telebot
import requests
from flask import Flask, request

# Load token from environment variable (Render -> Environment tab)
API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Default route to confirm server is running
@app.route('/')
def home():
    return 'Dealseeker Bot is running!'

# Webhook handler
@app.route(f"/{API_TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Sample command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to DealSeekerLoot Bot!")

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
