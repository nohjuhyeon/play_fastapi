from typing import Optional,List
from beanie import Document # 문서 형식으로 저장하기 위해 만듦

# 상속을 위한 하나의 클래스를 만듦. collection 지정을 위해

class Question(Document) :                          # collection에 들어갈 항목 저장. 문제 리스트!
    question : Optional[str] =None
    options1 : Optional[str] =None
    options2 : Optional[str] =None
    options3 : Optional[str] =None
    options4 : Optional[str] =None
    answer : Optional[str] = None
    points : Optional[int] = None

    class Settings :
        name = "Question_list"

class Player(Document) : # 플레이어와 점수 분포 리스트

    plyaer_name : Optional[str] =None
    answer1 : Optional[str] =None
    answer2 : Optional[str] =None
    answer3 : Optional[str] =None
    answer4 : Optional[str] =None
    player_score : Optional[int] =None

    class Settings :
        name = "Player_result"
