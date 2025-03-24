## label
> publick module for Label widget
> by default uses for the icons googles material-symbols-rounded
> with <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded" rel="stylesheet" />    
> in the html.head

## *class*:  Label(text: str = '', icon: str = None, icon_align: src.m_enums.IconAlign = '', roles: str = None)
> basic Label widget with text and icon
> it has text and icon, and ways to change the icon position
<details><summary><sub>expand source</sub></summary>

  ```python
class Label(Component):
    

    _el:Element = el_from_template(
{
    'tag_name':  'div',
    'roles':'label',
    'children': [
                    {
                    'tag_name':  'i',
                    'roles':'icon label-icon',
                    },
                    {
                    'tag_name':  'span',
                    'roles':'text label-text',
                    },
                ]
}
    )

    def __init__(self, text:str='', icon:str=None, icon_align:IconAlign=IconAlign.NONE, roles:str=None):
        
        el:Element = self._el.cloneNode(True)
        self._el = el
        
        children = el.children
        children[1].textContent = text
        
        if icon:
            children[0].textContent = icon
        if icon_align:
            self.icon_align = icon_align

        if roles:
            self.roles = roles

    @property
    def text(self)->str:
        
        return self._el.children[1].textContent
    
    @text.setter
    def text(self, text:str):
        
        self._el.children[1].textContent = text

    @property
    def icon(self)->str:
        
        return self._el.children[0].textContent
    
    @icon.setter
    def icon(self, char:str):
        
        self._el.children[0].textContent = char


    @property
    def icon_align(self):
        
        return self._el.dataset.flexDirection

    @icon_align.setter
    def icon_align(self, align:str|IconAlign):
        
        self._el.dataset.flexDirection = align

  ```

</details>

#### *method*:  \_\_init\_\_(self, text: str = '', icon: str = None, icon_align: src.m_enums.IconAlign = '', roles: str = None)
> makes widget with element by default div
> if provided roles adds them
<details><summary><sub>expand source</sub></summary>

  ```python
    def __init__(self, text:str='', icon:str=None, icon_align:IconAlign=IconAlign.NONE, roles:str=None):
        
        el:Element = self._el.cloneNode(True)
        self._el = el
        
        children = el.children
        children[1].textContent = text
        
        if icon:
            children[0].textContent = icon
        if icon_align:
            self.icon_align = icon_align

        if roles:
            self.roles = roles

  ```

</details>

#### *method*:  display(self, parent_el=<MagicMock name='mock.document.body' id='4321706400'>)
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

#### *method*:  set\_event\_handler(self, event_name: str, handler) -> None
> ading event handler for the widget, the handler will receive as first argument the event object
> example:

> ```python

> def fn(event=None)
> def fn(self, event=None)
> def fn(*args)

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




