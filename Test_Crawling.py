import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time



def main():
    while True:
        run()
        try:
            pass
            break
        except:
            print('wait for server 5 seconds...')
            time.sleep(5)

def run():
    # 데이터를 저장할 디렉터리 생성
    try:
        pass
    except:
        pass
    print('run...')
    print(get_latest_petition_num())



# 인권 / 성평등 만료청원 가장 최근에 만료된 청원 번호 가져오기
def get_latest_petition_num():
    URL = "https://www1.president.go.kr/petitions/?c=49&only=2&page=1&order=1"

    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get(URL)
    time.sleep(2)

    latest_petition_num = int(driver.find_element_by_xpath("/html/body/div[2]/div[2]/section[2]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[1]").text)

    return latest_petition_num



if __name__ == '__main__':
    main()
