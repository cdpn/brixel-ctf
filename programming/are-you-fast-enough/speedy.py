#!/usr/bin/env python3
#Objective: copy the random string below into the input form and submit within 1 second(s) to win!

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://timesink.be/speedy/index.php")
element = driver.find_element(By.ID,"rndstring").text
driver.find_element(By.ID,"inputfield").send_keys(element)
driver.find_element(By.ID,"submitbutton").send_keys(Keys.ENTER)
