"""
DropDown widget
"""
from .constructors import Component, Container, Element, Events, make_el_template


class DropDownOption(Component):
    """drop down option widget used by the DropDown widget class"""
    _el:Element = make_el_template({'tag_name':  'option','roles':'dropdown-option'})

    def __init__(self, value=None, key=''):

        el:Element = self._el.cloneNode()
        self._el = el
        el.setAttribute('value', value)
        el.textContent = key
        self.value = value
        self.key = key

class DropDown(Container):
    """DropDown widget class"""
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
        """private event handler for change event"""
        value = self._el.value
        key = self._items.get(value, None)
        self.value = value
        self.key = key
        # The value -1 indicates no element is selected.
