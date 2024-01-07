from typing import Optional
from beanie import Document # 문서 형식으로 저장하기 위해 만듦

# 상속을 위한 하나의 클래스를 만듦. collection 지정을 위해

class Question(Document) : # collection에 들어갈 항목 저장. 문제 리스트!
    Question : Optional[str] =None
    option1 : Optional[str] =None
    option2 : Optional[str] =None
    option3 : Optional[str] =None
    option4 : Optional[str] =None
    answer : Optional[str] = None
    score : Optional[str] = None

    class Settings :
        name = "Question_list"

class Player(Document) : # 플레이어와 점수 분포 리스트
    
    #######뭐가 필요할지 잘 모르겠음 ###### 노주노주

    class Settings :
        name = "Player_result"
