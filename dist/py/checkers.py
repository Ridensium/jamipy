_I='children'
_H='check_box_outline_blank'
_G='check_box'
_F='checked'
_E=None
_D='roles'
_C='tag_name'
_B=False
_A=True
from.label import Label,IconAlign
from.container import Container,Element,el_from_template
class Checker(Label):
	_icons={_A:_G,_B:_H}
	def __init__(A,text='',checked=_B,value=_E,icon_align=IconAlign.NONE,enabled=_A,**D):
		C=enabled;B=checked;super().__init__(text=text,icon=A._icons[B],icon_align=icon_align,**D)
		if C==_B:A.role.replace('enabled','disabled')
		A.checked=B;A.enabled=C;A.value=value;A.set_event_handler('click',A.toggle_check)
	def set_chechked(A,checked=_B):
		B=checked;A.checked=B;A._el.children[0].textContent=A._icons[B]
		if B==_A:A.role.add(_F)
		else:A.role.remove(_F)
	def toggle_check(A,event=_E):
		if A.enabled==_A:A.set_chechked(not A.checked);A.change()
	def change(A):0
class RadioButton(Checker):
	_el=el_from_template({_C:'div',_D:'label radio enabled',_I:[{_C:'i','style':{},_D:'icon label-icon radio-icon'},{_C:'span','style':{},_D:'text label-text radio-text'}]});_icons={_A:'radio_button_checked',_B:'radio_button_unchecked'};_parent=_E
	def change(A):
		try:A._parent.child_changed(A)
		except:pass
class CheckBox(Checker):_el=el_from_template({_C:'div',_D:'label checkbox enabled',_I:[{_C:'i',_D:'icon label-icon checkbox-icon'},{_C:'span',_D:'text label-text checkbox-text'}]});_icons={_A:_G,_B:_H}
class RadioGroup(Container):
	def __init__(A,items):
		B=items;super().__init__();A.role.add('radio-group');A._children=[];B={A:A for A in B}if isinstance(B,list)else B
		for(D,E)in B.items():C=RadioButton(text=D,value=E);A.add_child(C);A._children.append(C);C._parent=A
		A.checked=_B;A.value=_E
	def child_changed(A,child):
		B=child;[A.set_chechked(_B)for A in A._children if A!=B];C=B.checked;A.checked=C;A.value=B.value if C==_A else _E
		if C==_A:A.role.add(_F)
		else:A.role.remove(_F)