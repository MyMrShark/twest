from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import xlwt
import xlrd
import urllib
from xlutils.copy import copy

driver = webdriver.Firefox()
driver.get("http://zse.bialystok.pl/")


driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("http://zse.bialystok.pl/biblioteka/lektury/")
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])


book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("lektury")

for i in range(1, 46):
    link = '//*[@id="post-680"]/div/div/div/ul[1]/li[' + str(i) + ']'
    elem = driver.find_element_by_xpath(link)
    print(elem.text.find(" - "))
    print(elem.text.find(" – "))
    sheet.write(i - 1, 0, elem.text)
for i in range(1, 46):
    driver.get("http://zse.bialystok.pl/biblioteka/lektury/")
    link = '//*[@id="post-680"]/div/div/div/ul[1]/li[' + str(i) + ']'
    elem = driver.find_element_by_xpath(link)
    pq = elem.text
    print(pq)
    driver.get("https://www.taniaksiazka.pl/")
    linkk = 'q'
    search = driver.find_element_by_name(linkk)
    search.send_keys(pq)
    searchButton = driver.find_element_by_class_name('button')
    searchButton.click()
    cena = driver.find_element_by_class_name('product-price')
    print(cena.text)
    sheet.write(i-1,1,cena.text)


book.save("LAZONE.xls")
driver.close()