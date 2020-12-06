import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re




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
    get_petition(593813)



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



def get_petition(num_petition):

    URL = "https://www1.president.go.kr/petitions/" + str(num_petition)
    response = requests.get(url=URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # 카테고리 확인을 위한
    info_petition = soup.select("ul.petitionsView_info_list > li")
    category = info_petition[0].get_text(strip=True)[-6:]

    print(info_petition[0].get_text(strip=True)[-6:])  # 카테고리
    print(info_petition[1].get_text(strip=True)[-10:])  # 청원시작 날짜

    if category == "인권/성평등":
        print("인권/성평등 카테고리입니다.")
        print(info_petition[1].get_text(strip=True)[-10:])  # 청원시작 날짜

        text = remove_whitespaces(soup.find("div", {"class": "View_write"}).text)
        print(text)
    else:
        print("카테고리가 해당되지 않습니다.")









# 본문의 불필요한 공백 문자 제거
def remove_whitespaces(text):
    lines = text.split('\n')
    lines = (l.strip() for l in lines)
    lines = (l for l in lines if len(l) > 0)

    return '\n'.join(lines)



if __name__ == '__main__':
    main()
