"""Gallery Object."""
import os
from typing import Dict, Any
from .scraper import Scraper
from .saver import Saver


class Gallery(Scraper, Saver):
    """Gallery object."""

    data: Dict[str, Any]

    def __init__(self, folder: str):
        """Init."""
        Scraper.__init__(self, folder)
        self.load()

    def album(self, album_name):
        return self.data.get(album_name, {})

    def list_albums(self):
        return list(self.data.keys())

    def get_media(self, album, name):
        """Return a media."""
        return os.path.join(
            self.folder,
            album,
            name
        )


if __name__ == "__main__":
    gallery = Gallery(folder="../photos")
    gallery.scrap_albums()
    print(gallery.data)
    gallery.scrap_photos("2020-minquiers")
    gallery.save()
