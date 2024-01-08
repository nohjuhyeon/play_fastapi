from fastapi import FastAPI     
app = FastAPI()                                                     # fastAPI 연결

from fastapi import Request
from fastapi.templating import Jinja2Templates

from Bask_connection.exam_connection import Settings

settings = Settings()                                              # database 초기화
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="Bask_HTML/")             # template 위치를 Bask_HTML로 지정

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

from Bask_connection.exam_connection import Database                        # Database 연결

from Bask_connection.exam_users import Question # 컬랙션을 연결하고, 컬렉션에 저장/불러오기 하는 방법 

collection_quest = Database(Question)                                      # Question_list에 연결
@app.get("/")
async def root(request:Request):                                                    # bask_exam으로 이동 시 
    # return templates.TemplateResponse("bask_exam.html",{'request':Request})
    print(dict(request._query_params))
    question_list = await collection_quest.get_all()
    return templates.TemplateResponse(name="bask_exam.html"
                                      , context={'request':request
                                                 , 'question_list' :question_list})   

@app.get("/exam")
async def root(request:Request):
    return templates.TemplateResponse("sol_bask_exam.html",{'request':request})

@app.post("/exam")                                                                  # solv_bask_exam으로 이동 시 
async def root(request:Request):
    return templates.TemplateResponse("sol_bask_exam.html",{'request':request})

@app.get("/result")
async def root(request:Request):
    question_list = await collection_quest.get_all()

    return templates.TemplateResponse("bask_player_list.html",{'request':request
                                      , 'question_list' :question_list})

@app.post("/result")                                                                # bask_player_list로 이동 시
async def root(request:Request):
    question_list = await collection_quest.get_all()

    return templates.TemplateResponse("bask_player_list.html",{'request':request
                                      , 'question_list' :question_list})