"""
module for option widgets RadioButton, RadioGroup and CheckBox
"""

from .label import Label, IconAlign
from .container import Container, Element, el_from_template

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


class RadioButton(Checker):
    """publick class for the RadioButton widget"""

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
        #try is faster than if
        try:
            self._parent.child_changed(self)
        except:
            pass

class CheckBox(Checker):
    """publick class for the RadioButton widget"""

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



class RadioGroup(Container):
    """
    publick class for the RadioGroup widget
    creates child widgets RadioButtons by provided list or dictionary from which
    gets key:value couple
    """
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


