"""
publick class for DropDown widget
"""
from .component import Component, Element, Events, el_from_template
from .container import Container


class DropDownOption(Component):
    """non-publick class for the drop down option widget"""
    _el:Element = el_from_template({'tag_name':  'option','roles':'dropdown-option'})

    def __init__(self, value=None, key=''):

        el:Element = self._el.cloneNode()
        self._el = el
        el.setAttribute('value', value)
        el.textContent = key
        self.value = value
        self.key = key

class DropDown(Container):
    """publick class for the drop down widget"""
    _el:Element = el_from_template({'tag_name':  'select','roles':'dropdown'})

    _items:dict = {}
    value = None
    key = None
    def __init__(self, items:list|dict=None, selected_value=None, include_placeholder:bool=True, placeholder='', enabled=True):
        
        el:Element = self._el.cloneNode()
        self._el = el
        
        items = {item:item for item in items} if isinstance(items, list) else items

        _items:dict[str|DropDownOption] = {}

        for k,v in items.items():

            option = DropDownOption(key=k, value=v)

            self.add_child(option)

            _items.update({str(v):k})
           
        self._items = _items

        self.set_event_handler('change', self.change)
  
    def change(self, event):
        value = self._el.value
        key = self._items.get(value, None)
        self.value = value
        self.key = key
        # The value -1 indicates no element is selected.

