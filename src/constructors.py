"""
Component and Container widgets

all the widgets are based on these both, and you can use them as well
by their own or to build custom widgets

`Component` is the base one, `Container` is based on it adding methods
for acting as parenting widget

`js.Element` and `js.DOMTokenList` are imported **only** for typing autosuggestions.
"""

from js import document, Element, DOMTokenList
from .m_enums import *
from pyscript import config



# interpretor dependsies
INTERPRETOR = config['type']
if INTERPRETOR == 'mpy':
    pass
else:
    from pyscript.ffi import create_proxy



#shortcut to the js method
make_el = document.createElement


#micropython event handlers
def add_event_handler_mpy(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, handler)
#pyodide event handlers
def add_event_handler_py(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, create_proxy(handler))


# event handlers by interpretor
if INTERPRETOR == 'mpy':
    _add_event_handler = add_event_handler_mpy
else:
    _add_event_handler = add_event_handler_py


def make_el_template(template:dict)->'Element':
    """
    returns element from made from template like:

    ```json

    {
        "tag_name":  "div",
        "roles":"label",
        "children": []
    }

    ```

    """

    el:Element = make_el(template['tag_name'])
    el.className = template['roles']
    children:dict = template.get('children', [])

    for child in children:
        el_child:Element = make_el_template(child)
        el.append(el_child)
    return el


class Component:
    """
    Component widget class
    provides common for all other widget classes methods
    can be used by itself, as well for building custom widggets
    """
    _el:Element = None
    _parent:'Container' = None

    def __init__(self, tag_name='div', roles:str|list|set = None):
        """
        `tag_name` - tag name for the coresponding element, by default `div`
        `roles` - string with delimeter space, list or set for the roles
        of that widget wich are representing css classes as well
        """

        self._el:Element = make_el(tag_name)

        if roles:
            self.roles = roles


    @property
    def parent(self)->'Container':
        """return parent widget if so or None"""
        return self._parent

    @parent.setter
    def parent(self, parent:'Container'=None):
        """seting parent for widget"""
        # if provided parent will ask parent to append
        if parent:
            parent.append(self)

        # if not parent but has old one will ask old one to remove
        elif self._parent:
            self._parent.remove(self)



    def add_event_handler(self, event_name:str, handler=None)->None:
        """
        ading event handler to the widget `click`, `keyup` and so on
        the handler always will receive an event object as first argument
        in jamipy the naming of the handlers looks like `on_eventname`
        
        if provided only event_name but not handler will try
        to get method from the widget class by this naming convention

        ```python

        def on_click(event=None)
                print('Click 1')

        class Widget:
            def on_click(event=None)
                print('Click 2')

        #result on click >>> 'Clic 1'
        w1 = Widget().add_event_handler('click', on_click)

        #result on click >>> 'Clic 2'
        w2 = Widget().add_event_handler('click')

        ```
        
        """

        handler = handler if handler else getattr(self, f'on_{event_name}', None)

        if handler:
            _add_event_handler(self, event_name, handler)
       
        return self


    def remove_event_handler(self, event_name:str=None,
                             handler=None, remove_all=False):
        """remove selected or all event handlers
        > [!CAUTION]
        removing **all** handlers may break functionality,
        in some elements like `CheckBox` for example
        """
        el = self._el

        #remove the givven one
        if event_name and handler:
            if INTERPRETOR == 'py':
                handler = create_proxy(handler)
            el.removeEventListener(event_name, handler)

        #remove them all
        elif remove_all:
            new_el = el.cloneNode(True)
            el.replaceWith(new_el)


    def add_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
        """
        ading inline styles to the widget
        apart from optional parameters you can provide css keywords
        with underscore instead dash values as well as `flex_direction`
        from the example:
        
        `widget.style(font_size=12, flex_direction='column')`

        `border`, `font_size`, `width` and `height` if given as `int`
        will be parsed as pixels
        """
        style = self._el.style
        
        css:dict = {
            'font-weight': font_weight if bold == None else f"{'bold' if bold == True else 'unset'}",
            'color': color,
            'width': width if isinstance(width, str) else f'{width}px',
            'height': height if isinstance(height, str) else f'{height}px',
            'font_family':font,
            'font-size':f'{font_size}px' if isinstance(font_size, int) else font_size,
            'title':tooltip,
            'background-color':background,
            'font-style':italic,
            'text-align':text_align,
            'border' : f'{border}px solid' if isinstance(border, int) else border

        }
   
        for k,v in kwargs.items():
            css[k.replace('_', '-')] = v
        

        reset = kwargs.get('_reset', None)

        css_text:str = ';'.join([f'{k}:{v}' for k,v in css.items() if v!=None])

        if not reset:
            style.cssText += css_text
        else:
            style.cssText = css_text
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


    def set_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
        """set inline styles removing all old ones
        the key arguments work as in `add_style() `"""


        # for performace will do clean and add on one sweap so giving
        # add_style private key _reset=True for that
        self.add_style(border=border, text_align=text_align,
              tooltip=tooltip, font=font, font_size=font_size,
              font_weight=font_weight, color=color, background=background,
              bold=bold, width=width, height=height, italic=italic, _reset=True, **kwargs)


    @property
    def visible(self)->bool:
        """
        returns visibility value
        True - widget is alowed to be visible
        False - widget is hidden even if its parent is visible in the viewport
        """
        value = self.role.contains('hidden')
        
        return not value


    @visible.setter
    def visible(self, value:bool):
        print('set', value)
        """
        setting the visibility
        under the hood it adds/removes the css class *hidden*
        whinch makes `display:none` if is `False`
        """
        if value:
            self.role.remove('hidden')
        else:
            self.role.add('hidden')
    

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
    def size(self)->tuple:
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





class Container(Component):
    """
    class for all container like widgets as well making generic one
    adding methods to the *class* **Component** to do so
    by defaul the orientation of widgets inside it is column
    the widgets based on it in jamipy will have different orientations
    and if you make custom one, can apply different roles or styles to change it
    """

    # the class uses template for the html elements of the widgets
    # for a little more speed on the slow devices
    _el:Element = make_el_template({'tag_name':'div','roles':'container',})

    _children:set[Component]

    def __init__(self, children:list[Component]=None, roles:str=''):
        """
        will add children widgets provided by the `children:list`
        """

        self._el = self._el.cloneNode()

        if roles:
            self._el.className = roles
            
        self._children = set()

        if children:
            for child in children:
                self.append(child)
            
      
    
    @property
    def children(self)->list[Component]:
        """return ordered list of children widgets"""
        elements:list[Element] = self._el.children
        current:set[Component] = self._children
        ordered = sorted(current, key = lambda child: elements.index(child._el))
        return ordered
    

    @children.setter
    def children(self, children:Component|list[Component])->None:
        """set children widgets"""
        self.clear()
        self.append(children)


    #ad children
    def append(self, children:Component|list[Component]):
        """appends children widgets"""

        new: list[Component] = children if isinstance(children, list) else[children]

        # local set
        current_children:set[Component] = self._children

        for child in new:

            #parsing dom first
            self._el.append(child._el)

            #update local set with current child
            current_children.add(child)

            #update old parent
            if child._parent:
                child._parent._children.discard(child)

            #update child
            child._parent = self

        # update parent set with local one
        self._children = current_children


    def clear(self):
        """clear all children widgets"""

        # clear dom
        self._el.replaceChildren()
        
        # clear children
        for child in self._children:
            child._parent = None

        # clear parent set
        self._children.clear()


    def count(self)->int:
        """return number of children widgets"""
        return len(self._children)
    
    def insert(self, position:int=0, child:Component=None):
        """insert child widget by index
        default value is 0 meaning at start/top of all children
        if index is higher than the count will append at end/bottom"""
        
        count:int = len(self._children)

        #parsing dom with provided index
        if position == 0:
            self._el.prepend(child._el)

        elif position < count:

            #dom children list
            children_el:list[Element] = list(self._el.children)
            #ancor for inserBefore as no insertafter
            after_el:Element = children_el[position + 1]

            self._el.insertBefore(child._el, after_el)

        # if index is higher than count will append
        else:
            self._el.append(child._el)
        
        # update parent set
        self._children.add(child)

        # update if old parent
        if child._parent:
            child._parent._children.discard(child)

        # update child
        child._parent = self



    def pop(self, index:int=-1)->Component:
        """will remove child at provided index and will return it
        default value is -1 and will do the last child
        will return None if index is higher than the count"""

        #retrieve ordered list
        children: list[Component] = self.children

        #None if big index
        if index > len(children):
            return None
        
        else:
            child_pop = children.pop(index)
            self.remove(child_pop)
            return child_pop
 
    def remove(self, children:Component|list[Component]):
        """removes children widget/widgets"""

        rem:list[Component] = children if isinstance(children, list) else [children]
        
        # local set 
        current:set[Component] = self._children
        
        for child in rem:

            # update dom
            child._el.remove()

            # update child
            child._parent = None
            
            # update local set
            current.discard(child)

        # update parent set
        self._children = current
   

    # AUGMENTED ASSIGNED OPERATORS for adding children

    def __iadd__(self, component:Component):
        """
        augmented append of children widgets
        `parent += child`
        """
        self.append(component)
        return self
    
    def __isub__(self, component:Component):
        """
        augmented remove of children widgets
        `parent -= child`
        """
        self.remove(component)
        return self

 




