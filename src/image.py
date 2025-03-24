"""
publick class for Image widget
"""

from .component import Component, Element, el_from_template


class Image(Component):

    _el:Element = el_from_template({'tag_name':  'img','roles':'image'})

    def __init__(self, url='', height=None, width=None, display_mode=None, border_radius=None):

        el:Element = self._el.cloneNode()

        el.src = url

        self._el:Element = el

        self.style(width=width, height=height, displayMode=display_mode, borderRadius = border_radius)
        



