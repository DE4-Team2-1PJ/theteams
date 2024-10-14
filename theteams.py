#https://www.theteams.kr/results/recruit?search_query="데이터"
#theteams 채용사이트를 크롤링 해보자

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#EC_wait을 위한 import 모듈
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    #https://www.theteams.kr/results/recruit/10?search_query=데이터
    #"https://hashcode.co.kr/?page={}".format(i)
    
    #다음이라는 엘리먼트가 있으면 다음페이지가 있는거임.
    # page = driver.find_element(By.CLASS_NAME, "pagination")
    # li_elements = page.find_elements(By.TAG_NAME, "li")
    # page_num = int(li_elements[len(li_elements)-2])
    # print(page_num)
    
    search_querys = [
        '데이터', '백엔드'
    ]
    for keword in search_querys:
        print(f"kewyord = {keword}")
        for i in range(1, 3):
            url = "https://www.theteams.kr/results/recruit/{}?search_query={}".format(i, keword)
            driver.get(url)

            # 캡션 클래스 내부의 a 태그 아래 h4 태그의 텍스트를 출력
            for element in driver.find_elements(By.CLASS_NAME, "caption"):
                div_element = element.find_element(By.CLASS_NAME, "badge_occupation")
                h4_element = element.find_element(By.TAG_NAME, "h4")
                p4_element = element.find_element(By.TAG_NAME, "p")
                print("Text:", (div_element.text, h4_element.text, p4_element.text))