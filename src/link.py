"""
Link (hyperlink) widget
Label based, with more styling by default and url keyword as well
"""

from .label import Label, IconAlign, make_el_template, Element

class Link(Label):
    """Link widget class (hyperlinks)"""
    _el:Element = make_el_template({
'tag_name':'a',
'roles':'label link',
'children':[{
'tag_name':'i',
'roles':'icon label-icon link-icon',
},
{
'tag_name':  'span',
'roles':'text label-text link-text',
},
]})


    def __init__(self, text = '', url='', icon = None, icon_align = IconAlign.NONE, roles = None):
        super().__init__(text, icon, icon_align, roles)
        self._el.href = url
        


