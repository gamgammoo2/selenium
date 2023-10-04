# import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# service = ChromeService(ChromeDriverManager().install())
# with Chrome(options=options, service=service) as driver:
# print(service.path) # this is where the driver is located
# Github credentials
username = ""
password = ""

# initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# head to github login page
driver.get("http://kibwagg.org/uat/uia/egovLoginUsr.do")
# find username/email field and send the username itself to the input field
driver.find_element("id", "idText").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "passwordText").send_keys(password)
# click login button
# wait = WebDriverWait(driver, 1)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '로그인')]"))).click()
driver.find_element(By.XPATH,"//*[@id='wrap']/article/form/section/dl/dd[3]/a").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# error_message = "Incorrect username or password."
# # get the errors (if there are)
# errors = driver.find_elements("css selector", ".flash-error")
# # print the errors optionally
# # for e in errors:
# #     print(e.text)
# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")

# wait = WebDriverWait(driver, 1)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '로그인')]"))).click()



driver.find_element(By.XPATH,"//*[@id='mainHeader']/nav/img[2]").click()
WebDriverWait(driver, 1)
driver.find_element(By.XPATH,"//*[@id='mainHeader']/nav/div[1]/ul/li[5]/a").click()
WebDriverWait(driver, 2)

#팀블로그 들어가기 

driver.find_element(By.XPATH,"//*[@id='publicBoardList']/table/tbody/tr/td[4]/button").click()
WebDriverWait(driver, 2)

# 퇴실체크
driver.find_element(By.XPATH,"//*[@id='wrap']/article/section/ul/li[3]/div/article/div[2]/button[2]").click()
WebDriverWait(driver, 2)

#경고창 내용 얻기 - https://liveyourit.tistory.com/38

try:
    result=driver.switch_to_alert()
    #alert내용
    print(result.text)
except:
    "There is no alert"

driver.close()



