import time
import requests
import telebot
from keep_alive import keep_alive
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
AMAZON_ACCESS_KEY = os.getenv("AMAZON_ACCESS_KEY")
AMAZON_SECRET_KEY = os.getenv("AMAZON_SECRET_KEY")
AMAZON_TAG = os.getenv("AMAZON_TAG")

bot = telebot.TeleBot(BOT_TOKEN)
channel_id = "@dealseekerloots"

def fetch_amazon_deals():
    # Dummy deals to simulate functionality (Replace with real API call)
    return [
        {"title": "Amazon Deal 1", "link": "https://amzn.to/3example1"},
        {"title": "Amazon Deal 2", "link": "https://amzn.to/3example2"},
        {"title": "Amazon Deal 3", "link": "https://amzn.to/3example3"},
    ]

def post_deals():
    deals = fetch_amazon_deals()
    for deal in deals:
        try:
            message = f"🔥 {deal['title']}\n💰 Price: ₹{deal['price']}\n🔗 {deal['link']}"
👉 {deal['link']}"
            bot.send_message(channel_id, message)
        except Exception as e:
            print("Error posting deal:", e)

keep_alive()
while True:
    post_deals()
    time.sleep(600)  # 10 minutes
