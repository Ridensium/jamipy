from .component import DOCUMENT
from .singleton import Singleton

class Body(Singleton):
    def __new__(cls, roles='body'):
        return super().__new__(dom=DOCUMENT.body, roles=roles)

