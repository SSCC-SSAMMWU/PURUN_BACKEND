from fastapi import Depends, APIRouter, status
import sys

from utils.Request import task
from utils.ManageData import InsertData, SelectData
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
# from fastapi.security import OAuth2PasswordRequestForm

sys.path.append("..")
router = APIRouter(
    prefix="/api",
    tags=["api"],
    # responses={401: {"user": "Not authorized"}},
)

@router.get("/data")
async def GetterDate(query: str = ''):
    return SelectData(query)

@router.get("/module")
async def ControlModule():
    # 임베디드 통신 선행 필요
    await task("http://127.0.0.1:8000/api/ㅁㄴㅇㄹ")
    # require error handling
    return '대충 완료했다는 뜻'

class Item(BaseModel):
    water_temp: Optional[float]
    ph_state: Optional[float]
    water_level: Optional[int]
    light_intensity: Optional[int]
    last_feed: Optional[bool]

@router.post("/data", status_code=status.HTTP_201_CREATED)
def update_item(item: Item):
    # feed -> my request
    # not request -> last last_feed
    #            시간            온도              ph               물 높이               빛 높이         마지막 먹이  식물 높이 식물 너비
    InsertData(f'now(), {item.water_temp}, {item.ph_state}, {item.water_level}, {item.light_intensity}, now(), 10, 10')