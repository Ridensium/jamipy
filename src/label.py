"""
Label widget
by default uses for the icons googles material-symbols-rounded
with <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded" rel="stylesheet" />    
in the html.head
"""

from .constructors import Component, Element, IconAlign, make_el_template


class Label(Component):
    """
    Label widget class
    it has text and icon, and ways to change the icon position
    """

    _el:Element = make_el_template(
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
        """get text of the label"""
        return self._el.children[1].textContent
    
    @text.setter
    def text(self, text:str):
        """set text of the label"""
        self._el.children[1].textContent = text

    @property
    def icon(self)->str:
        """
        get the value of the icon
        """
        return self._el.children[0].textContent
    
    @icon.setter
    def icon(self, char:str):
        """
        set icon with name of the gliph - if like google icons
        or character of it - if like fontawesome
        """
        self._el.children[0].textContent = char


    @property
    def icon_align(self):
        """
        returns css value of flex direction:
        'row' if at left
        'row-reverse' if at right
        'column' if on top
        'column-reverse' if at bottom
        '' if at left
        """
        return self._el.dataset.flexDirection

    @icon_align.setter
    def icon_align(self, align:str|IconAlign):
        """
        seting the icon position
        use IconAlign class as it simplifies it to:
        TOP, LEFT, RIGHT and BOTTOM - towards the text
        if not using the helper class IconAlign provide css value for `flex-direction`
        Note: micropython doesnt have Enum so its simple dataclass like
        """
        self._el.dataset.flexDirection = align



