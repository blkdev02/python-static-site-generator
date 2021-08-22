import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+)"
    __regex = re.compile(__delimiter, re.MULTILINE)