from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

import sqlite3


def make_db():

    path = 'https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd=005930&cn='
    chrome = webdriver.Chrome()
    chrome.get(path)

    chrome.find_element_by_xpath('//*[@id="rpt_td1"]').click()
    time.sleep(5)
    html_is = chrome.page_source
    soup_is = BeautifulSoup(html_is, 'html.parser')
    fs_is = soup_is.find('table', {'class': 'gHead01 all-width data-list'})

    chrome.find_element_by_xpath('//*[@id="rpt_td2"]').click()
    time.sleep(5)
    html_bs = chrome.page_source
    soup_bs = BeautifulSoup(html_bs, 'html.parser')
    fs_bs = soup_bs.find('table', {'class': 'gHead01 all-width data-list'})

    chrome.find_element_by_xpath('//*[@id="rpt_td3"]').click()
    time.sleep(5)
    html_cf = chrome.page_source
    soup_cf = BeautifulSoup(html_cf, 'html.parser')
    fs_cf = soup_cf.find('table', {'class': 'gHead01 all-width data-list'})


    chrome.close()

    # con = sqlite3.connect('./fs_is.db')
    # cur = con.cursor()
    # for i in code_df.code:
    #     tablename = 'CREATE TABLE "' + i +'"'
    #     cur.execute(tablename+' (name text)')

    print(fs_is)
    print('______________________________________________________________________________________________________________________________________________________________________________________')
    print(fs_bs)
    print('______________________________________________________________________________________________________________________________________________________________________________________')
    print(fs_cf)





if __name__ == '__main__':
    make_db()
