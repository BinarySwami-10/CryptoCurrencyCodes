import bs4
import html5lib
import selenium;import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time as t

url='https://bitcointicker.co/'
driver = webdriver.Firefox()
driver.get(url)
temp_val=[0]
for i in range(0,100):
	t.sleep(1)

	heading1 = driver.find_element_by_id('lastTrade').text
	temp_val.append(heading1)
	if temp_val[1]==temp_val[0]:
		# print('same')
		pass
	else:
		print(temp_val[1])
	temp_val.pop(0)

driver.close()





# dirs=os.sys.path
# dirs.append('/home/nikhil/Desktop/python')
# print(dirs)
