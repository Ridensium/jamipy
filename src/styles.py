from js import document, Element, CSSStyleSheet
from .constructors import make_el


class Style:
    sheet:CSSStyleSheet = None
    id:str = None

    def __init__(self, id=None, css:str='', url:str='', parent=None):

        if url:
            el:Element = make_el('link')
            el.rel = 'stylesheet'
            el.href = url
        else:
            el:Element = make_el('style')
            el.innerHTML = css


        if id:
            el.id = id
            self.id = id
     
        self._el:Element = el
   
        if parent:
            self.append_to_element(parent)
    
    def append_to_element(self, parent:Element=None):
        parent = parent if parent else document.head
        id = self.id
        if id:
            el:Element = document.getElementById(id)
            if el:
                self._el = el
            else:
                parent.append(self._el)
        else:
            parent.append(self._el)

        self.sheet = self._el.sheet




class Role:
    roles:dict = {}
    index:int
    data:dict
    name:str
    _sheet:CSSStyleSheet = None
    
    def __new__(cls, role_name:str, **kwargs):
        if not cls._sheet:
            style = Style('jamipy-roles')
            style.append_to_element()
            cls._sheet = style.sheet

        self = cls.roles.get(role_name, None)

        if not self:
            self = super().__new__(cls)
            self.name = role_name
            self.index = None
            self.data = {}
            if kwargs:
                self.set_style(**kwargs)

            cls.roles[role_name] = self
        
        return self
    
    def __init__(self, role_name:str, **kwargs):
        if kwargs:
            self.set_style(**kwargs)

    def __call__(self, *args, **kwds):
        return self.name


    def __str__(self):
        return f'{self.name} - {self.data}'
    

    def set_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
        

        data:dict = {
            'font-weight': font_weight if bold == None else f"{'bold' if bold == True else ''}",
            'color': color,
            'width': width if isinstance(width, str) else f'{width + "px" if width else ''}',
            'height': height if isinstance(height, str) else f'{height + "px" if height else ''}',
            'font_family':font,
            'font-size':f'{font_size}px' if isinstance(font_size, int) else font_size,
            'title':tooltip,
            'background-color':background,
            'font-style':italic,
            'text-align':text_align,
            'border' : f'{border}px solid' if isinstance(border, int) else border
            }
        data = {k:v for k,v in data.items() if v}
        for k, v in kwargs.items():
            data[k]=v
        
        self.data = data
        
        self.update_style()

        return self
    

    def update_style(self):
        sheet = self._sheet
        data = self.data
        css:str = ''
        for key, value in data.items():
            css += f'{key}:{value};'

        rule:str = f'.{self.name} {{ {css} }}'
        indexes = sheet.cssRules.length
     
        new_index = sheet.insertRule(rule, indexes)

        index = self.index
        
        if index or index == 0:

            sheet.deleteRule(index)
            self.index = new_index - 1
        else:
  
            self.index = new_index

    def add_style(self, key:str, value:str):
        self.data[key] = value
        self.update_style()
        return self

    def remove_style(self, key:str):
        self.data.pop(key, None)

        self.update_style()

        return self
    

    def clear(self):
        index = self.index
        sheet = self._sheet
        if index and sheet:
            sheet.deleteRule(index)

        return self