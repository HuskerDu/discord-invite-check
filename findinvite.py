from selenium import webdriver
from random import randint
from random import choice
import time

check = webdriver.Chrome('<link to chromedriver location>')
while True:
    b = 'http://discord.gg/'
    for i in range(7):
        a = [randint(48, 57), randint(65, 90), randint(97, 122)]
        b += chr(choice(a))    # generating possible invite link
    check.get(b)
    time.sleep(1)   # wait for window to completely load
    try:
        check.find_element_by_css_selector('.auth-form.form.deprecated.auth-form-invite.register')  # check to see if link is valid
        print('Link found at '+b)
        break
    except:
        print('Fail')
check.close()
