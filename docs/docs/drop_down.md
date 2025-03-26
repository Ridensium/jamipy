## drop_down

DropDown widget

## *class*:  DropDown()

<details><summary>[items: list | dict = None, selected_value=None, include_placeholder: bool = True, placeholder='', enabled=True]</summary>


  ```python
class DropDown(Container):
    _el:Element = make_el_template({'tag_name':  'select','roles':'dropdown'})
    _items:dict = {}
    value = None
    key = None
    def __init__(self, items:list|dict=None, selected_value=None, include_placeholder:bool=True, placeholder='', enabled=True):
        el:Element = self._el.cloneNode()
        self._el = el
        self._children = set()
        items = {item:item for item in items} if isinstance(items, list) else items
        _items:dict[str|DropDownOption] = {}
        for k,v in items.items():
            option = DropDownOption(key=k, value=v)
            self.append(option)
            _items.update({str(v):k})
        self._items = _items
        self.add_event_handler('change', self._on_change)
    def _on_change(self, event):
        value = self._el.value
        key = self._items.get(value, None)
        self.value = value
        self.key = key
```


</details>


DropDown widget class


### *method*:  \_\_init\_\_()

<details><summary>[self, items: list | dict = None, selected_value=None, include_placeholder: bool = True, placeholder='', enabled=True]</summary>


  ```python
    def __init__(self, items:list|dict=None, selected_value=None, include_placeholder:bool=True, placeholder='', enabled=True):
        el:Element = self._el.cloneNode()
        self._el = el
        self._children = set()
        items = {item:item for item in items} if isinstance(items, list) else items
        _items:dict[str|DropDownOption] = {}
        for k,v in items.items():
            option = DropDownOption(key=k, value=v)
            self.append(option)
            _items.update({str(v):k})
        self._items = _items
        self.add_event_handler('change', self._on_change)
```


</details>


will add children widgets provided by the `children:list`


### *method*:  \_on\_change()

<details><summary>[self, event]</summary>


  ```python
    def _on_change(self, event):
        value = self._el.value
        key = self._items.get(value, None)
        self.value = value
        self.key = key
```


</details>


private event handler for change event


### *method*:  \_\_iadd\_\_()

<details><summary>[self, component: src.constructors.Component]</summary>


  ```python
    def __iadd__(self, component:Component):
        self.append(component)
        return self
```


</details>


augmented append of children widgets
`parent += child`


### *method*:  \_\_isub\_\_()

<details><summary>[self, component: src.constructors.Component]</summary>


  ```python
    def __isub__(self, component:Component):
        self.remove(component)
        return self
```


</details>


augmented remove of children widgets
`parent -= child`


### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            _add_event_handler(self, event_name, handler)
        return self
```


</details>


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


### *method*:  add\_style()

<details><summary>[self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs]</summary>


  ```python
    def add_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
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
```


</details>


ading inline styles to the widget
apart from optional parameters you can provide css keywords
with underscore instead dash values as well as `flex_direction`
from the example:

`widget.style(font_size=12, flex_direction='column')`

`border`, `font_size`, `width` and `height` if given as `int`
will be parsed as pixels


### *method*:  append()

<details><summary>[self, children: src.constructors.Component | list[src.constructors.Component]]</summary>


  ```python
    def append(self, children:Component|list[Component]):
        new: list[Component] = children if isinstance(children, list) else[children]
        current_children:set[Component] = self._children
        for child in new:
            self._el.append(child._el)
            current_children.add(child)
            if child._parent:
                child._parent._children.discard(child)
            child._parent = self
        self._children = current_children
```


</details>


appends children widgets


### *method*:  clear()

<details><summary>[self]</summary>


  ```python
    def clear(self):
        self._el.innerHTML = ''
        for child in self._children:
            child._parent = None
        self._children.clear()
```


</details>


clear all children widgets


### *method*:  count()

<details><summary>[self] ->  int</summary>


  ```python
    def count(self)->int:
        return len(self._children)
```


</details>


return number of children widgets


### *method*:  display()

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4356702624'>]</summary>


  ```python
    def display(self, parent_el=document.body):
        parent_el.append(self._el)
        return self
```


</details>


appends the widget to html element in `parent_el`,
which default value is the webpage body


### *method*:  get\_style()

<details><summary>[self, name=None] ->  dict</summary>


  ```python
    def get_style(self, name=None)->dict:
        styles:str = self.el.style.cssText
        styles = styles.split(';')
        result = {}
        for style in styles:
            style = style.split(':')
            result[style[0]] = style[1]
        return result if name == None else result.get(name, {})
```


</details>


gets all if `name=None` or specific inline style/styles


### *method*:  insert()

<details><summary>[self, position: int = 0, child: src.constructors.Component = None]</summary>


  ```python
    def insert(self, position:int=0, child:Component=None):
        count:int = len(self._children)
        if position == 0:
            self._el.prepend(child._el)
        elif position < count:
            children_el:list[Element] = list(self._el.children)
            after_el:Element = children_el[position + 1]
            self._el.insertBefore(child._el, after_el)
        else:
            self._el.append(child._el)
        self._children.add(child)
        if child._parent:
            child._parent._children.discard(child)
        child._parent = self
```


</details>


insert child widget by index
default value is 0 meaning at start/top of all children
if index is higher than the count will append at end/bottom


### *method*:  pop()

<details><summary>[self, index: int = -1] ->  src.constructors.Component</summary>


  ```python
    def pop(self, index:int=-1)->Component:
        children: list[Component] = self.children
        if index > len(children):
            return None
        else:
            child_pop = children.pop(index)
            self.remove(child_pop)
            return child_pop
```


</details>


will remove child at provided index and will return it
default value is -1 and will do the last child
will return None if index is higher than the count


### *method*:  remove()

<details><summary>[self, children: src.constructors.Component | list[src.constructors.Component]]</summary>


  ```python
    def remove(self, children:Component|list[Component]):
        rem:list[Component] = children if isinstance(children, list) else [children]
        current:set[Component] = self._children
        for child in rem:
            child._el.remove()
            child._parent = None
            current.discard(child)
        self._children = current
```


</details>


removes children widget/widgets


### *method*:  remove\_event\_handler()

<details><summary>[self, event_name: str = None, handler=None, remove_all=False]</summary>


  ```python
    def remove_event_handler(self, event_name:str=None,
                             handler=None, remove_all=False):
        el = self._el
        if event_name and handler:
            if INTERPRETOR == 'py':
                handler = create_proxy(handler)
            el.removeEventListener(event_name, handler)
        elif remove_all:
            new_el = el.cloneNode(True)
            el.replaceWith(new_el)
```


</details>


remove selected or all event handlers
> [!CAUTION]
removing **all** handlers may break functionality,
in some elements like `CheckBox` for example


### *method*:  set\_style()

<details><summary>[self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs]</summary>


  ```python
    def set_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
        self.add_style(border=border, text_align=text_align,
              tooltip=tooltip, font=font, font_size=font_size,
              font_weight=font_weight, color=color, background=background,
              bold=bold, width=width, height=height, italic=italic, _reset=True, **kwargs)
```


</details>


set inline styles removing all old ones
the key arguments work as in `add_style() `



## *class*:  DropDownOption()

<details><summary>[value=None, key='']</summary>


  ```python
class DropDownOption(Component):
    _el:Element = make_el_template({'tag_name':  'option','roles':'dropdown-option'})
    def __init__(self, value=None, key=''):
        el:Element = self._el.cloneNode()
        self._el = el
        el.setAttribute('value', value)
        el.textContent = key
        self.value = value
        self.key = key
```


</details>


drop down option widget used by the DropDown widget class


### *method*:  \_\_init\_\_()

<details><summary>[self, value=None, key='']</summary>


  ```python
    def __init__(self, value=None, key=''):
        el:Element = self._el.cloneNode()
        self._el = el
        el.setAttribute('value', value)
        el.textContent = key
        self.value = value
        self.key = key
```


</details>


`tag_name` - tag name for the coresponding element, by default `div`
`roles` - string with delimeter space, list or set for the roles
of that widget wich are representing css classes as well


### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            _add_event_handler(self, event_name, handler)
        return self
```


</details>


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


### *method*:  add\_style()

<details><summary>[self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs]</summary>


  ```python
    def add_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
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
```


</details>


ading inline styles to the widget
apart from optional parameters you can provide css keywords
with underscore instead dash values as well as `flex_direction`
from the example:

`widget.style(font_size=12, flex_direction='column')`

`border`, `font_size`, `width` and `height` if given as `int`
will be parsed as pixels


### *method*:  display()

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4356702624'>]</summary>


  ```python
    def display(self, parent_el=document.body):
        parent_el.append(self._el)
        return self
```


</details>


appends the widget to html element in `parent_el`,
which default value is the webpage body


### *method*:  get\_style()

<details><summary>[self, name=None] ->  dict</summary>


  ```python
    def get_style(self, name=None)->dict:
        styles:str = self.el.style.cssText
        styles = styles.split(';')
        result = {}
        for style in styles:
            style = style.split(':')
            result[style[0]] = style[1]
        return result if name == None else result.get(name, {})
```


</details>


gets all if `name=None` or specific inline style/styles


### *method*:  remove\_event\_handler()

<details><summary>[self, event_name: str = None, handler=None, remove_all=False]</summary>


  ```python
    def remove_event_handler(self, event_name:str=None,
                             handler=None, remove_all=False):
        el = self._el
        if event_name and handler:
            if INTERPRETOR == 'py':
                handler = create_proxy(handler)
            el.removeEventListener(event_name, handler)
        elif remove_all:
            new_el = el.cloneNode(True)
            el.replaceWith(new_el)
```


</details>


remove selected or all event handlers
> [!CAUTION]
removing **all** handlers may break functionality,
in some elements like `CheckBox` for example


### *method*:  set\_style()

<details><summary>[self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs]</summary>


  ```python
    def set_style(self, border:str=None, text_align:str=None,
              tooltip:str=None, font:str=None, font_size:str|int=None,
              font_weight:int=None, color:str=None, background:str=None,
              bold:bool=None, width:str|int=None, height:str|int=None,
              italic:bool=None, **kwargs):
        self.add_style(border=border, text_align=text_align,
              tooltip=tooltip, font=font, font_size=font_size,
              font_weight=font_weight, color=color, background=background,
              bold=bold, width=width, height=height, italic=italic, _reset=True, **kwargs)
```


</details>


set inline styles removing all old ones
the key arguments work as in `add_style() `






