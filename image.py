from .component import Component

class Image(Component):
    def __init__(self, src='', roles='image'):
        super().__init__(tag='img', roles=roles)
        self.dom.src = src
    @property
    def src(self):
        return self.dom.src

    @src.setter
    def text(self, src:str):
       self.dom.src = src