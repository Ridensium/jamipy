"""
Pill widget
Label based, with more styling by default
"""

from .label import Label, IconAlign, make_el_template, Element

class Pill(Label):
    """Pill widget class"""
    _el:Element = make_el_template(
    {
        'tag_name':  'div',
        'roles':'label pill',
        'children': [
                        {
                        'tag_name':  'i',
                        'roles':'icon label-icon pill-icon',
                        },
                        {
                        'tag_name':  'span',
                        'roles':'text label-text pill-text',
                        },
                    ]
    }
        )


    def __init__(self, text = '', icon = None, icon_align = IconAlign.NONE, roles = None):
        super().__init__(text, icon, icon_align, roles)
        


