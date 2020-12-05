import requests
from bs4 import BeautifulSoup

URL = "https://www.inflearn.com/courses/it-programming/mobile-app"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

get_all_course = soup.find_all("div", {"class":"course_title"})

print(get_all_course)

def parsing_course(elements):
    print(elements.find("course_title").text)
    print("-------")

for i in get_all_course:
    parsing_course(i)
    # print(i)


