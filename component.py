from js import document, window
from .typing import Dom, classList, Window, Document

WINDOW:Window = window
DOCUMENT:Document = document
make_dom = DOCUMENT.createElement

class Component:
    dom:Dom
    roles:classList
    width:int
    height:int

    def __init__(self, tag:str='div', roles:str=None, dom:Dom=None, *args, **kwargs):
        dom:Dom = make_dom(tag) if dom==None else dom
        dom.className = roles if roles else self.__qualname__
        self.dom:Dom = dom

    def remove(self):
        self.dom.remove()

    @property
    def roles(self)->classList:
        return self.dom.classList
    
    @property
    def get_roles(self)->list:
        return list(self.dom.classList)
    
    @roles.setter
    def roles(self, roles:str):
        self.dom.className = roles

    @property
    def width(self)->int:
        return self.dom.offsetWidth
    @property
    def height(self)->int:
        return self.dom.offsetHeight