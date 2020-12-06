import requests
from bs4 import BeautifulSoup
import time


URL = "https://www1.president.go.kr/petitions/?c=49&only=2&page=1&order=1"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

get_all_course = soup.find_all("div", {"class":"bl_no"})

print(get_all_course)



def parsing_course(elements):
    print(elements.text)
    print("-------")


for i in get_all_course:
    parsing_course(i)
    # print(i)




def main():
    while True:
        try:
            run()
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


def get_latest_petition_num():
    URL = "https://www1.president.go.kr/petitions/?c=49&only=2&page=1&order=1"
    html = requests.get(url=URL)
    soup = BeautifulSoup(html.text, "html.parser")

    latest_petition_num = soup.find_all("div", {"class": "bl_no"})



    return latest_petition_num



if __name__ == '__main__':
    main()
