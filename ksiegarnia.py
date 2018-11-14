from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import xlwt
import xlrd
import urllib
from xlutils.copy import copy


driver = webdriver.Firefox()


driver.get("https://www.taniaksiazka.pl/")
linkk = 'q'
search = driver.find_element_by_name(linkk)
search.send_keys("bogurodzica")
searchButton = driver.find_element_by_class_name('button')
searchButton.click()
cena = driver.find_element_by_class_name('product-price')
print(cena.text)
driver.get("https://www.taniaksiazka.pl/")
linkk = 'q'
search = driver.find_element_by_name(linkk)
search.send_keys("Bolesław Prus- Lalka")
searchButton = driver.find_element_by_class_name('button')
searchButton.click()
cena = driver.find_element_by_class_name('product-price')
print(cena.text)
rb = xlrd.open_workbook("lq2.xls")
wb = copy(rb)
wsheet = wb.get_sheet(0)
#wsheet.write(i-1,1,cena.text)
wb.save("lq2.xls")
driver.close()
