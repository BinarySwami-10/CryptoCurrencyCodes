from bs4 import BeautifulSoup as soup
import requests
import lxml

def read_ac_power(file_name):
	data=open(file_name, 'r').read()
	variabul=soup(data,'lxml')
	val=variabul.findAll('measurement')[2]
	# print(val['type'],val['value'])
	return val['value']

AC_Power=float(read_ac_power('inverter'))
print(AC_Power)

#compare the variable and send to server , use POST [or your preferred] method

