## checkers
> publick class for option widgets RadioButton, RadioGroup and CheckBox

## *class*:  CheckBox(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> publick class for the RadioButton widget
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  \_\_init\_\_(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> makes widget with element by default div
> if provided roles adds them
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  change(self)

<details><summary><sub>expand source</sub></summary>

  ```python
    def change(self):
        pass

  ```

</details>

#### *method*:  display(self, parent_el=<MagicMock name='mock.document.body' id='4393402784'>)
> appends the widget to html element in `parent_el`,
> which default value is the webpage body
<details><summary><sub>expand source</sub></summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

#### *method*:  get\_event\_handler(self, event_name)
> sometimes we may need to know what was the handler we set above
<details><summary><sub>expand source</sub></summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

#### *method*:  get\_style(self, name=None) -> dict
> gets all if `name=None` or specific inline style/styles
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  remove(self)
> removing widget from its parent
<details><summary><sub>expand source</sub></summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

#### *method*:  set\_chechked(self, checked: bool = False)

<details><summary><sub>expand source</sub></summary>

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

#### *method*:  set\_event\_handler(self, event_name: str, handler) -> None
> ading event handler for the widget, the handler will receive as first argument the event object
> example:

> ```python

> def fn(event=None)
> # def fn(self, event=None)
> # def fn(*args)

> widget.set_event_handler('click', fn)

> ```
> 
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

#### *method*:  set\_parent(self, parent: 'Component', at_begining=False)
> adding widget to parent one
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

#### *method*:  style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)
> its recommended to use classes for styling html instead inline css
> but with this method you can add inline styles to the widget
> for better performace if adding multipe add them together to reflow the element once
> apart from optional parameters you can provide css keywords with underscore instead dash
> values if should be provided in css example:
> `widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
> `border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
> keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
> it adds the styles doesnt clean all old ones
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  toggle\_check(self, event=None)

<details><summary><sub>expand source</sub></summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>


## *class*:  Checker(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> non publick class constructor for the RadioButton and CheckBox
> based on the Label
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  \_\_init\_\_(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> makes widget with element by default div
> if provided roles adds them
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  change(self)

<details><summary><sub>expand source</sub></summary>

  ```python
    def change(self):
        pass

  ```

</details>

#### *method*:  display(self, parent_el=<MagicMock name='mock.document.body' id='4393402784'>)
> appends the widget to html element in `parent_el`,
> which default value is the webpage body
<details><summary><sub>expand source</sub></summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

#### *method*:  get\_event\_handler(self, event_name)
> sometimes we may need to know what was the handler we set above
<details><summary><sub>expand source</sub></summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

#### *method*:  get\_style(self, name=None) -> dict
> gets all if `name=None` or specific inline style/styles
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  remove(self)
> removing widget from its parent
<details><summary><sub>expand source</sub></summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

#### *method*:  set\_chechked(self, checked: bool = False)

<details><summary><sub>expand source</sub></summary>

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

#### *method*:  set\_event\_handler(self, event_name: str, handler) -> None
> ading event handler for the widget, the handler will receive as first argument the event object
> example:

> ```python

> def fn(event=None)
> # def fn(self, event=None)
> # def fn(*args)

> widget.set_event_handler('click', fn)

> ```
> 
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

#### *method*:  set\_parent(self, parent: 'Component', at_begining=False)
> adding widget to parent one
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

#### *method*:  style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)
> its recommended to use classes for styling html instead inline css
> but with this method you can add inline styles to the widget
> for better performace if adding multipe add them together to reflow the element once
> apart from optional parameters you can provide css keywords with underscore instead dash
> values if should be provided in css example:
> `widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
> `border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
> keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
> it adds the styles doesnt clean all old ones
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  toggle\_check(self, event=None)

<details><summary><sub>expand source</sub></summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>


## *class*:  RadioButton(text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> publick class for the RadioButton widget
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  \_\_init\_\_(self, text: str = '', checked: bool = False, value=None, icon_align: src.m_enums.IconAlign = '', enabled=True, **kwargs)
> makes widget with element by default div
> if provided roles adds them
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  change(self)

<details><summary><sub>expand source</sub></summary>

  ```python
    def change(self):
        
        try:
            self._parent.child_changed(self)
        except:
            pass

  ```

</details>

#### *method*:  display(self, parent_el=<MagicMock name='mock.document.body' id='4393402784'>)
> appends the widget to html element in `parent_el`,
> which default value is the webpage body
<details><summary><sub>expand source</sub></summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

#### *method*:  get\_event\_handler(self, event_name)
> sometimes we may need to know what was the handler we set above
<details><summary><sub>expand source</sub></summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

#### *method*:  get\_style(self, name=None) -> dict
> gets all if `name=None` or specific inline style/styles
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  remove(self)
> removing widget from its parent
<details><summary><sub>expand source</sub></summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

#### *method*:  set\_chechked(self, checked: bool = False)

<details><summary><sub>expand source</sub></summary>

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

#### *method*:  set\_event\_handler(self, event_name: str, handler) -> None
> ading event handler for the widget, the handler will receive as first argument the event object
> example:

> ```python

> def fn(event=None)
> # def fn(self, event=None)
> # def fn(*args)

> widget.set_event_handler('click', fn)

> ```
> 
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

#### *method*:  set\_parent(self, parent: 'Component', at_begining=False)
> adding widget to parent one
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

#### *method*:  style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)
> its recommended to use classes for styling html instead inline css
> but with this method you can add inline styles to the widget
> for better performace if adding multipe add them together to reflow the element once
> apart from optional parameters you can provide css keywords with underscore instead dash
> values if should be provided in css example:
> `widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
> `border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
> keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
> it adds the styles doesnt clean all old ones
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  toggle\_check(self, event=None)

<details><summary><sub>expand source</sub></summary>

  ```python
    def toggle_check(self, event=None):
        if self.enabled == True:
            self.set_chechked(not self.checked)
            self.change()

  ```

</details>


## *class*:  RadioGroup(items: dict | list)
> publick class for the RadioGroup widget
> creates child widgets RadioButtons by provided list or dictionary from which
> gets key:value couple
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  \_\_iadd\_\_(self, component: src.component.Component)
> augmented adding of children widgets
> will apend the child widget at end
> `parent += child`
<details><summary><sub>expand source</sub></summary>

  ```python
    def __iadd__(self, component:Component):
        
        self.add_child(component)
        return self

  ```

</details>

#### *method*:  \_\_init\_\_(self, items: dict | list)
> will add children widgets provided by the `children:list`
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  \_\_isub\_\_(self, component: src.component.Component)
> augmented removal of children widgets
> `parent -= child`
<details><summary><sub>expand source</sub></summary>

  ```python
    def __isub__(self, component:Component):
        
        component.remove()
        return self

  ```

</details>

#### *method*:  add\_child(self, component: src.component.Component)
> adsing widget child at end
<details><summary><sub>expand source</sub></summary>

  ```python
    def add_child(self, component:Component):
        
        self._el.append(component._el)

  ```

</details>

#### *method*:  add\_child\_as\_first(self, component: src.component.Component)
> adsing widget child at begining
> for speed esp when lots of children is in separate method to prevent `if`
<details><summary><sub>expand source</sub></summary>

  ```python
    def add_child_as_first(self, component:Component):
        
        self._el.prepend(component._el)

  ```

</details>

#### *method*:  child\_changed(self, child: src.checkers.RadioButton)

<details><summary><sub>expand source</sub></summary>

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

#### *method*:  clear(self)
> removes all children
<details><summary><sub>expand source</sub></summary>

  ```python
    def clear(self):
        
        self._el.innerHTML = ''

  ```

</details>

#### *method*:  display(self, parent_el=<MagicMock name='mock.document.body' id='4393402784'>)
> appends the widget to html element in `parent_el`,
> which default value is the webpage body
<details><summary><sub>expand source</sub></summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

#### *method*:  get\_event\_handler(self, event_name)
> sometimes we may need to know what was the handler we set above
<details><summary><sub>expand source</sub></summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

#### *method*:  get\_style(self, name=None) -> dict
> gets all if `name=None` or specific inline style/styles
<details><summary><sub>expand source</sub></summary>

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

#### *method*:  remove(self)
> removing widget from its parent
<details><summary><sub>expand source</sub></summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

#### *method*:  remove\_child(self, component: src.component.Component)
> removes child widget from itself
<details><summary><sub>expand source</sub></summary>

  ```python
    def remove_child(self, component:Component):
        
        component._el.remove()

  ```

</details>

#### *method*:  set\_event\_handler(self, event_name: str, handler) -> None
> ading event handler for the widget, the handler will receive as first argument the event object
> example:

> ```python

> def fn(event=None)
> # def fn(self, event=None)
> # def fn(*args)

> widget.set_event_handler('click', fn)

> ```
> 
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)

  ```

</details>

#### *method*:  set\_parent(self, parent: 'Component', at_begining=False)
> adding widget to parent one
<details><summary><sub>expand source</sub></summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

#### *method*:  style(self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs)
> its recommended to use classes for styling html instead inline css
> but with this method you can add inline styles to the widget
> for better performace if adding multipe add them together to reflow the element once
> apart from optional parameters you can provide css keywords with underscore instead dash
> values if should be provided in css example:
> `widget.style(font_size=12, flex_direction='column', border = '1px solid gray')`
> `border`, `font_size`, `width` and `height` if given as `int` will be parsed as pixels
> keep in mind the in jamipy you have better ways for styling with role/roles and custom/dynamic css stylesheets
> it adds the styles doesnt clean all old ones
<details><summary><sub>expand source</sub></summary>

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




