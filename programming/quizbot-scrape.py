#!/usr/bin/env python3
# sends a blank guess to each question, fetches the answer for each previous question
# to create a wordlist of all the right answers

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

file_object = open('list.txt', 'a')

driver = webdriver.Firefox()
driver.get("http://timesink.be/quizbot/index.php")
while True:
    submit = driver.find_element_by_name("submit")
    submit.send_keys(Keys.ENTER)
    time.sleep(1)
    element = driver.find_element(By.ID,"answer").text
    file_object.write(element+"\n")
