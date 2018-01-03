#coding=utf-8
from selenium import webdriver
import time
import sys
sys.path.append('\package')
from package import location

we = location

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
dr = webdriver.Chrome(chromedriver)
dr.get('http://www.baidu.com')
we.findId(dr, 'kw').send_keys('selenium')
time.sleep(2)
we.findId(dr, "su").click()
time.sleep(2)

dr.quit()