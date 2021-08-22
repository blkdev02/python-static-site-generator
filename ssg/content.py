import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+)"
    __regex = re.compile(__delimeter, re.MULTILINE)