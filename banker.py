#!/usr/bin/env python3
import time
import argparse
from selenium import webdriver


def collect_interest(config):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get('http://www.neopets.com/bank.phtml')

        #Login
        login_form = driver.find_element_by_class_name('welcomeLoginContent')
        username_login = login_form.find_element_by_name('username')
        password_login = login_form.find_element_by_name('password')
        username_login.clear()
        username_login.send_keys(config.username)
        password_login.clear()
        password_login.send_keys(config.password)
        login_button = driver.find_element_by_class_name('welcomeLoginButton')
        login_button.click()

        #Collect interest
        interest_button = driver.find_element_by_xpath(
            '//*[@id="content"]/table/tbody/tr/td[2]/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/div/form/input[2]'
        )
        interest_button.click()

        time.sleep(1)

        driver.quit()

    except Exception:
        driver.quit()

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
    collect_interest(config)


if __name__ == '__main__':
    main()