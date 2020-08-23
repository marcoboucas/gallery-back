"""Back Server."""

import uvicorn

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from .gallery import Gallery
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

gallery = Gallery('../photos')

origins = [
    "http://192.168.0.53:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Gallery App",
        "baseUrl": "http://192.168.0.53:8000/photos"}


@app.get("/getAlbum/{album_name}")
def read_album(album_name: str):
    return {
        "data": gallery.album(album_name)
    }


@app.get("/getAlbums")
def get_albums():
    return {
        "data": gallery.list_albums()
    }


app.mount("/getMedia", StaticFiles(directory="../photos"), name="static")
"""
@app.get("/getMedia/{album}/{media}")
async def get_media(album: str, media: str):
    extension = media.split('.')[-1].lower()
    file_path = gallery.get_media(album, media)
    if extension in ['mp4']:
        file_like = open(file_path, mode="rb")
        return StreamingResponse(file_like, media_type="video/mp4")
    return FileResponse(file_path)

"""


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="192.168.0.54",
        port=8000,
        log_level="info"
    )
