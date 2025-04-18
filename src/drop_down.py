"""
DropDown widget
"""
from .constructors import Component, Container, Element, Events, make_el_template
from .label import Label


class DropDownOption(Component):
    """drop down option widget used by the DropDown widget class"""
    _el:Element = make_el_template({'tag_name':  'option','roles':'dropdown-option'})

    def __init__(self, value=None, text='', selected=False):
        text = text if text else value
        el:Element = self._el.cloneNode()
        self._el = el
        el.setAttribute('value', value)
        el.textContent = text
        self.value = value
        self.text = text
        if selected:
            el.selected = True

class DropDownSelect(Container):
    """DropDown select widget class used by drop down widget"""
    _el:Element = make_el_template({'tag_name':  'select','roles':'dropdown-select'})

    _items:dict = {}
    value = None
    key = None
    def __init__(self, items:list|dict=None, selected_value=None, include_placeholder:bool=True, placeholder='', enabled=True):
        
        el:Element = self._el.cloneNode()
        self._el = el
        self._children = set()
        items = items if items else []
        items = {item:item for item in items} if isinstance(items, list) else items
        
        _items:dict[str|DropDownOption] = {}

        index = 0
        for k,v in items.items():
            selected = True if k == selected_value else False
                
            option = DropDownOption(text=str(k), value=index, selected=selected)

            self.append(option)

            item = {index:{'key':k, 'value':v}}
            _items.update(item)

            index += 1
           
        self._items = _items

        self.add_event_handler('change', self._on_change)

  
    def _on_change(self, event=None):
        """private event handler for change event"""
        index = self._el.value
        data = self._items[int(index)]

   
        key = data['key']
        value = data['value']

      
        self.value = value
        self.key = key
 
        # The value -1 indicates no element is selected.
        parent:DropDown = self.parent
        parent.on_change(parent)


class DropDown(Container):
    """DropDown widget class
    if list will convert to dictionary like key:key and value:key
    keys will be displayed in the ui
    able to be used wit any types for values and stringifable for keys
    will return original key/value couple"""
    

    _items:dict = {}
    value = None
    key = None
    def __init__(self, items:list|dict=None, selected_value=None, include_placeholder:bool=True, placeholder='', enabled=True, icon='expand_all'):
        super().__init__()
        self.role.add('dropdown')
        select = DropDownSelect(items, selected_value, include_placeholder, placeholder, enabled)
        self += select
        self.select = select
        label = Label(icon=icon)
        label.role.add('dropdown-label')
        self += label
        self.label = label

   
    def on_change(self, *args, **kwargs):
        """can be assigned if need"""
        pass

    @property
    def value(self):
        return self.select.value

    @property
    def key(self):
        return self.select.key

