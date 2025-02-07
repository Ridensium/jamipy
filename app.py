from .component import WINDOW
from .container import Container
from .browser import Body, Singleton




class App(Singleton):
    navigation:Container
    content:Container
    def __new__(cls, content=None, navbar=None):
        self = super().__new__(roles='app')
        if navbar:
            navbar()
        if content:
            content()
        
        return self
    def __call__(self):

        if WINDOW.matchMedia('(pointer: coarse)').matches:
            touch = True
        elif WINDOW.matchMedia('(hover: none)').matches:
            touch = True
        else:
            touch = False

        self.touch:bool = touch
        self.roles.add('touch' if touch == True else 'no-touch')


        self.navigation = Container(roles='app-navigation')
        self.content = Container(roles='app-content')
        self.modal = Container(roles='app-modal')




        body = Body()
        body >> self


class Page(Singleton):
    def __new__(cls, link=None, *args, **kwars):
        self:Page = super().__new__(roles='page')
        App.content += self
        return self
    


class Navbar(Singleton):
    def __new__(cls):
        self:Navbar = super().__new__(roles='navbar')
        App.navigation += self
        return self
    

class Modal(Singleton):
    def __new__(cls, link=None):
        self = super().__new__(roles='modal')
        App.modal += self
        return self