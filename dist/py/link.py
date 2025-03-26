_B='roles'
_A='tag_name'
from.label import Label,IconAlign,make_el_template,Element
class Link(Label):
	_el=make_el_template({_A:'a',_B:'label link','children':[{_A:'i',_B:'icon label-icon link-icon'},{_A:'span',_B:'text label-text link-text'}]})
	def __init__(A,text='',url='',icon=None,icon_align=IconAlign.NONE,roles=None):super().__init__(text,icon,icon_align,roles);A._el.href=url