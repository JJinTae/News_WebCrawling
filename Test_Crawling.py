#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
import time
import re
import os
import csv


"""
URL = "https://www1.president.go.kr/petitions/59352"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

info_petition = soup.select("ul.petitionsView_info_list > li")
text = remove_whitespaces(soup.find("div", {"class":"View_write"}).text)

print(info_petition[0].get_text(strip=True)[-6:]) # 카테고리
print(info_petition[1].get_text(strip=True)[-10:]) # 청원시작 날짜
print(text)
"""

DATA_DIR = 'Data_CSV'

CSV_PETITION = os.path.join(DATA_DIR, 'petition.csv')


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
    latest_id = 593728
    while latest_id > 593628:
        save_petition(get_petition(latest_id))
        latest_id -= 1
    try:
        print('run...')

    except:
        print('error...')
        pass
    print('end')




# 전체 만료청원 가장 최근에 만료된 청원 번호 가져오기
def get_latest_petition_num():
    # (현재 기능에선 사용하지 않는다. 기간별로 얻고싶기 때문에 직접 값을 넣어주기로 한다.)
    URL = "https://www1.president.go.kr/petitions/?c=0&only=2&page=1&order=1"

    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get(URL)
    time.sleep(2)

    a_tag = driver.find_element_by_xpath("/html/body/div[2]/div[2]/section[2]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[3]/a")
    href = a_tag.get_attribute('href')

    latest_petition_num = int(re.match(r'.+/petitions/(\d+).*', href).group(1))
    print("최근에 만료된 청원 번호 확인")
    return latest_petition_num



# 청원 내용 가져오기
def get_petition(num_petition):

    URL = "https://www1.president.go.kr/petitions/" + str(num_petition)
    html = requests.get(url=URL)
    # response = request.urlopen(URL).read().decode('utf-8')
    soup = BeautifulSoup(html.text, "html.parser")
    print(num_petition)

    # 카테고리 확인
    info_petition = soup.select("ul.petitionsView_info_list > li")
    category = info_petition[0].get_text(strip=True)[-6:] # 카테고리

    if category == "인권/성평등":
        # print("인권/성평등 카테고리입니다.")

        date = info_petition[1].get_text(strip=True)[-10:] # 청원 시작 날짜
        title = soup.find("h3", {"class":"petitionsView_title"}).text # 청원 제목
        content = remove_whitespaces(soup.find("div", {"class": "View_write"}).text) # 청원 내용
        print('date : ', date)
        print('titile : ', title)
        print('content : ', content)
        return {
            'petition_num': num_petition,
            'date': date,
            'title': title,
            'content': content
        }

    return False


def save_petition(petition):
    cols = [
        'petition_num', 'date', 'title', 'content'
    ]
    # 파일이 없으면 파일을 생성하고 cols를 첫행에 추가해준다.
    if not os.path.exists(CSV_PETITION):
        with open(CSV_PETITION, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(cols)
    if petition:
        # 데이터 저장
        with open(CSV_PETITION, 'a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(petition[col] for col in cols)





# 본문의 불필요한 공백 문자 제거
def remove_whitespaces(text):
    lines = text.split('\n')
    lines = (l.strip() for l in lines)
    lines = (l for l in lines if len(l) > 0)

    return '\n'.join(lines)



if __name__ == '__main__':
    main()
