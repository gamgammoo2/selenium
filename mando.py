# import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import schedule
import time

import datetime

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeService, ChromeOptions

options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--single-process")
options.add_argument("--disable-dev-shm-usage")

# def mandoevent():
username = ""
phone = ""

import random

challenges = ["가족행복", "취업성공", "부모님효도", "할머니찾아뵙기", "행복하기", "동생이랑여행", "가족여행", "살빼기"]
challenge = random.choice(challenges)

# initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# head to github login page
driver.get("https://doanddo.hlcompany.com/")


# 참가 버튼 누르기
driver.find_element(By.XPATH,"//*[@id='main-event02']/div[1]/div/p/button").click()
WebDriverWait(driver, 5)


# 동의합니다
driver.find_element(By.XPATH,"//*[@id='event02-modal']/div[2]/div/div[1]/div[1]/div[2]/label[1]/input").click()
WebDriverWait(driver, 5)

# 확인했습니다.
driver.find_element(By.XPATH,"//*[@id='event02-modal']/div[2]/div/div[1]/div[2]/div[2]/label/input").click()
WebDriverWait(driver, 5)

# 이름 입력
driver.find_element("name", "user_name").send_keys(username)
WebDriverWait(driver, 5)
# 폰번호 입력
driver.find_element("name", "user_phone").send_keys(phone)
WebDriverWait(driver, 5)

#다음버튼
driver.find_element(By.XPATH,"//*[@id='event02-modal']/div[2]/div/div[1]/p/button").click()
WebDriverWait(driver, 5)

#빈칸 입력
driver.find_element("name", "user_challenge").send_keys(challenge)
WebDriverWait(driver, 5)

#당첨확인하기 버튼
driver.find_element(By.XPATH,"//*[@id='event02-modal2']/div[2]/div/div[1]/p/button").click()
WebDriverWait(driver, 5)

try:
    result=driver.find_element(By.XPATH,"//*[@id='event02-modal-result']/div[2]/div/div[1]/div[1]/div[3]/div")
    expected_result = driver.find_element(By.XPATH, "//*[@id='event02-modal-result']/div[2]/div/div[1]/div[1]/div[3]/div")

    if result.text == expected_result.text:
        driver.find_element(By.XPATH,"//*[@id='event02-modal-result']/div[2]/div/div[1]/div[1]/div[3]/p/button").click()
        #alert내용
        print("success airpod")
except:
    print("fail")

driver.close()
    
#     now = datetime.datetime.now()
#     print("test code- 현재 시간 출력하기")
#     print(now)

# mandoevent()
    
# schedule.every(1).day.at("04:17").do(mandoevent)
# schedule.every(1).day.at("04:18").do(mandoevent)
# schedule.every(1).day.at("04:19").do(mandoevent)
# schedule.every(1).day.at("04:20").do(mandoevent)
# schedule.every(1).day.at("04:21").do(mandoevent)
# schedule.every(1).day.at("04:22").do(mandoevent)
# schedule.every(1).day.at("04:23").do(mandoevent)
# schedule.every(1).day.at("04:24").do(mandoevent)
# schedule.every(1).day.at("04:25").do(mandoevent)
# schedule.every(1).day.at("04:26").do(mandoevent)
# schedule.every(1).day.at("04:27").do(mandoevent)
# schedule.every(1).day.at("04:28").do(mandoevent)
# schedule.every(1).day.at("04:29").do(mandoevent)
# schedule.every(1).day.at("04:30").do(mandoevent)
# schedule.every(1).day.at("04:31").do(mandoevent)
# schedule.every(1).day.at("04:32").do(mandoevent)
# schedule.every(1).day.at("04:33").do(mandoevent)

# #무한 루프를 돌면서 스케쥴을 유지한다.
# while True:
#     schedule.run_pending()
#     time.sleep(1)