"""
RadioButton, RadioGroup and CheckBox widgets
"""

from .label import Label, IconAlign
from .constructors import Container, Element, make_el_template

class Checker(Label):
    """
    class constructor for the RadioButton and CheckBox
    based on the Label
    """

    _icons = {True:'check_box', False:'check_box_outline_blank'}

    def __init__(self, text:str='', checked:bool=False, value=None, icon_align:IconAlign=IconAlign.NONE,  enabled=True, **kwargs): #allow_indeterminate=False, True/False and None state
        super().__init__(text=text, icon=self._icons[checked], icon_align=icon_align, **kwargs)

        #enabled
        if enabled == False:
            self.role.replace('enabled', 'disabled')

        #class attr
        self.checked:bool = checked
        self.enabled:bool = enabled
        self.value = value
        self.add_event_handler('click', self._on_click)


    def _set_checked(self, checked:bool):
        """private method for changing visuals depending the checked state"""
        self._el.children[0].textContent = self._icons[checked]
        self.checked = checked
        self._el.dataset.checked = checked

    def _on_click(self, event=None):
        """private handler for the click event
        is `_on_click` to show is private and not to mess if one later
        set aditional handler for click with method `on_click`"""
        if self.enabled == True:
            self._set_checked(not self.checked)


class RadioButton(Checker):
    """RadioButton widget class
    can be used separate from the RadioGroup too"""

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
        """private method - handler for the click events
        apart from the what is in super()
        will send message to the RadioGroup if there is one
        """
        super()._on_click(event)
        group:RadioGroup = self._group
        if group:
            group._child_changed(child=self)
        

class CheckBox(Checker):
    """RadioButton widget class"""

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



class RadioGroup(Container):
    """
    RadioGroup widget class
    creates children RadioButtons by provided list or dictionary
    from which gets key:value couple 
    if list both key and value will be equal to the item from it
    """
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
        """private method for parsing clicks on RadioButtons"""
        children:set[RadioButton] = self._children

        [c._set_checked(False) for c in children if c != child]
        checked = child.checked
        self.checked = checked
        self.value = child.value if checked == True else None

        self._el.dataset.checked = checked



