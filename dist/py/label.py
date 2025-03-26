_B='roles'
_A='tag_name'
from.constructors import Component,Element,IconAlign,make_el_template
class Label(Component):
	_el=make_el_template({_A:'div',_B:'label','children':[{_A:'i',_B:'icon label-icon'},{_A:'span',_B:'text label-text'}]})
	def __init__(A,text='',icon=None,icon_align=IconAlign.NONE,roles=None):
		C=roles;B=icon_align;D=A._el.cloneNode(True);A._el=D;E=D.children;E[1].textContent=text
		if icon:E[0].textContent=icon
		if B:A.icon_align=B
		if C:A.roles=C
	@property
	def text(self):return self._el.children[1].textContent
	@text.setter
	def text(self,text):self._el.children[1].textContent=text
	@property
	def icon(self):return self._el.children[0].textContent
	@icon.setter
	def icon(self,char):self._el.children[0].textContent=char
	@property
	def icon_align(self):return self._el.dataset.flexDirection
	@icon_align.setter
	def icon_align(self,align):self._el.dataset.flexDirection=align