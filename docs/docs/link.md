## link

module for Link (hyperlink) widget class
Label based, with more styling by default and url keyword as well

## *class*:  Link()

<details><summary>[text='', url='', icon=None, icon_align='', roles=None]</summary>


  ```python
class Link(Label):

    _el:Element = el_from_template({
'tag_name':'a',
'roles':'label link',
'children':[{
'tag_name':'i',
'roles':'icon label-icon link-icon',
},
{
'tag_name':  'span',
'roles':'text label-text link-text',
},
]})


    def __init__(self, text = '', url='', icon = None, icon_align = IconAlign.NONE, roles = None):
        super().__init__(text, icon, icon_align, roles)
        self._el.href = url

  ```


</details>


basic Label widget with text and icon
it has text and icon, and ways to change the icon position


### *method*:  \_\_init\_\_()

<details><summary>[self, text='', url='', icon=None, icon_align='', roles=None]</summary>


  ```python
    def __init__(self, text = '', url='', icon = None, icon_align = IconAlign.NONE, roles = None):
        super().__init__(text, icon, icon_align, roles)
        self._el.href = url

  ```


</details>


makes widget with element by default div
if provided roles adds them


### *method*:  display()

<details><summary>[self, parent_el=<MagicMock name='mock.document.body' id='4355867040'>]</summary>


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


### *method*:  remove()

<details><summary>[self]</summary>


  ```python
    def remove(self):
        
        self._el.remove()

  ```


</details>


removing widget from its parent


### *method*:  set\_event\_handler()

<details><summary>[self, event_name: str, handler] ->  None</summary>


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






