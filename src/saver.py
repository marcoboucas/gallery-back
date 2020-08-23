"""Saver file."""

import json
import os


class Saver:
    """Handle saving the data."""

    data: dict
    folder: str

    def save(self):
        """Save the data."""
        with open(os.path.join(self.folder, "gallery.json"), "w") as file:
            json.dump(self.data, file, indent=4)

    def load(self):
        """Load the data."""
        path = os.path.join(self.folder, "gallery.json")
        if os.path.isfile(path):
            with open(path, 'r') as file:
                self.data = json.load(file)
