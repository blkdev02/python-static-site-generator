from typing import List
from pathlib import Path

class Parser:

    extensions: List[str] = []

    def vaild_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False