"""
Image widget
"""

from .constructors import Component, Element, make_el_template


class Image(Component):
    """Image widget class"""
    _el:Element = make_el_template({'tag_name':  'img','roles':'image'})

    def __init__(self, url='', height=None, width=None, display_mode=None, border_radius=None, roles:str=None):

        el:Element = self._el.cloneNode()

        el.src = url

        self._el:Element = el

        self.set_style(width=width, height=height, displayMode=display_mode, borderRadius = border_radius)
        

        if roles:
            self._el.className = roles

