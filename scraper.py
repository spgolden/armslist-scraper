#!/usr/bin/env python
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict
from dateutil.parser import parse
from datetime import datetime

ARMSLIST_URL = 'http://www.armslist.com/classifieds/search'
STOP_DATETIME = datetime(2016, 6, 13, 0, 0, 0)

def scrape(stop_datetime):
    param_arguments = [('location', 'florida'), ('category', 'guns'), ('posttype', '3'), ('page', 1)]
    params = OrderedDict(param_arguments)
    response = requests.get(ARMSLIST_URL, params=params)
    print(response.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find(id='bootstrap-overrides')
    divs = container.find_all('div')
    soup.find_all('div', position='absolute')
    for div in divs:
        href = div.get('href')
        if href:
            table = div.find('table')
            second_td = div.find_all('td')[1]
            third_div = second_td.find_all('div')[2]
            junk, date_string = third_div.string.strip().split(', ')
            parsed_date = parse(date_string)
            if parsed_date < stop_datetime:
                break
            print(parsed_date)


if __name__ == '__main__':
    scrape(STOP_DATETIME)
