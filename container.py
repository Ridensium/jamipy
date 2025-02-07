from .component import Component, make_dom, Dom

class Container(Component):


    def __init__(self, roles=None, tag='div', dom=None, *args, **kwargs):
        super().__init__(roles=roles, tag=tag, dom=dom)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if hasattr(value, 'dom'):
            self.dom.append(value.dom)



    def __iadd__(self, child:Component): # self += child
        self.dom.innerHTML = ''
        self.dom.append(child.dom)
        return self
    
    def __isub__(self, child:Component=None): # # self -= child
        if child:
            child.dom.remove()
        else:
            self.dom.innerHTML = ''
        return self
    
    def __rshift__(self, child:Component): # self >> child
        self.dom.append(child.dom)
        return self
    
    def __lshift__(self, child:Component): # parent << child
        self.dom.prepend(child.dom)
        return self


    def append_dom(self, child:Component|Dom):
        dom:Dom = child if isinstance(child, Dom) else child.dom
        self.dom.append(dom)
        
    def prepend_dom(self, child:Component|Dom):
        dom:Dom = child if isinstance(child, Dom) else child.dom
        self.dom.prepend(dom)


    def remove_dom(self, child:Component|Dom):
        dom:Dom = child if isinstance(child, Dom) else child.dom
        dom.remove()

    def add_child(self, child:Component, name=None, append=False, prepend=False, only=False):
        if name:
            object.__setattr__(self, name, child)
        if append==True:
            self >> child
        if prepend == True:
            self << child
        if only == True:
            self += child


    @property
    def children_dom(self)->list[Dom]:
        return list(self.dom.children)