from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import sqlite3


def make_db(company_code):
    def crawling(click, order=0):
        chrome.find_element_by_xpath(click).click()
        time.sleep(5)
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        html = soup.find_all('table', {'class': 'gHead01 all-width data-list'})
        table_value = []
        head_value = []
        for i in html[order].find_all('tr'):
            for h in i.find_all('th'):
                head_value.append(h.get_text())
            value = []
            for ii in i.find_all('td'):
                value.append(ii.get_text())
            table_value.append(value)

        df = pd.DataFrame(data=table_value, columns=head_value)
        df.columns = df.columns.str.replace(r'\n', '')
        df = df.replace(r'[\t\n]', '', regex=True)
        df = df.replace(r'펼치기', '', regex=True)
        df = df.set_index(['항목'])
        return (df)

    chrome = webdriver.Chrome()

    # 크롬 열기 종목코드의 재무분석 페이지
    path_fs = 'https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd='+company_code+'&cn='
    chrome.get(path_fs)
    financial_statement = []
    # 손익계산서 //*[@id="rpt_td1"], 재무상태표 //*[@id="rpt_td2"] 현금흐름표 //*[@id="rpt_td3"]
    rpt_button = ['//*[@id="rpt_td1"]', '//*[@id="rpt_td2"]', '//*[@id="rpt_td3"]']
    for click in rpt_button:
        financial_statement.append(crawling(click))

    # 크롬 열기 종목코드의 투자지표 페이지
    path_ii ='https://navercomp.wisereport.co.kr/v2/company/c1040001.aspx?cmp_cd='+company_code+'&cn='
    chrome.get(path_ii)
    invest_index = []
    # 수익성 //*[@id="val_td1"], 성장성//*[@id="val_td2"], 안정성//*[@id="val_td3"], 활동성//*[@id="val_td4"]
    # 가치분석 // *[ @ id = "viVGVTbkwxZ2"] / table[2]
    val_button = ['//*[@id="val_td1"]', '//*[@id="val_td2"]', '//*[@id="val_td3"]', '//*[@id="val_td4"]', '// *[ @ id = "viVGVTbkwxZ2"] / table[2]']
    for click in val_button:
        if click=='// *[ @ id = "viVGVTbkwxZ2"] / table[2]':
            invest_index.append(crawling(click,order=1))
        else:
            invest_index.append(crawling(click))

    # db에 입력하는 부분
    # con = sqlite3.connect('fs_is.db')
    # financial_statement[0].to_sql('fs_is.db', con, if_exists='append')
    # # todo 1. 컬럼명 '전년대비(YoY)'가 두개임....충돌발생으로 인하여 입력이 되지 않음
    chrome.close()



    # 여기는 테스트 부분임
    # print(financial_statement[0].head(10))
    # print(financial_statement[1].head(10))
    # print(financial_statement[2].head(10))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(invest_index[0].head(10))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(invest_index[1].head(10))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(invest_index[2].head(10))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(invest_index[3].head(10))
    # print('______________________________________________________________________________________________________________________________________________________________________________________')
    # print(invest_index[4].head(10))




if __name__ == '__main__':
    make_db('005930')
