from fastapi import Depends, APIRouter, status
import sys

from utils.Request import task
from utils.ManageData import InsertData, SelectData
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional

from utils.STATUS_CODE import MODULES_ACCESS

# from fastapi.security import OAuth2PasswordRequestForm

sys.path.append("..")
router = APIRouter(
    prefix="/api",
    tags=["api"],
    # responses={401: {"user": "Not authorized"}},
)

@router.get("/data")
async def GetterDate(query: str = ''):
    # raise MODULES_ACCESS()
    # return 1

    return SelectData(query)

@router.get("/control/{module}")
async def ControlModule(module: str):
    print(module)
    # await task("http://127.0.0.1:8000/api/ㅁㄴㅇㄹ")
    # require error handling
    return '대충 완료했다는 뜻'

class Item(BaseModel):
    water_temp: Optional[float] = -1.0
    ph_state: Optional[float] = -1.0
    water_level: Optional[int] = -1
    led_state: Optional[bool] = False
    last_feed: Optional[bool] = False

@router.post("/data", status_code=status.HTTP_201_CREATED)
def update_item(item: Item):
    print(item)
    # feed -> my request
    # not request -> last last_feed

    # TEMP, PH, WATER_LEVEL, LED, FEED
    InsertData({
        "TEMP": item.water_temp,
        "PH": item.ph_state,
        "WATER_LEVEL": item.water_level,
        "LED": item.led_state,
        "FEED": item.last_feed
    })
    #            시간            온도              ph               물 높이               빛 높이         마지막 먹이  식물 높이 식물 너비
    # InsertData(f'now(), {item.water_temp}, {item.ph_state}, {item.water_level}, {item.light_intensity}, now(), 10, 10')