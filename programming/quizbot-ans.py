#!/usr/bin/env python3
# use the wordlist from the scraping script
# to answer all the questions and get the flag

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

wlist = open('list.txt', 'r')

driver = webdriver.Firefox()
driver.get("http://timesink.be/quizbot/index.php")
for answers in wlist:
    bruh = driver.find_element(By.ID,"insert_answer")
    bruh.send_keys(str(answers))
    submit = driver.find_element_by_name("submit")
    submit.send_keys(Keys.ENTER)
    time.sleep(1)
