from .constructors import Container, Component, Element

#for allowed when doin eval
from .label import Label
from .spacer import Spacer
from .pill import Pill
from .link import Link
from .image import Image
from .drop_down import DropDown
from .checkers import RadioButton, RadioGroup, CheckBox


class Wiki(Label):
    on_click = None
    no_ext_class = Label
    no_ext_path = '/'

    image_class = Image
    img_path = '/'
    img_ext = None

    _img_extentions = {'jpg', 'jpeg', 'bmp', 'png', 'webp', 'svg'}


    def __new__(cls, text = '', icon = None, wiki=None, show=False):
        if show:
            instance = cls.show_wiki(text=text, icon=icon, wiki=wiki)
        else:
            instance = super().__new__(cls)
        return instance

    def __init__(self, text = '', icon = None, wiki=None, show=None):
        super().__init__(text, icon)
        if self.on_click:
            self.add_event_handler('click', self.on_click)
        self.wiki = wiki

    def on_click(self, event=None):
        pass

    @classmethod
    def show_wiki(cls, text:str, icon:str, wiki:str):

        wiki_parts = wiki.split('.')

        if len(wiki_parts) == 1:

            return cls.no_ext_class(text=text, icon=icon, wiki=wiki)
        
        elif wiki_parts[1] in cls._img_extentions:

            name = wiki_parts[0]

            img_ext = cls.img_ext

            file_name = f'{name}.{img_ext}' if img_ext else wiki

            img = cls.image_class(f'{cls.img_path}/{file_name}')

            return img



class Hashtag(Label):

    on_click = None

    def __init__(self, text = '', icon = None):
        super().__init__(text, icon)
        if self.on_click:
            self.add_event_handler('click', self.on_click)
        self.tag = text
   




class ContainerHtml(Container):
    _allowed:dict[str,type] = {v.__qualname__:v for v in [Label, DropDown, Link, Spacer, Pill, Image, RadioButton, RadioGroup, CheckBox, Wiki, Hashtag]}
    _html:str = ''
    def __init__(self, html:str='', slots:list[type]=None, roles='container container-html'):

        super().__init__(roles=roles)

        if slots:
            self._allowed = {v.__qualname__:v for v in slots}

        if html:
            self._html = html
            self._build(html)



    @property
    def html(self):
        return self._html
    
    @html.setter
    def html(self, value:str):

        self._build(value)


    def _build(self, html:str):
        allowed = self._allowed
        
        temp_el:Element = self._el.cloneNode()

        temp_el.innerHTML = html

        temp_children:set[Component] = set()

        widgets_el:list[Element] = temp_el.querySelectorAll('widget')


        for w_el in widgets_el:

            child_class = w_el.getAttribute('component')

            if not child_class in allowed:
                continue

            init = w_el.getAttribute('init')

            child:Component = eval(f'{child_class}({init})', allowed)
         
            w_el.replaceWith(child._el)

            temp_children.add(child)


        self.clear()

        self._el.replaceWith(temp_el)

        self._el = temp_el

        self._children = temp_children

        self._html = html



      

