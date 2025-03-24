## component
module with the super class `Component` used for all widgets
can be used as well to build custom widgets
`js.Element` and `js.DOMTokenList` are imported **only** for typing autosuggestions.

## *class*:  Component()

<details><summary>[tag_name='div', roles: str = None]</summary>

  ```python
class Component:
    
    _el:Element = None


    def __init__(self, tag_name='div', roles:str=None):
        

        self._el:Element = create_el(tag_name)
        if roles:
            self.roles = roles



    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)


    def remove(self):
        
        self._el.remove()


    def set_event_handler(self, event_name:str, handler)->None:
        
        setattr(self._el, f'on{event_name}', handler)


    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)


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

    def get_style(self, name=None)->dict:
        
        styles:str = self.el.style.cssText
        styles = styles.split(';')
        result = {}
        for style in styles:
            style = style.split(':')
            result[style[0]] = style[1]

        return result if name == None else result.get(name, {})


    @property
    def visible(self)->bool:
        
        return self.role.contains('hidden')


    @visible.setter
    def visible(self, value:bool):
        
        if value == False:
            self.role.add('hidden')
        else:
            self.role.remove('hidden')
    

    @property
    def roles(self)->list:
        
        return list(self._el.classList)
        

    @roles.setter
    def roles(self, roles:str|list|set):
        
        _roles = roles if isinstance(roles, str) else ' '.join(roles)
        self._el.className = _roles


    @property
    def role(self)->DOMTokenList:
        
        return self._el.classList
        

    @property
    def get_size(self)->tuple:
        
        rect = self._el.getBoundingClientRect()
        return (rect.width, rect.height)


    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

publick class for the common for all other constructors and widget classes
can be used for building custom widggets
`Component._el` wraps the html element for the widget

### *method*:  \_\_init\_\_()

<details><summary>[self, tag_name='div', roles: str = None]</summary>

  ```python
    def __init__(self, tag_name='div', roles:str=None):
        

        self._el:Element = create_el(tag_name)
        if roles:
            self.roles = roles

  ```

</details>

makes widget with element by default div
if provided roles adds them

### *method*:  display()

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4349001216'>]</summary>

  ```python
    def display(self, parent_el=document.body):
        
        parent_el.append(self._el)
        return self

  ```

</details>

appends the widget to html element in `parent_el`,
which default value is the webpage body

### *method*:  get\_event\_handler()

<details><summary>[self, event_name]</summary>

  ```python
    def get_event_handler(self, event_name):
        
        return getattr(self._el, f'on{event_name}', None)

  ```

</details>

sometimes we may need to know what was the handler we set above

### *method*:  get\_style()

<details><summary>[self, name=None) -> dic]</summary>

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

### *method*:  remove()

<details><summary>[self]</summary>

  ```python
    def remove(self):
        
        self._el.remove()

  ```

</details>

removing widget from its parent

### *method*:  set\_event\_handler()

<details><summary>[self, event_name: str, handler) -> Non]</summary>

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
        

### *method*:  set\_parent()

<details><summary>[self, parent: 'Component', at_begining=False]</summary>

  ```python
    def set_parent(self, parent:'Component', at_begining=False):
        
        if at_begining == False:
            parent._el.append(self._el)
        else:
            parent._el.prepend(self._el)

  ```

</details>

adding widget to parent one

### *method*:  style()

<details><summary>[self, border: str = None, text_align: str = None, tooltip: str = None, font: str = None, font_size: str | int = None, font_weight: int = None, color: str = None, background: str = None, bold: bool = None, width: str | int = None, height: str | int = None, italic: bool = None, **kwargs]</summary>

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



## *function*:  el\_from\_template()

<details><summary>[template: dict = None) -> 'Element]</summary>

  ```python
def el_from_template(template:dict=None)->'Element':
    

    el:Element = create_el(template['tag_name'])
    el.className = template['roles']
    children:dict = template.get('children', [])

    for child in children:
        el_child:Element = el_from_template(child)
        el.append(el_child)
    return el

  ```

</details>

non-publick fn for making elements from template like:

```json

{
    "tag_name":  "div",
    "roles":"label",
    "children": []
}

```

useful for widgets with compund html to make copie from template instead making and nesting new one


