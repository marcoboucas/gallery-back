"""Back Server."""


from flask_cors import CORS
from .gallery import Gallery

from flask import Flask

STATIC_FOLDER = '/mnt/Disque 1/Photos/'
IP = "192.168.0.54"
PORT = 8000

app = Flask(__name__, static_url_path=STATIC_FOLDER)
CORS(app)


gallery = Gallery('/mnt/Disque 1/Photos/')


@app.route("/")
def read_root():
    return {
        "message": "Welcome to the Gallery App",
        "baseUrl": f"http://{IP}:{PORT}/photos"}


@app.route("/getAlbum/<album_name>")
def read_album(album_name: str):
    return {
        "data": gallery.album(album_name)
    }


@app.route("/getAlbums")
def get_albums():
    return {
        "data": gallery.list_albums()
    }


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
    app.run(
        host="0.0.0.0",
        port=PORT,

    )
