from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json
import re

def using_selenium(url):
	driver = webdriver.Chrome(r'E:\Python\lite\baitap\Browser\chromedriver.exe')
	driver.get(url)
	sleep(20)
	driver.find_element_by_name('account[email]').send_keys('vietphuongnguyen98@gmail.com')
	sleep(3)
	driver.find_element_by_name('commit').click()
	sleep(2)
	driver.find_element_by_name('account[password]').send_keys('mhbbnhlt')
	sleep(3)
	driver.find_element_by_name('commit').click()
	sleep(2)
	for entity in ['customers', 'products', 'orders']:
		url_resquest = url + '/' + entity.lower() + '.json'
		if entity == 'orders':
			url_resquest += '?status=any'
		driver.get(url_resquest)
		print('Get ' + entity + ' data:')
		data_src = driver.page_source
		# print(data_src)
		find_data = re.findall(r'(\{(.*?)\})', data_src)
		data = find_data[0][0]
		print(data)

url = 'https://nvphuong7.myshopify.com/admin'
using_selenium(url)
