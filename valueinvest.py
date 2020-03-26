import getcode
import makedb

def value_invest():
    company_code = getcode.get_code()
    # 유가증권시장 상장 코드 및 회사명 가져오기
    makedb(company_code)
    # 상장회사의 최근 5년간 재무정보를 DB화 하기
    # magic_formular()
    # 마법공식 자료 가져오기
    # safety_first()
    # 자본손실 의심 회사의 제거
    # economic_moat()
    # 경제적 해자를 가진 기업 조사
    # whatch_company()
    # 관심기업의 200ma 및 5ma 추척
    # buy_sell()
    # 관심기업의 자동매매

if __name__ == '__main__':
    print(value_invest())



