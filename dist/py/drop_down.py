_C='tag_name'
_B=True
_A=None
from.constructors import Component,Container,Element,Events,make_el_template
class DropDownOption(Component):
	_el=make_el_template({_C:'option','roles':'dropdown-option'})
	def __init__(B,value=_A,text='',selected=False):
		D=value;A=text;A=A if A else D;C=B._el.cloneNode();B._el=C;C.setAttribute('value',D);C.textContent=A;B.value=D;B.text=A
		if selected:C.selected=_B
class DropDown(Container):
	_el=make_el_template({_C:'select','roles':'dropdown'});_items={};value=_A;key=_A
	def __init__(A,items=_A,selected_value=_A,include_placeholder=_B,placeholder='',enabled=_B,roles=_A):
		D=roles;B=items;G=A._el.cloneNode();A._el=G;A._children=set();B=B if B else[];B={A:A for A in B}if isinstance(B,list)else B;E={}
		for(C,F)in B.items():H=_B if C==selected_value else False;I=DropDownOption(text=F,value=C,selected=H);A.append(I);E.update({str(F):C})
		A._items=E;A.add_event_handler('change',A._on_change)
		if D:A._el.className=D
	def _on_change(A,event):B=A._el.value;C=A._items.get(B,_A);A.value=B;A.key=C