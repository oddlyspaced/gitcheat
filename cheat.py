#!/bin/python3
from telethon import TelegramClient, events, sync
import names
from passwordgenerator import pwgenerator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Constants as cons

api_id = cons.api_id
api_hash = cons.api_hash

# Constants for telegram side
generate_count = 0
id_fakemailbot = 'fakemailbot'
new_mail_string = 'Your new fake mail id'
fake_mail = ''
fake_mail_domain = '@hi2.in'

# Initialising the Telegram Client
client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def response_handler(event):
    # new fake mail
    global fake_mail
    if new_mail_string in event.raw_text:
        words = str(event.raw_text).split(" ")
        for word in words:
            if fake_mail_domain in word:
                fake_mail = word
                print(fake_mail)

def generate_email():
    client.send_message(id_fakemailbot, "/generate")


client.start()
generate_email()
client.run_until_disconnected()