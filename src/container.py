"""
module with the class `Container` used for widgets with ability to add children ones
can be used as well to build custom widgets
"""

from .component import Component, Element, el_from_template, create_el


class Container(Component):
    """
    class for all container like widgets as well making generic one
    adding methods to the *class* **Component** to do so
    by defaul the orientation of widgets inside it is column
    the widgets based on it in jamipy will have different orientations
    and if you make custom one, can apply different roles or styles to change it
    """

    # the class uses template for the html elements of the widgets
    # for a little more speed on the slow devices
    _el:Element = el_from_template({'tag_name':'div','roles':'container',})


    def __init__(self, children:list[Component]=None, *args, **kwargs):
        """
        will add children widgets provided by the `children:list`
        """

        self._el = self._el.cloneNode()

        if children:
            for child in children:
                self.add_child(child)


    def add_child(self, component:Component):
        """adsing widget child at end"""
        self._el.append(component._el)


    def add_child_as_first(self, component:Component):
        """
        adsing widget child at begining
        for speed esp when lots of children is in separate method to prevent `if`
        """
        self._el.prepend(component._el)


    def remove_child(self, component:Component):
        """removes child widget from itself"""
        component._el.remove()


    def clear(self):
        """removes all children"""
        self._el.innerHTML = ''


    # AUGMENTED ASSIGNED OPERATORS for adding children

    def __iadd__(self, component:Component):
        """
        augmented adding of children widgets
        will apend the child widget at end
        `parent += child`
        """
        self.add_child(component)
        return self
    
    def __isub__(self, component:Component):
        """
        augmented removal of children widgets
        `parent -= child`
        """
        component.remove()
        return self

 
