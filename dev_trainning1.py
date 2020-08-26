from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests


def using_request(url):
	value = {'log': 'admin', 'pwd': '123456aA'}
	r = requests.post(url, data=value)
	print(r.cookies.keys()[0])


def using_selenium(url):
	driver = webdriver.Chrome(r'D:\Python\lite\Browser\chromedriver.exe')
	driver.get(url)
	driver.find_element_by_name('log').send_keys('admin')
	driver.find_element_by_name('pwd').send_keys('123456aA')
	driver.find_element_by_name('wp-submit').send_keys(Keys.ENTER)
	print(driver.get_cookies()[0]['name'])
	driver.close()

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
using_selenium(url)
using_request(url)
