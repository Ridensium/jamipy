from .component import Component

class Text(Component):
    def __init__(self, text='', roles='text'):
        super().__init__(tag='span', roles=roles)
        self.dom.textContent = text
    @property
    def text(self):
        return self.dom.textContent

    @text.setter
    def text(self, text:str):
       self.dom.textContent = text