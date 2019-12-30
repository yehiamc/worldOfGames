from time import sleep
from selenium import webdriver
import sys


def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.get(app_url)
    sleep(1)
    text = driver.find_element_by_id("score").text
    if int(text) >= 0 and int(text) <= 100:
        driver.close()
        return True
    else:
        driver.close()
        return False


def main_function():
    score = test_scores_service("http://127.0.0.1:8777")
    if (score) == True:
        print("True")
        sys.exit(0)
    else:
        print("False")
        sys.exit(-1)


main_function()
