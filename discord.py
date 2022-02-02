from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
import threading
from selenium.webdriver.common.by import By

message_content = """TRIUMPHAL WARRIOR 
NFT FIGHTING GAME PLAY TO EARN COMING SOON X100 :rocket:

Website: https://triumphalwarrior.com/  
Discord: https://discord.gg/3JtWQbFvMY
Twitter: @triumphalwar01
Instagram: https://www.instagram.com/triumphalwarrior/

May the best win ! :trophy:

YOU ARE EARLY ! don't miss your chance !

BIG GIVEAWAY VALUE 1500 :heavy_dollar_sign:

TO PARTICIPATE :

Join us on Discord

https://discord.gg/3JtWQbFvMY


Good luck The warriors :gift: :four_leaf_clover: :fingers_crossed:

"""
driver = webdriver.Chrome()

driver.get("https://discord.com/login")
time.sleep(6)
#--------------------------------------------------------------- Email and password --------------------------#
username_input = driver.find_element_by_name('email')
username_input.send_keys("")


password_input = driver.find_element_by_name('password')
password_input.send_keys("")


btn = driver.find_element(By.CSS_SELECTOR,'.marginBottom8-AtZOdT.button-38aScr')
btn.click()
time.sleep(6)
driver.get("https://discord.com/channels/711242066260262994/807247247212412928")
time.sleep(6)



o = []

#layout-2DM8Md
like = driver.find_elements_by_class_name('member-3-YXUe')









    

index = 0
while True:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'member-3-YXUe')))
    members = driver.find_elements(By.CLASS_NAME,'member-3-YXUe')
    try:
        time.sleep(3)
        members[index].click()    
        time.sleep(3)
        
        message_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'input-2_SIlA')))
        
        message_input.send_keys("Hi !")
        message_input.send_keys(Keys.ENTER)
        time.sleep(2)
        """messagebox = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div/span/span/span')
                
        messagebox.send_keys(message_content)"""
                
        index += 1
        driver.back()
    except IndexError:
        time.sleep(3)
        try:
            time.sleep(3)
            members[index].click()    
            time.sleep(3)
            
            message_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'input-2_SIlA')))
            
            message_input.send_keys("Hi !")
            message_input.send_keys(Keys.ENTER)
            time.sleep(2)
            index += 1
            driver.back()
        except IndexError:
            print('last member!')
            break
          
    print(index)
    