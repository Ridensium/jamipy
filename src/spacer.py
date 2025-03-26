"""
Spacer widget
extends the space betheen widgets in containers
"""

from .constructors import Component, Element, make_el_template


class Spacer(Component):
    """Spacer widget class"""
    _el:Element = make_el_template({'tag_name':  'div','roles':'spacer'})
      
    def __init__(self):

        self._el:Element = self._el.cloneNode()




