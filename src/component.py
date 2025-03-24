"""
module with the super class `Component` used for all widgets
can be used as well to build custom widgets
`js.Element` and `js.DOMTokenList` are imported **only** for typing autosuggestions.
"""

from js import document, Element, DOMTokenList
from .m_enums import *

#shortcut to the js method
create_el = document.createElement

def el_from_template(template:dict=None)->Element:
    """
    non-publick fn for making elements from template like:

```json

{
'tag_name':  'div',
'roles':'label',
'children': []
}

```

useful for widgets with compund html to make copie from template instead making and nesting new one
    """

    el:Element = create_el(template['tag_name'])
    el.className = template['roles']
    children:dict = template.get('children', [])

    for child in children:
        el_child:Element = el_from_template(child)
        el.append(el_child)
    return el


class Component:
    """
    publick class for the common for all other constructors and widget classes
    can be used for building custom widggets
    `Component._el` wraps the html element for the widget
    """
    _el:Element = None


    def __init__(self, tag_name='div', roles:str=None):
        """
        makes widget with element by default div
        if provided roles adds them
        """

        self._el:Element = create_el(tag_name)
        if roles:
            self.roles = roles



    def set_parent(self, parent:'Component', at_begining=False):
        """adding widget to parent one"""
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)


    def remove(self):
        """removing widget from its parent"""
        self._el.remove()


    def set_event_handler(self, event_name:str, handler)->None:
        """
        ading event handler for the widget, the handler will receive as first argument the event object
        example:

```python

def fn(event=None)
def fn(self, event=None)
def fn(*args)

widget.set_event_handler('click', fn)

```
        """
        setattr(self._el, f'on{event_name}', handler)


    def get_event_handler(self, event_name):
        """sometimes we may need to know what was the handler we set above"""
        return getattr(self._el, f'on{event_name}', None)


    def style(self, border:str=None, text_align:str=None, tooltip:str=None, font:str=None, font_size:str|int=None, font_weight:int=None, color:str=None, background:str=None, bold:bool=None, width:str|int=None, height:str|int=None, italic:bool=None, **kwargs):
        """
        its recommended to use classes for styling html instead inline css
        but with this method you can add inline styles to the widget
        for better performace if adding multipe add them together to reflow the element once
        apart from optional parameters you can provide css keywords with underscore instead dash
        values if should be provided in css example:
        `widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
        `border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
        keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
        it adds the styles doesnt clean all old ones
        """
        style = self._el.style
        
        css = {
            'font-weight': font_weight if bold == None else f"{'bold' if bold == True else 'unset'}",
            'color': color,
            'width': width if isinstance(width, str) else f'{width}px',
            'height': height if isinstance(height, str) else f'{height}px',
            'font_family':font,
            'font-size':font_size,
            'title':tooltip,
            'background-color':background,
            'font-style':italic,
            'text-align':text_align,
            'border' : f'{border}px solid' if isinstance(border, int) else border

        }
   
        for k,v in kwargs.items():
            css[k.replace('_', '-')] = v
        
        print(css)
        style.cssText += ';'.join([f'{k}:{v}' for k,v in css.items() if v!=None])
        return self

    def get_style(self, name=None)->dict:
        """gets all if `name=None` or specific inline style/styles"""
        styles:str = self.el.style.cssText
        styles = styles.split(';')
        result = {}
        for style in styles:
            style = style.split(':')
            result[style[0]] = style[1]

        return result if name == None else result.get(name, {})


    @property
    def visible(self)->bool:
        """
        returns visibility value
        True - widget is alowed to be visible
        False - widget is hidden even if its parent is visible in the viewport
        """
        return self.role.contains('hidden')


    @visible.setter
    def visible(self, value:bool):
        """
        setting the visibility
        under the hood it adds/removes the css class *hidden*
        whinch makes `display:none` if is `False`
        """
        if value == False:
            self.role.add('hidden')
        else:
            self.role.remove('hidden')
    

    @property
    def roles(self)->list:
        """
        roles and role above are wrappers of the css classes of the widget
        this property returns the current roles as a list
        """
        return list(self._el.classList)
        

    @roles.setter
    def roles(self, roles:str|list|set):
        """
        setting the roles from string, list or set
        this will **remove** all older ones
        for partial add/delete use *role* below
        """
        _roles = roles if isinstance(roles, str) else ' '.join(roles)
        self._el.className = _roles


    @property
    def role(self)->DOMTokenList:
        """
        returns a object of the widget roles/classes on which we have those methods:
        `.add(value:str)` - adds one
        `.remove(value:str)` - removes one
        `.replace(old:str, new:str)` - replaces one with another
        `.toggle(value:str)` - if not present will add else remove 
        `.contains(value:str)` - return True if present
        """
        return self._el.classList
        

    @property
    def get_size(self)->tuple:
        """
        returns tuple with width and height of the calculated by the browser values
        keep in mind even if we set some values the browser may recalculate them with some tolerance
        some styles like borders got impact too
        """
        rect = self._el.getBoundingClientRect()
        return (rect.width, rect.height)


    def display(self, parent_el=document.body):
        """
        appends the widget to html element in `parent_el`,
        which default value is the webpage body
        """
        parent_el.append(self._el)
        return self

