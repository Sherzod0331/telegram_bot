from my_account import *
from pages import *
from selenium import webdriver
from time import sleep

# print(my_account.my_login,my_account.my_pass)


brower = webdriver.Firefox()
brower.implicitly_wait(5)

# home_page=HomePage(brower)
# login_page=home_page.go_to_login_page() 
# login_page.login(my_login,my_pass) 

brower.implicitly_wait(5)
brower.get('https://www.instagram.com/')

username_input=brower.find_element_by_css_selector("input[name='username']")
password_input=brower.find_element_by_css_selector("input[name='password']")

username_input.send_keys(my_login)
password_input.send_keys(my_pass)

login_button=brower.find_element_by_css_selector("button[type='submit']")
login_button.click()

sleep(15)
# brower.close()



