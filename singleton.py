from .container import Container, make_dom, Dom


class Singleton(Container):
    _instance = None
    def __new__(cls, roles=None, tag='div', dom=None):
        self = cls._instance
        if self == None:
            print(cls.__qualname__)
            self = super().__new__(cls)
            dom:Dom = make_dom(tag) if dom==None else dom
            if roles:
                dom.className = roles
            self.dom = dom

            cls._instance = self
            self()
        return self


    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self
    
    def __setattr__(self, name, value):
        #super().__setattr__(name, value)
        cls = self.__class__
        setattr(cls, name, value)
        if hasattr(value, 'dom'):
            cls.dom.append(value.dom)


