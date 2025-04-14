import telebot
import requests
from flask import Flask, request

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Sample endpoint to check if server is running
@app.route('/')
def home():
    return 'Bot is running!'

@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    webhook_url = f'https://YOUR_RENDER_DOMAIN/{API_TOKEN}'
    bot.remove_webhook()
    success = bot.set_webhook(url=webhook_url)
    if success:
        return "Webhook set successfully!"
    else:
        return "Webhook setup failed"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to DealSeeker Bot! Type /deals to get latest Amazon loot deals.")

@bot.message_handler(commands=['deals'])
def send_deals(message):
    deals = fetch_loot_deals()
    for deal in deals:
        text = f"{deal['title']}\nPrice: ₹{deal['price']}\nLink: {deal['link']}"
        bot.send_message(message.chat.id, text)

def fetch_loot_deals():
    # Replace this mock data with real API logic if needed
    return [
        {
            "title": "Noise Smart Watch with 1.4'' Display",
            "price": "1,299",
            "link": "https://amzn.to/example1"
        },
        {
            "title": "boAt Bassheads 100 Wired Earphones",
            "price": "349",
            "link": "https://amzn.to/example2"
        },
        {
            "title": "Samsung 25W USB-C Fast Charger",
            "price": "899",
            "link": "https://amzn.to/example3"
        }
    ]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
