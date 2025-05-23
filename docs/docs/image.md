## image

Image widget

## *class*:  Image()

<details><summary>[url='', height=None, width=None, display_mode=None, border_radius=None]</summary>


  ```python
class Image(Component):
    _el:Element = make_el_template({'tag_name':  'img','roles':'image'})
    def __init__(self, url='', height=None, width=None, display_mode=None, border_radius=None):
        el:Element = self._el.cloneNode()
        el.src = url
        self._el:Element = el
        self.set_style(width=width, height=height, displayMode=display_mode, borderRadius = border_radius)
```


</details>


Image widget class


### *method*:  \_\_init\_\_()

<details><summary>[self, url='', height=None, width=None, display_mode=None, border_radius=None]</summary>


  ```python
    def __init__(self, url='', height=None, width=None, display_mode=None, border_radius=None):
        el:Element = self._el.cloneNode()
        el.src = url
        self._el:Element = el
        self.set_style(width=width, height=height, displayMode=display_mode, borderRadius = border_radius)
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






