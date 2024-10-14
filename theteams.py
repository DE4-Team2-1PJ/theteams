#https://www.theteams.kr/results/recruit?search_query="데이터"
#theteams 채용사이트를 크롤링 해보자

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# 사용자로부터 입력값 받기 (없으면 기본값으로 설정)
search_querys_input = input("검색어를 쉼표로 구분하여 입력하세요 (기본값: 데이터, 백엔드): ")

# 입력값이 비어있으면 기본값 사용
if not search_querys_input:
    search_querys = ['데이터', '백엔드']
else:
    # 입력된 값을 쉼표로 구분하여 리스트로 변환
    search_querys = [query.strip() for query in search_querys_input.split(',')]

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:  
    
    for keword in search_querys:
        print(f"\n kewyord = {keword} \n")
        #이후 keyword가 넘어가면 url 초기화
        url = "https://www.theteams.kr/results/recruit/?search_query={}".format(keword)
        driver.get(url)

        while True:
            # 현재 URL 출력
            print(f"Current URL: {driver.current_url}")
            # 캡션 클래스 내부에 data를 수집
            elements = driver.find_elements(By.CLASS_NAME, "caption")
            for element in driver.find_elements(By.CLASS_NAME, "caption"):
                try:
                    div_element = element.find_element(By.CLASS_NAME, "badge_occupation")
                    h4_element = element.find_element(By.TAG_NAME, "h4")
                    p4_element = element.find_element(By.TAG_NAME, "p")
                    print("Text:", (div_element.text.strip(), h4_element.text.strip(), p4_element.text.strip()))
                except Exception as e:
                    print(f"Error extracting element data: {e}")
            
            # 수집한 후 next_page가 있으면 next_page로 이동
            try:
                page = driver.find_element(By.CLASS_NAME, "pagination")
                li_elements = page.find_elements(By.TAG_NAME, "li")
                
                # 맨 마지막 엘리먼트는 '다음'이어야 함.
                li_element = li_elements[-1]
                if li_element.text.strip() == "다음":
                    print("Moving to the next page...")
                    a_element = li_element.find_element(By.TAG_NAME, "a")
                    a_element.click()  # 다음 페이지 클릭
                    # dom을 다시 reload 하기위해 페이지 새로고침
                    driver.refresh()
                    time.sleep(1) 
                else:
                    # 마지막 페이지일 경우 다음 keyword로 넘어감
                    break
            except Exception as e:
                print(f"Error navigating to next page: {e}")
                break


