#-*-utf-8-*-
import requests
import csv
import random
import time
import socket
import http
from bs4 import BeautifulSoup

def get_content(url, date = None):
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    time_out = random.choice(range(50, 100))

    try:
        req = requests.get(url, headers=header, timeout=time_out)
        req.encoding = 'utf-8'
    except socket.timeout as  e:
        print('1:', e)
        time.sleep(random.choice(range(5,10)))
    except socket.error as  e:
        print('1:', e)
        time.sleep(random.choice(range(5,10)))
    except http.client.BadStatusLine as e:
        print('5:', e)
        time.sleep(random.choice(range(30, 80)))

    return req.text


def get_data(html_text):
    str = []
    bs = BeautifulSoup(html_text, 'html.parser')
    body = bs.body
    data = body.find('div', {'id':'7d'})
    ul = data.find('ul');
    li = ul.find_all('li')

    for i in li:
        tmp = []
        date = i.find('h1').string
        tmp.append(date)

        info = i.find_all('p')
        tmp.append(info[0].string)
        temperature_highest = None
        temperature_lowest = None
        if info[1].find('span') is not None:
            temperature_highest = info[1].find('span').string
            temperature_highest = temperature_highest.replace('℃', '')
        if info[1].find('i') is not None:
            temperature_lowest = info[1].find('i').string
            temperature_lowest = temperature_lowest.replace('℃', '')

        tmp.append(temperature_highest)
        tmp.append(temperature_lowest)

        wind = info[2].find('i').string
        tmp.append(wind)
        str.append(tmp)
    return str

def write_file(data, name):
    file_name = name
    with open(name, 'a', errors='ignore', newline='') as f:
        csv_f = csv.writer(f)
        csv_f.writerows(data)

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    data = get_content(url)
    result = get_data(data)
    write_file(result, 'C:\\Users\\Desktop\\weather_sh.csv')

