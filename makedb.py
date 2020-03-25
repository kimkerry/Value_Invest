from selenium import webdriver
import time
from bs4 import BeautifulSoup
from IPython.display import display_html
import pandas as pd
import re
import sqlite3


def make_db():
    # todo 4. get_code 함수의 리턴값을 받아서 for 문을 돌려 각각의 상장코드별로 path에 넣어줘야 함
    path = 'https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd=005930&cn='
    chrome = webdriver.Chrome()
    chrome.get(path)

    chrome.find_element_by_xpath('//*[@id="rpt_td1"]').click()
    time.sleep(5)
    html_is = chrome.page_source
    soup_is = BeautifulSoup(html_is, 'html.parser')
    html_fs_is = soup_is.find('table', {'class': 'gHead01 all-width data-list'})
    table_value = []
    head_value =[]
    for i in html_fs_is.find_all('tr'):
        for h in i.find_all('th'):
            head_value.append(h.get_text())
        value = []
        for ii in i.find_all('td'):
            value.append(ii.get_text())
        table_value.append(value)
    df_fs_is = pd.DataFrame(data = table_value, columns = head_value)
    df_fs_is.replace(['\t','\n'],'')

    # df_fs_is = df_fs_is.set_index(df_fs_is.iloc[:,0], drop=True)

    # df_fs_is = df_fs_is.str.replace(pat=r'[\s\s+]', repl = r' ', regex = True)
    # df_fs_is = df_fs_is[0]
    # todo 1. 표의 펼치기 부분은 데이터프레임으로 들어가지 않음 -> 데이타는 있음에도 불구하고 아마도 컬럼명이 하나라서 맨 앞의것만 나오는거 같음

    # chrome.find_element_by_xpath('//*[@id="rpt_td2"]').click()
    # time.sleep(5)
    # html_bs = chrome.page_source
    # soup_bs = BeautifulSoup(html_bs, 'html.parser')
    # fs_bs = soup_bs.find('table', {'class': 'gHead01 all-width data-list'})
    # todo 2. 1번 todo를 완성하고 나서 여기랑 밑에도 같이 수정해야 함

    # chrome.find_element_by_xpath('//*[@id="rpt_td3"]').click()
    # time.sleep(5)
    # html_cf = chrome.page_source
    # soup_cf = BeautifulSoup(html_cf, 'html.parser')
    # fs_cf = soup_cf.find('table', {'class': 'gHead01 all-width data-list'})


    chrome.close()

    # con = sqlite3.connect('./fs_is.db')
    # cur = con.cursor()
    # for i in code_df.code:
    #     tablename = 'CREATE TABLE "' + i +'"'
    #     cur.execute(tablename+' (name text)')
    # todo 3. is, bs, cf별로 DB를 만든 후 상장코드 별로 table을 만들고 값을 넣어줘야 함


    # 여기는 테스트 부분임
    print(df_fs_is.head(20))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(fs_bs)
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(fs_cf)





if __name__ == '__main__':
    make_db()
