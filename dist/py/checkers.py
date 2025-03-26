_H='children'
_G='check_box_outline_blank'
_F='check_box'
_E='roles'
_D='tag_name'
_C=True
_B=None
_A=False
from.label import Label,IconAlign
from.constructors import Container,Element,make_el_template
class Checker(Label):
	_icons={_C:_F,_A:_G}
	def __init__(A,text='',checked=_A,value=_B,icon_align=IconAlign.NONE,enabled=_C,**D):
		C=enabled;B=checked;super().__init__(text=text,icon=A._icons[B],icon_align=icon_align,**D)
		if C==_A:A.role.replace('enabled','disabled')
		A.checked=B;A.enabled=C;A.value=value;A.add_event_handler('click',A._on_click)
	def _set_checked(A,checked):B=checked;A._el.children[0].textContent=A._icons[B];A.checked=B;A._el.dataset.checked=B
	def _on_click(A,event=_B):
		if A.enabled==_C:A._set_checked(not A.checked)
class RadioButton(Checker):
	_group=_B;_el=make_el_template({_D:'div',_E:'label radio enabled',_H:[{_D:'i','style':{},_E:'icon label-icon radio-icon'},{_D:'span','style':{},_E:'text label-text radio-text'}]});_icons={_C:'radio_button_checked',_A:'radio_button_unchecked'};_parent=_B
	def _on_click(A,event=_B):
		super()._on_click(event);B=A._group
		if B:B._child_changed(child=A)
class CheckBox(Checker):_el=make_el_template({_D:'div',_E:'label checkbox enabled',_H:[{_D:'i',_E:'icon label-icon checkbox-icon'},{_D:'span',_E:'text label-text checkbox-text'}]});_icons={_C:_F,_A:_G}
class RadioGroup(Container):
	def __init__(A,items):
		B=items;super().__init__();A.role.add('radio-group');B={A:A for A in B}if isinstance(B,list)else B
		for(D,E)in B.items():C=RadioButton(text=D,value=E);A.append(C);C._group=A
		A.checked=_A;A.value=_B
	def _child_changed(A,child):B=child;D=A._children;[A._set_checked(_A)for A in D if A!=B];C=B.checked;A.checked=C;A.value=B.value if C==_C else _B;A._el.dataset.checked=C