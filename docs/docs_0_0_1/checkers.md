## checkers
publick class for option widgets RadioButton, RadioGroup and CheckBox

## *class*:  CheckBox()

<details><summary>CheckBox(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

  ```python
class CheckBox(Checker):
    

    _el:Element = el_from_template({
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

publick class for the RadioButton widget

#### *method*:  __init__()

<details><summary>__init__(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)

        
        if enabled == False:
            self.role.replace('enabled', 'disabled')

        
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.set_event_handler('click', self.toggle_check)

  ```

</details>

makes widget with element by default div
if provided roles adds them

#### *method*:  change()

<details><summary>change(self)</summary>

  ```python
    def change(self):
        pass

  ```

</details>



#### *method*:  display()

<details><summary>display(self, parent_el=<MagicMock name='mock.document.body' id='4309351936'>)</summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

appends the widget to html element in `parent_el`,
which default value is the webpage body

#### *method*:  get_event_handler()

<details><summary>get_event_handler(self, event_name)</summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

sometimes we may need to know what was the handler we set above

#### *method*:  get_style()

<details><summary>get_style(self, name=None) -> dict</summary>

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

#### *method*:  remove()

<details><summary>remove(self)</summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

removing widget from its parent

#### *method*:  set_chechked()

<details><summary>set_chechked(self, checked: bool = False)</summary>

  ```python
    def set_chechked(self, checked:bool=False):
        self.checked = checked
        self._el.children[0].textContent = self._icons[checked]
        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

  ```

</details>



#### *method*:  set_event_handler()

<details><summary>set_event_handler(self, event_name: str, handler) -> None</summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

        ading event handler for the widget, the handler will receive as first argument the event object
        example:

```python

def fn(event=None)
def fn(self, event=None)
def fn(*args)

widget.set_event_handler('click', fn)

```
        

#### *method*:  set_parent()

<details><summary>set_parent(self, parent: 'Component', at_begining=False)</summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

adding widget to parent one

#### *method*:  style()

<details><summary>style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)</summary>

  ```python
    def style(self, border:str=None, text_align:str=None, tooltip:str=None, font:str=None, font_size:str|int=None, font_weight:int=None, color:str=None, background:str=None, bold:bool=None, width:str|int=None, height:str|int=None, italic:bool=None, **kwargs):
        
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

  ```

</details>

its recommended to use classes for styling html instead inline css
but with this method you can add inline styles to the widget
for better performace if adding multipe add them together to reflow the element once
apart from optional parameters you can provide css keywords with underscore instead dash
values if should be provided in css example:
`widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
`border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
it adds the styles doesnt clean all old ones

#### *method*:  toggle_check()

<details><summary>toggle_check(self, event=None)</summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>




## *class*:  Checker()

<details><summary>Checker(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

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
        self.set_event_handler('click', self.toggle_check)


    def set_chechked(self, checked:bool=False):
        self.checked = checked
        self._el.children[0].textContent = self._icons[checked]
        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

    def change(self):
        pass

  ```

</details>

non publick class constructor for the RadioButton and CheckBox
based on the Label

#### *method*:  __init__()

<details><summary>__init__(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)

        
        if enabled == False:
            self.role.replace('enabled', 'disabled')

        
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.set_event_handler('click', self.toggle_check)

  ```

</details>

makes widget with element by default div
if provided roles adds them

#### *method*:  change()

<details><summary>change(self)</summary>

  ```python
    def change(self):
        pass

  ```

</details>



#### *method*:  display()

<details><summary>display(self, parent_el=<MagicMock name='mock.document.body' id='4309351936'>)</summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

appends the widget to html element in `parent_el`,
which default value is the webpage body

#### *method*:  get_event_handler()

<details><summary>get_event_handler(self, event_name)</summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

sometimes we may need to know what was the handler we set above

#### *method*:  get_style()

<details><summary>get_style(self, name=None) -> dict</summary>

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

#### *method*:  remove()

<details><summary>remove(self)</summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

removing widget from its parent

#### *method*:  set_chechked()

<details><summary>set_chechked(self, checked: bool = False)</summary>

  ```python
    def set_chechked(self, checked:bool=False):
        self.checked = checked
        self._el.children[0].textContent = self._icons[checked]
        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

  ```

</details>



#### *method*:  set_event_handler()

<details><summary>set_event_handler(self, event_name: str, handler) -> None</summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

        ading event handler for the widget, the handler will receive as first argument the event object
        example:

```python

def fn(event=None)
def fn(self, event=None)
def fn(*args)

widget.set_event_handler('click', fn)

```
        

#### *method*:  set_parent()

<details><summary>set_parent(self, parent: 'Component', at_begining=False)</summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

adding widget to parent one

#### *method*:  style()

<details><summary>style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)</summary>

  ```python
    def style(self, border:str=None, text_align:str=None, tooltip:str=None, font:str=None, font_size:str|int=None, font_weight:int=None, color:str=None, background:str=None, bold:bool=None, width:str|int=None, height:str|int=None, italic:bool=None, **kwargs):
        
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

  ```

</details>

its recommended to use classes for styling html instead inline css
but with this method you can add inline styles to the widget
for better performace if adding multipe add them together to reflow the element once
apart from optional parameters you can provide css keywords with underscore instead dash
values if should be provided in css example:
`widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
`border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
it adds the styles doesnt clean all old ones

#### *method*:  toggle_check()

<details><summary>toggle_check(self, event=None)</summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>




## *class*:  RadioButton()

<details><summary>RadioButton(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

  ```python
class RadioButton(Checker):
    

    _el:Element = el_from_template({
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
    
    def change(self):
        
        try:
            self._parent.child_changed(self)
        except:
            pass

  ```

</details>

publick class for the RadioButton widget

#### *method*:  __init__()

<details><summary>__init__(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)</summary>

  ```python
    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): 
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)

        
        if enabled == False:
            self.role.replace('enabled', 'disabled')

        
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.set_event_handler('click', self.toggle_check)

  ```

</details>

makes widget with element by default div
if provided roles adds them

#### *method*:  change()

<details><summary>change(self)</summary>

  ```python
    def change(self):
        
        try:
            self._parent.child_changed(self)
        except:
            pass

  ```

</details>



#### *method*:  display()

<details><summary>display(self, parent_el=<MagicMock name='mock.document.body' id='4309351936'>)</summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

appends the widget to html element in `parent_el`,
which default value is the webpage body

#### *method*:  get_event_handler()

<details><summary>get_event_handler(self, event_name)</summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

sometimes we may need to know what was the handler we set above

#### *method*:  get_style()

<details><summary>get_style(self, name=None) -> dict</summary>

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

#### *method*:  remove()

<details><summary>remove(self)</summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

removing widget from its parent

#### *method*:  set_chechked()

<details><summary>set_chechked(self, checked: bool = False)</summary>

  ```python
    def set_chechked(self, checked:bool=False):
        self.checked = checked
        self._el.children[0].textContent = self._icons[checked]
        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

  ```

</details>



#### *method*:  set_event_handler()

<details><summary>set_event_handler(self, event_name: str, handler) -> None</summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

        ading event handler for the widget, the handler will receive as first argument the event object
        example:

```python

def fn(event=None)
def fn(self, event=None)
def fn(*args)

widget.set_event_handler('click', fn)

```
        

#### *method*:  set_parent()

<details><summary>set_parent(self, parent: 'Component', at_begining=False)</summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

adding widget to parent one

#### *method*:  style()

<details><summary>style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)</summary>

  ```python
    def style(self, border:str=None, text_align:str=None, tooltip:str=None, font:str=None, font_size:str|int=None, font_weight:int=None, color:str=None, background:str=None, bold:bool=None, width:str|int=None, height:str|int=None, italic:bool=None, **kwargs):
        
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

  ```

</details>

its recommended to use classes for styling html instead inline css
but with this method you can add inline styles to the widget
for better performace if adding multipe add them together to reflow the element once
apart from optional parameters you can provide css keywords with underscore instead dash
values if should be provided in css example:
`widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
`border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
it adds the styles doesnt clean all old ones

#### *method*:  toggle_check()

<details><summary>toggle_check(self, event=None)</summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>




## *class*:  RadioGroup()

<details><summary>RadioGroup(items: dict | list)</summary>

  ```python
class RadioGroup(Container):
    
    def __init__(self, items:dict|list):
        super().__init__()
        self.role.add('radio-group')
        self._children:list[RadioButton] = []
        items = {item:item for item in items} if isinstance(items, list) else items
        for k,v in items.items():
            radio = RadioButton(text=k, value=v)
            self.add_child(radio)
            self._children.append(radio)
            radio._parent = self

        self.checked:bool = False
        self.value = None

    def child_changed(self, child:RadioButton):
        [c.set_chechked(False) for c in self._children if c != child]
        checked = child.checked
        self.checked = checked
        self.value = child.value if checked == True else None

        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

  ```

</details>

publick class for the RadioGroup widget
creates child widgets RadioButtons by provided list or dictionary from which
gets key:value couple

#### *method*:  __iadd__()

<details><summary>__iadd__(self, component: src.component.Component)</summary>

  ```python
    def __iadd__(self, component:Component):
        
        self.add_child(component)
        return self

  ```

</details>

augmented adding of children widgets
will apend the child widget at end
`parent += child`

#### *method*:  __init__()

<details><summary>__init__(self, items: dict | list)</summary>

  ```python
    def __init__(self, items:dict|list):
        super().__init__()
        self.role.add('radio-group')
        self._children:list[RadioButton] = []
        items = {item:item for item in items} if isinstance(items, list) else items
        for k,v in items.items():
            radio = RadioButton(text=k, value=v)
            self.add_child(radio)
            self._children.append(radio)
            radio._parent = self

        self.checked:bool = False
        self.value = None

  ```

</details>

will add children widgets provided by the `children:list`

#### *method*:  __isub__()

<details><summary>__isub__(self, component: src.component.Component)</summary>

  ```python
    def __isub__(self, component:Component):
        
        component.remove()
        return self

  ```

</details>

augmented removal of children widgets
`parent -= child`

#### *method*:  add_child()

<details><summary>add_child(self, component: src.component.Component)</summary>

  ```python
    def add_child(self, component:Component):
        
        self._el.append(component._el)

  ```

</details>

adsing widget child at end

#### *method*:  add_child_as_first()

<details><summary>add_child_as_first(self, component: src.component.Component)</summary>

  ```python
    def add_child_as_first(self, component:Component):
        
        self._el.prepend(component._el)

  ```

</details>

adsing widget child at begining
for speed esp when lots of children is in separate method to prevent `if`

#### *method*:  child_changed()

<details><summary>child_changed(self, child: src.checkers.RadioButton)</summary>

  ```python
    def child_changed(self, child:RadioButton):
        [c.set_chechked(False) for c in self._children if c != child]
        checked = child.checked
        self.checked = checked
        self.value = child.value if checked == True else None

        if checked == True:
            self.role.add('checked')
        else:
            self.role.remove('checked')

  ```

</details>



#### *method*:  clear()

<details><summary>clear(self)</summary>

  ```python
    def clear(self):
        
        self._el.innerHTML = ''

  ```

</details>

removes all children

#### *method*:  display()

<details><summary>display(self, parent_el=<MagicMock name='mock.document.body' id='4309351936'>)</summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

appends the widget to html element in `parent_el`,
which default value is the webpage body

#### *method*:  get_event_handler()

<details><summary>get_event_handler(self, event_name)</summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

sometimes we may need to know what was the handler we set above

#### *method*:  get_style()

<details><summary>get_style(self, name=None) -> dict</summary>

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

#### *method*:  remove()

<details><summary>remove(self)</summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

removing widget from its parent

#### *method*:  remove_child()

<details><summary>remove_child(self, component: src.component.Component)</summary>

  ```python
    def remove_child(self, component:Component):
        
        component._el.remove()

  ```

</details>

removes child widget from itself

#### *method*:  set_event_handler()

<details><summary>set_event_handler(self, event_name: str, handler) -> None</summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

        ading event handler for the widget, the handler will receive as first argument the event object
        example:

```python

def fn(event=None)
def fn(self, event=None)
def fn(*args)

widget.set_event_handler('click', fn)

```
        

#### *method*:  set_parent()

<details><summary>set_parent(self, parent: 'Component', at_begining=False)</summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

adding widget to parent one

#### *method*:  style()

<details><summary>style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)</summary>

  ```python
    def style(self, border:str=None, text_align:str=None, tooltip:str=None, font:str=None, font_size:str|int=None, font_weight:int=None, color:str=None, background:str=None, bold:bool=None, width:str|int=None, height:str|int=None, italic:bool=None, **kwargs):
        
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

  ```

</details>

its recommended to use classes for styling html instead inline css
but with this method you can add inline styles to the widget
for better performace if adding multipe add them together to reflow the element once
apart from optional parameters you can provide css keywords with underscore instead dash
values if should be provided in css example:
`widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
`border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
it adds the styles doesnt clean all old ones




