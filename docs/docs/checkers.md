## checkers

RadioButton, RadioGroup and CheckBox widgets

## *class*:  CheckBox()

<details><summary>[text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
class CheckBox(Checker):
    _el:Element = make_el_template({
    'tag_name':  'div',
    'roles':'label checkbox enabled',
    'children': [
                    {
                    'tag_name':  'i',
                    'roles':'icon label-icon checkbox-icon',
                    },
                    {
                    'tag_name':  'span',
                    'roles':'text label-text checkbox-text',
                    },
                ]
})
    _icons = {True:'check_box', False:'check_box_outline_blank'}
```


</details>


RadioButton widget class


### *method*:  \_\_init\_\_()

<details><summary>[self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)
        if enabled == False:
            self.role.replace('enabled', 'disabled')
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.add_event_handler('click', self._on_click)
```


</details>


`tag_name` - tag name for the coresponding element, by default `div`
`roles` - string with delimeter space, list or set for the roles
of that widget wich are representing css classes as well


### *method*:  \_add\_event\_handler()

<details><summary>[component: 'Component', event_name: str, handler]</summary>


  ```python
def add_event_handler_py(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, create_proxy(handler))
```


</details>





### *method*:  \_on\_click()

<details><summary>[self, event=None]</summary>


  ```python
    def _on_click(self, event=None):
        if self.enabled == True:
            self._set_checked(not self.checked)
```


</details>


private handler for the click event
is `_on_click to show is private and not to mess if one later
set aditional handler for click with method `on_click`


### *method*:  \_set\_checked()

<details><summary>[self, checked: bool]</summary>


  ```python
    def _set_checked(self, checked:bool):
        self._el.children[0].textContent = self._icons[checked]
        self.checked = checked
        self._el.dataset.checked = checked
```


</details>


private method for changing visuals depending the checked state


### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            self._add_event_handler(event_name, handler)
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

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4386701728'>]</summary>


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



## *class*:  Checker()

<details><summary>[text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
class Checker(Label):
    _icons = {True:'check_box', False:'check_box_outline_blank'}
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)
        if enabled == False:
            self.role.replace('enabled', 'disabled')
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.add_event_handler('click', self._on_click)
    def _set_checked(self, checked:bool):
        self._el.children[0].textContent = self._icons[checked]
        self.checked = checked
        self._el.dataset.checked = checked
    def _on_click(self, event=None):
        if self.enabled == True:
            self._set_checked(not self.checked)
```


</details>


class constructor for the RadioButton and CheckBox
based on the Label


### *method*:  \_\_init\_\_()

<details><summary>[self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)
        if enabled == False:
            self.role.replace('enabled', 'disabled')
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.add_event_handler('click', self._on_click)
```


</details>


`tag_name` - tag name for the coresponding element, by default `div`
`roles` - string with delimeter space, list or set for the roles
of that widget wich are representing css classes as well


### *method*:  \_set\_checked()

<details><summary>[self, checked: bool]</summary>


  ```python
    def _set_checked(self, checked:bool):
        self._el.children[0].textContent = self._icons[checked]
        self.checked = checked
        self._el.dataset.checked = checked
```


</details>


private method for changing visuals depending the checked state


### *method*:  \_on\_click()

<details><summary>[self, event=None]</summary>


  ```python
    def _on_click(self, event=None):
        if self.enabled == True:
            self._set_checked(not self.checked)
```


</details>


private handler for the click event
is `_on_click to show is private and not to mess if one later
set aditional handler for click with method `on_click`


### *method*:  \_add\_event\_handler()

<details><summary>[component: 'Component', event_name: str, handler]</summary>


  ```python
def add_event_handler_py(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, create_proxy(handler))
```


</details>





### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            self._add_event_handler(event_name, handler)
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

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4386701728'>]</summary>


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



## *class*:  RadioButton()

<details><summary>[text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
class RadioButton(Checker):
    _group:'RadioGroup' = None
    _el:Element = make_el_template({
    'tag_name':  'div',
    'roles':'label radio enabled',
    'children': [
                    {
                    'tag_name':  'i',
                    'style':    {},
                    'roles':'icon label-icon radio-icon',
                    },
                    {
                    'tag_name':  'span',
                    'style':    {},
                    'roles':'text label-text radio-text',
                    },
                ]
})
    _icons = {True:'radio_button_checked', False:'radio_button_unchecked'}
    _parent:'RadioGroup' = None
    def _on_click(self, event=None):
        super()._on_click(event)
        group:RadioGroup = self._group
        if group:
            group._child_changed(child=self)
```


</details>


RadioButton widget class
can be used separate from the RadioGroup too


### *method*:  \_on\_click()

<details><summary>[self, event=None]</summary>


  ```python
    def _on_click(self, event=None):
        super()._on_click(event)
        group:RadioGroup = self._group
        if group:
            group._child_changed(child=self)
```


</details>


private method - handler for the click events
apart from the what is in super()
will send message to the RadioGroup if there is one


### *method*:  \_\_init\_\_()

<details><summary>[self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs]</summary>


  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)
        if enabled == False:
            self.role.replace('enabled', 'disabled')
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.add_event_handler('click', self._on_click)
```


</details>


`tag_name` - tag name for the coresponding element, by default `div`
`roles` - string with delimeter space, list or set for the roles
of that widget wich are representing css classes as well


### *method*:  \_add\_event\_handler()

<details><summary>[component: 'Component', event_name: str, handler]</summary>


  ```python
def add_event_handler_py(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, create_proxy(handler))
```


</details>





### *method*:  \_set\_checked()

<details><summary>[self, checked: bool]</summary>


  ```python
    def _set_checked(self, checked:bool):
        self._el.children[0].textContent = self._icons[checked]
        self.checked = checked
        self._el.dataset.checked = checked
```


</details>


private method for changing visuals depending the checked state


### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            self._add_event_handler(event_name, handler)
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

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4386701728'>]</summary>


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



## *class*:  RadioGroup()

<details><summary>[items: dict | list]</summary>


  ```python
class RadioGroup(Container):
    def __init__(self, items:dict|list):
        super().__init__()
        self.role.add('radio-group')
        items = {item:item for item in items} if isinstance(items, list) else items
        for k,v in items.items():
            radio = RadioButton(text=k, value=v)
            self.append(radio)
            radio._group = self
        self.checked:bool = False
        self.value = None
    def _child_changed(self, child:RadioButton):
        children:set[RadioButton] = self._children
        [c._set_checked(False) for c in children if c != child]
        checked = child.checked
        self.checked = checked
        self.value = child.value if checked == True else None
        self._el.dataset.checked = checked
```


</details>


RadioGroup widget class
creates children RadioButtons by provided list or dictionary
from which gets key:value couple 
if list both key and value will be equal to the item from it


### *method*:  \_\_init\_\_()

<details><summary>[self, items: dict | list]</summary>


  ```python
    def __init__(self, items:dict|list):
        super().__init__()
        self.role.add('radio-group')
        items = {item:item for item in items} if isinstance(items, list) else items
        for k,v in items.items():
            radio = RadioButton(text=k, value=v)
            self.append(radio)
            radio._group = self
        self.checked:bool = False
        self.value = None
```


</details>


will add children widgets provided by the `children:list`


### *method*:  \_child\_changed()

<details><summary>[self, child: src.checkers.RadioButton]</summary>


  ```python
    def _child_changed(self, child:RadioButton):
        children:set[RadioButton] = self._children
        [c._set_checked(False) for c in children if c != child]
        checked = child.checked
        self.checked = checked
        self.value = child.value if checked == True else None
        self._el.dataset.checked = checked
```


</details>


private method for parsing clicks on RadioButtons


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


### *method*:  \_add\_event\_handler()

<details><summary>[component: 'Component', event_name: str, handler]</summary>


  ```python
def add_event_handler_py(component:'Component', event_name:str, handler):
    component._el.addEventListener(event_name, create_proxy(handler))
```


</details>





### *method*:  add\_event\_handler()

<details><summary>[self, event_name: str, handler=None] ->  None</summary>


  ```python
    def add_event_handler(self, event_name:str, handler=None)->None:
        handler = handler if handler else getattr(self, f'on_{event_name}', None)
        if handler:
            self._add_event_handler(event_name, handler)
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

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4386701728'>]</summary>


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






