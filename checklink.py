from selenium import webdriver
import time
import link

check = webdriver.Chrome('<link to chromedriver>')


def check_invite(b):
    check.get(b)
    time.sleep(1)  # wait for window to completely load
    try:
        check.find_element_by_css_selector(
            '.auth-form.form.deprecated.auth-form-invite.register')  # check to see if link is valid
        return '{} {}'.format('Link found at', b)
    except:
        return 0


yes = 1
while yes:
    invite = link.create()
    ok = check_invite(invite)
    if ok:
        print(ok)
        yes = 0
check.close()
