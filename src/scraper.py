"""Scraper of data."""
from typing import Dict, List
import os
from glob import glob


EXTENSIONS = [
    "png", "jpeg", "jpg",
    "mp4", "avi"
]


class Scraper:
    """Scraper object."""

    def __init__(self, folder: str):
        """Init."""
        self.data = {}
        self.folder = folder

    def scrap_albums(self) -> None:
        """Scrap all albums that exists."""
        for element in os.listdir(self.folder):
            path = os.path.join(self.folder, element)
            if os.path.isdir(path):
                if element not in self.data:
                    self.data[element] = {
                        "name": element,
                        "description": "Here is the description",
                        "content": []
                    }

    def scrap_photos(self, album) -> None:
        """Scrap photos for a given album."""
        folder = os.path.join(self.folder, album)
        if os.path.isdir(folder):
            for file_path in glob(os.path.join(folder, "*")):
                self.add_media(album, file_path.split('/')[-1])

    def add_media(self, album, media) -> bool:
        """Add a media to an album."""
        # Check if element is a media
        extension = media.split('.')[-1]
        if extension.lower() not in EXTENSIONS:
            print(f"Not a media file {media}")
            return False

        # Check if album exists
        if album not in self.data:
            return False

        # Check if media not already in album
        list_names = list(
            map(lambda x: x['name'], self.data[album]['content']))
        if media in list_names:
            return False

        # Add the media
        self.data[album]['content'].append({
            "name": media,
            "url": os.path.join(album, media),
            "extension": extension
        })
        return True


if __name__ == "__main__":
    scraper = Scraper(folder="../photos")
    scraper.scrap_albums()
    print(scraper.data)
    scraper.scrap_photos("2020-minquiers")
