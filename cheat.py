#!/bin/python3
from telethon import TelegramClient, events, sync
import names
from passwordgenerator import pwgenerator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Constants as cons
from random_username.generate import generate_username

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
                print("Fake email generated: " + fake_mail)
                sign_up()

def generate_email():
    client.send_message(id_fakemailbot, "/generate")


# Github SignUp
driver = webdriver.Firefox()
link = "https://github.com/join"
def sign_up():
    global fake_mail
    username = generate_username(1)[0]
    email = fake_mail
    password = fake_mail
    driver.get(link)
    # finding text fields
    element_username = driver.find_element_by_id("user_login")
    element_email = driver.find_element_by_id("user_email")
    element_password = driver.find_element_by_id("user_password")
    # sending details to text fields
    element_username.send_keys(username)
    element_email.send_keys(email)
    element_password.send_keys(password)

client.start()
generate_email()
# sign_up()
client.run_until_disconnected()