from selenium import webdriver
from bs4 import BeautifulSoup

# 웹 드라이버 실행
driver = webdriver.Chrome()  # 웹 드라이버의 경로 지정
html = ''
try:
    driver.get("https://petitions.assembly.go.kr/")
    html = driver.page_source
except Exception as e:
    print(e)
finally:
    driver.quit()  # 웹 드라이버 종료

# BeautifulSoup을 사용하여 웹 페이지의 내용 분석
bsObj = BeautifulSoup(html, "html.parser")
sectionTags = bsObj.findAll('section', {'class': 'MaintabSection'})

# 저장소
petition_dic = {}
titleList = []
agreeList = []

# 인기 청원 리스트 가져와서 리스트에 저장
for section in sectionTags:
    titleSection = section.findAll('span', {'class': 'title'})
    agreeSection = section.findAll('li')
    for title in titleSection:
        titleList.append(title.text)
    for agree in agreeSection[3:]:
        agreeList.append(agree.text.replace('\n', '').strip().replace(' '*5, ':'))

# 인기 청원 리스트 출력
print("인기 청원 리스트")
for i in range(len(titleList)):
    petition_dic[titleList[i]] = "%s(%s)" % (agreeList[2*i], agreeList[2*i+1])
    print("%d번 청원은 %s이고 %s입니다." % (i+1, titleList[i], petition_dic[titleList[i]]))
