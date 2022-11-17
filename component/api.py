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
    TEMP: Optional[float]
    PH: Optional[float]
    WATER_LEVEL: Optional[int]
    LED: Optional[bool]
    FEED: Optional[bool]
@router.post("/data", status_code=status.HTTP_201_CREATED)
def update_item(item: Item):
    # item = {
    #     "TEMP": round(item.TEMP, 2) if item.TEMP else None,
    #     "PH": round(item.PH, 2) if item.PH else None,
    # }
    print(item)
    # InsertData(item)