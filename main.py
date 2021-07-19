# selenium으로 instagram열기

from selenium import webdriver
import time, random
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint


random_wait_min = 5
random_wait_max = 9

random_next_min = 4
random_next_max = 9

comment_list = ['좋은 사진 잘보고 갑니다~~~ 소통해요', '피드 잘 구경하고 갑니다. 소통해요~!!',
                '너무 너무 반가워요!♥ 우리 소통해요 ₍₍ (ง ˙ω˙)ว ⁾',
                '♥ 자주소통해용 ♥ ', '소통하고 싶어 댓글답니다 ^^ ',
                '소통하고 싶어 댓글 남겨요~ ', '잘 보고 갑니다~ 찐소통해요오:)', '소통자주해요 ㅎㅎ',
                '피드 구경하고 갑니다~ 소통해요', '저희 언팔없는 소통해요~~♥', '피드 보고 너무 맘에 들어서 댓글 남겨요~ 소통해요 ㅎㅎ']

options = webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")

browser = webdriver.Chrome("../../chrome/chromedriver90.exe")

url_login = "https://www.instagram.com/accounts/login/?source=auth_switcher"
browser.get(url_login)

time.sleep(3)
#browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("mayseven.ceo")
#browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("ttobaki93!")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("mayseven.shop")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("mayseven57!")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

# search
time.sleep(2)
url_base = 'https://www.instagram.com/explore/tags/'
url_tag = input('검색할 태그를 입력하세요: ')
url = url_base + quote_plus(url_tag)
browser.get(url)
time.sleep(2)

# 최근 게시물 선택하기
time.sleep(5)
feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
feed.click()

#다음 게시물 이동하기 함수
def nextFeed():
     time.sleep(3)
     nextFeed = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
     nextFeed.click()

like_count = 0

for a in range(500):
    # 좋아요 누르기
    time.sleep((randint(random_wait_min, random_wait_max)))
    try:
        like_list = browser.find_elements_by_xpath('//article//section/span/button')
        likeBtnTxt = browser.find_elements_by_class_name('_8-yf5 ')
        if likeBtnTxt[5].get_attribute("aria-label") != '좋아요':
            like_list[0].click()  # list 중 0번째 버튼을 선택
            like_count += 1
            print("like count = ", like_count)
        else:
            print(likeBtnTxt[5].get_attribute("aria-label"), "Pass 좋아요")
    except:
        print("exception!")
        continue



    # 다음 피드로 이동하기
    for b in range(randint(random_next_min, random_next_max)):
        nextFeed()



