import json

from fastapi import FastAPI, File, UploadFile
from time import time
import httpx
import asyncio

app = FastAPI()

# get list of data from db
# /date/ => special data
@app.get('/api/data')
### front to arduino / raspberry pi
@app.get('/api/feed')
@app.get('/api/pump')
@app.get('/api/led')
# create data to db
@app.post('/api/data')

@app.get('/api/')
async def getData():
    return json.dumps(f"""
    {
    'hello': 1
    }
    """)




@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# https://cocosy.tistory.com/65
# URL = "http://127.0.0.1:8000/api/test/"

URL = "http://httpbin.org/uuid"

async def request(client):
    response = await client.get(URL)
    return response.text

async def task():
    async with httpx.AsyncClient() as client:
        tasks = [request(client) for i in range(100)]
        result = await asyncio.gather(*tasks)
        print(result)

@app.get('/api/testiiing')
async def f():
    start = time()
    await task()
    print("time: ", time() - start)

# @app.post("/photo")
# async def upload_photo(file: UploadFile):
#     UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로
#     content = await file.read()
#     filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
#     with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
#         fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)
#     return {"filename": filename}