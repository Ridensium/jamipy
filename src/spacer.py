"""
module for the Spacer widget class, which
extends the space betheen widgets in containers
"""

from .component import Component, Element, el_from_template


class Spacer(Component):

    _el:Element = el_from_template({'tag_name':  'div','roles':'spacer'})
      
    def __init__(self):

        self._el:Element = self._el.cloneNode()




