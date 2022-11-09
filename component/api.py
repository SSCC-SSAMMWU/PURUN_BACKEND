from fastapi import Depends, APIRouter
import sys

from utils.Request import task
from utils.ManageData import InsertData, SelectAllData, SelectSpecialData

sys.path.append("..")
# https://velog.io/@minhyuk_ko/TILFastAPI-%EC%97%B0%EC%8A%B5-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8

# from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    prefix="/api",
    tags=["api"],
    # responses={401: {"user": "Not authorized"}},
)

@router.get("/data")
async def GetterAllDate():
    return SelectAllData()
    # return "hello"

# @router.get("/data/:id")
@router.get("/data2")
async def GetterSpecialData():
    #           날짜     온도    ph    물 높이  빛 높이   마지막 먹이    식물 높이     식물 너비
    InsertData('now(), 10.00, 10.00,   10,     10,     now(),        10,         10')
    return "hello"

@router.get("/module")
async def ControlModule():
    await task("http://127.0.0.1:8000/api/ㅁㄴㅇㄹ")
    # require error handling
    return '대충 완료했다는 뜻'



