from typing import List
from pathlib import Path

class Parser:

    extensions: List[str] = []

    def vaild_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest + ext / with_suffix().name




