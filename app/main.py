import io, os, base64
from PIL import Image
from typing import List
import time

from .get_songs import get_song
from .config import settings

from fastapi import FastAPI, UploadFile, File, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse, FileResponse, Response


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
base_url = settings.base_url
@app.get('/')
def welcome():

    content="""</br><b>Let's recommend some songs to you but first of all let decide what your mood is</b>"""
    return {'response':'Hi! Welcome to my API'+content}

@app.post("/recommend", response_class=ORJSONResponse)
async def make_recommedation(files: UploadFile= File(...)): 
    if files.content_type != 'image/jpeg':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No image uploaded please upload a jpg image")

    file_path = f"datasets/test/{files.filename}"
    outcome = {"results":None}
    with open(file_path, 'wb+') as imfile:
        imfile.write(files.file.read())
        imfile.close()
    try:
        outcome = get_song()

        file_name = f"static/{str(time.time())}.png"
        Image.open(outcome["image"]).save(file_name)       
        outcome["image"] = f"{base_url}/{file_name}"
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error.args))
    finally:
        if os.path.isfile(f"datasets/test/{files.filename}"):
            os.remove(f"datasets/test/{files.filename}")
        if os.path.isfile(f"trainer/outcome/test/{files.filename.replace('.jpg', '.png').replace('.jpeg', '.png')}"):
            os.remove(f"trainer/outcome/test/{files.filename.replace('.jpg', '.png').replace('.jpeg', '.png')}")  
    return outcome