# from requests import get
# from random import randint
# from bs4 import BeautifulSoup

# def one_Test():
#     def first_text(user_text="typing!"):
#         return user_text
#     def 뀨_text(user_text="typing!"):
#         say_bye(user_text)
#     def say_bye(user_text="do not typing?"): #입력안할경우의 기본값을 설정 (생성자 느낌?)
#         print("ggume : "+user_text)
        
#     my_text = "dsd"
#     say_bye(first_text("YES~"))
#     뀨_text("??")

#     print(f"aha {my_text} ")#f는 포멧을 나타냄
#     a= 4
#     if a>5:
#         print ("Correct!")
#     elif a == 4:
#         print ("a :",a)
#     else :
#         print("Fair")

#     quetion=input("u know?\n")
#     print(type(quetion))
#     age=int(input("what my age?\n"))
#     if age>18:
#         print ('my age... u did say to low')
#     elif age<18:
#         print('my age... u did say to high')
#     else :
#         print (f'my age so {age}')
#     pc_choice = randint(1,50)#렌덤 숫자
#     print (pc_choice)


# def Test2() :
#     distance =0
#     while distance<=20:
#         print("I'm running : ",distance,"km")
#         distance=distance+1
# def Test3():
#     week=["Mon",'Tur','Wed','Thor','Fri']
#     name = "나는 nico"
#     week.remove("Mon")
#     week.append("M")
#     print(week)
#     print(name.find('ㅇ'))#endswith은 끝나는 값을 비교?
#     palyer ={
#         'name':'nico',
#         'age':12,
#         'alive':True,
#         'fav_food':('ㅇㅅㅇ','\'ㅇ\'')
#     }
# def Test4():
#     websites= ('google.com','airbnb.com','twitter.com','facebook.com','tiktok.com')

#     results={}

#     for website in websites:
#         if not website.startswith("https://"):
#             website = f"https://{website}"
#         response = get(website)
#         if response.status_code==200:
#             results[website]='OK'
#             print(website)
#             response = get(website)
#             print (response)
#         else: 
#             results[website]='FAILED'
#         print (results)

# def test4() :
#     base_url="https://weworkremotely.com/remote-jobs/search?=✓&term="
#     search_team="python"

#     response = get(f"{base_url}{search_team}")
#     if response.status_code !=200:
#         print("can't request website")
#     else :
#         soup = BeautifulSoup(response.text,"html.parser")
#         jobs = soup.find_all('section',class_='jobs')# <section class: jobs>
#         for job_section in jobs:
#             job_posts = job_section.find_all('li') #<li>
#             job_posts.pop(-1)#li class : viewall을 삭제하기위해서 실행 
#             for post in job_posts:
#                 anchors = post.find_all('a')# <a>
#                 anchor = anchors[1]
#                 link=anchor['href']#anchor내의 href를 출력 파이선은 크롤링시 파이썬 다큐먼트리로 포멧됨으로 값으로 가져오는것이 가능
#                 company,kind,reion = anchor.find_all('span',class_='company')
#                 title = anchor.find('span',class_='title')
#                 print("\n#",company,"\n#",kind,"\n#",reion,"\n#",title)
#                 print("//////////////////////")
               
               
#                 # list_of_numbers = [1,2,3]
#                 # first,second,third=list_of_numbers # 배열의 길이를 알고있으면 다음과같이 가능 
#                 # print (first,second,third)
# test4()
import base64
text = str("히잉")

print(base64.b64encode(text.encode('utf-8')))