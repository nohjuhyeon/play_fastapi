from fastapi import FastAPI
app = FastAPI()

from fastapi import Request
from fastapi.templating import Jinja2Templates



# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="Bask_HTML/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root(Request:Request):
    return templates.TemplateResponse("bask_exam.html",{'request':Request})

@app.post("/")
async def root(Request:Request):
    return templates.TemplateResponse("bask_exam.html",{'request':Request})

@app.get("/exam")
async def root(Request:Request):
    return templates.TemplateResponse("sol_bask_exam.html",{'request':Request})

@app.post("/exam")
async def root(Request:Request):
    return templates.TemplateResponse("sol_bask_exam.html",{'request':Request})

@app.get("/result")
async def root(Request:Request):
    return templates.TemplateResponse("bask_player_list.html",{'request':Request})

@app.post("/result")
async def root(Request:Request):
    return templates.TemplateResponse("bask_player_list.html",{'request':Request})
