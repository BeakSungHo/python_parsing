import sys, io
from requests import get
from random import randint
from bs4 import BeautifulSoup
from konlpy.tag import Okt 
okt = Okt()
hacktableobject ={

}
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

alltable =[]

def crawling() :
    base_url="https://www.wsi.ac.kr/page/meal_list.jsp#self"
    search_team="python"

    response = get(f"{base_url}{search_team}")
    if response.status_code !=200:
        print("can't request website")
    else :
        #//*[@id="tabMenu"]/div/div[1]/div/table/tbody/tr[1]/td[6]/div/text()[1]
        #tabMenu > div > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > div")
        soup = BeautifulSoup(response.text,"html.parser")
        divlist = soup.find_all('table',class_='tbl_skin2 mt20')# <section class: jobs>
        delete_html=['<div>','</div>','</strong>','<strong>','[Plus bar]'
        ,'<th scope="row">','<tbody>','</tbody>','<thead>','</thead>','<colgroup>','</colgroup>',
        '<th scope="col">','<col style=""/>','&amp;','<br/><br/>','<caption>','</caption>','\n',
        '</td>','</tr>','<tr>','</th>','/']
        for div_section in divlist:
            for post in div_section:
                anchors=str(post)   
                anchors = anchors.replace('숭늉','<td>')#.find_all('div')# <a>
                for todo in delete_html:
                    anchors = anchors.replace(todo,'')#.find_all('div')# <a>
                alltable.append(anchors.replace('<br>','%').split('<td>'))
                #print("//////////////////////")
            #print("끝단")
         
               
                # list_of_numbers = [1,2,3]
                # first,second,third=list_of_numbers # 배열의 길이를 알고있으면 다음과같이 가능 
                # print (first,second,third)
        
        #date= alltable[2].split('<td>')
        #print(alltable)
        #print('성공')
        hacktableobject={                   #
            '학생식당(서캠)' : alltable[7], #날짜	소담상	프레시박스	속이찬새참	덮밥	바삭카츠	교직원
            '학생식당(동캠)':alltable[16],  #날짜	한식	푸드코트
            '기숙사(서캠)':alltable[25],    #날짜	조식(서캠)	중식(서캠)	석식(서캠)
            '기숙사(동캠)':alltable[34]     #날짜	조식(동캠)	중식(동캠)	석식(동캠)
        }   
        # for data in hacktableobject.keys():
        #     print(f'{data} :\n {hacktableobject.get(data)}\n\n')
        print(hacktableobject) 
        # print(hacktableobject.get('학생식당(서캠)'),'\n\n',
        #     hacktableobject.get('학생식당(동캠)'),'\n\n',
        #     hacktableobject.get('기숙사(서캠)'),'\n\n',
        #     hacktableobject.get('기숙사(동캠)'),'\n\n')


crawling()
