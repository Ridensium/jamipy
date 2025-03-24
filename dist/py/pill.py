_B='roles'
_A='tag_name'
from.label import Label,IconAlign,el_from_template,Element
class Pill(Label):
	_el=el_from_template({_A:'div',_B:'label pill','children':[{_A:'i',_B:'icon label-icon pill-icon'},{_A:'span',_B:'text label-text pill-text'}]})
	def __init__(A,text='',icon=None,icon_align=IconAlign.NONE,roles=None):super().__init__(text,icon,icon_align,roles)