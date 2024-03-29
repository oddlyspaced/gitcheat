#!/bin/python3
from telethon import TelegramClient, events, sync
import names
from passwordgenerator import pwgenerator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Constants as cons
from random_username.generate import generate_username
import time

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
    print("Generating FakeEmail")
    client.send_message(id_fakemailbot, "/generate")

# Github SignUp
option = webdriver.ChromeOptions()
# For ChromeDriver version 79.0.3945.16 or over
# Hide automation
option.add_argument('--disable-blink-features=AutomationControlled')
#Open Browser
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=option)
link = "https://github.com/join"
def sign_up():
    global fake_mail
    print("Fake details generated:")
    username = generate_username(1)[0]
    email = fake_mail
    password = fake_mail
    print("Username: " + str(username) + "\nEmail: " + str(email) + "\nPassword: " + password)
    print("Loading Sign Up Page...")
    driver.get(link)
    # finding text fields
    print("Filling text fields...")
    element_username = driver.find_element_by_id("user_login")
    element_email = driver.find_element_by_id("user_email")
    element_password = driver.find_element_by_id("user_password")
    # sending details to text fields
    element_username.send_keys(username)
    element_email.send_keys(email)
    element_password.send_keys(password)
    # finding continue button
    wait_for_verification()

def wait_for_verification():
    print("Waiting for verification...")
    element_button = driver.find_element_by_id("signup_button")
    while (element_button.get_attribute("disabled") != None):
        time.sleep(1)
    print("Verified!")
    element_button.click()
    try :
        verify_join()
    except:
        follow_oddly()

def verify_join():
    element_button = driver.find_element_by_id("signup_button")
    print("Waiting for Join Github verification")
    while (element_button.get_attribute("disabled") != None):
        time.sleep(1)
    print("Verified and sign up done!")
    follow_oddly()

def follow_oddly():
    driver.get("https://github.com/oddlyspaced")
    print("Following oddly")
    # Follow oddlyspaced
    element_follow = driver.find_element_by_name("commit")
    driver.execute_script("arguments[0].click();", element_follow)
    driver.get("https://github.com/oddlyspaced")
    print("Done")
    time.sleep(3)
    client.disconnect()
    driver.quit()
    quit(0)

client.start()
generate_email()
# sign_up()
client.run_until_disconnected()
