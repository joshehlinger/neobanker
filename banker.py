#!/usr/bin/env python3
import time
import sys
import argparse
import datetime
from selenium import webdriver


def collect_interest(config):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    try:
        print ('Run starting at {}'.format(str(datetime.datetime.now())))
        driver.get('http://www.neopets.com/bank.phtml')

        #Login
        print('Logging in...')
        login_form = driver.find_element_by_class_name('welcomeLoginContent')
        username_login = login_form.find_element_by_name('username')
        password_login = login_form.find_element_by_name('password')
        username_login.clear()
        username_login.send_keys(config.username)
        password_login.clear()
        password_login.send_keys(config.password)
        login_button = driver.find_element_by_class_name('welcomeLoginButton')
        login_button.click()
        print('Login successful')

        #Collect interest
        interest_button = driver.find_element_by_css_selector("input[value^='Collect Interest']")
        interest_button.click()
        print('Collected Interest!')

        time.sleep(1)
        driver.quit()
        return 0

    except Exception:
        driver.quit()
        return 1

def arg_parser() -> argparse.ArgumentParser:
    desc = 'Collect that interest'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--username',
                        dest='username',
                        metavar='',
                        help='username')
    parser.add_argument('--password',
                        dest='password',
                        metavar='',
                        help='password')
    return parser


def main(args=None):
    parser = arg_parser()
    config = parser.parse_args(args=args)
    if config.username is None or config.password is None:
        print('Username and Password are required!')
        return 1
    return collect_interest(config)


if __name__ == '__main__':
    sys.exit(main())