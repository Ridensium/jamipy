_B='tag_name'
_A=None
from.component import Component,Element,Events,el_from_template
from.container import Container
class DropDownOption(Component):
	_el=el_from_template({_B:'option','roles':'dropdown-option'})
	def __init__(A,value=_A,key=''):C=value;B=A._el.cloneNode();A._el=B;B.setAttribute('value',C);B.textContent=key;A.value=C;A.key=key
class DropDown(Container):
	_el=el_from_template({_B:'select','roles':'dropdown'});_items={};value=_A;key=_A
	def __init__(A,items=_A,selected_value=_A,include_placeholder=True,placeholder='',enabled=True):
		B=items;F=A._el.cloneNode();A._el=F;B={A:A for A in B}if isinstance(B,list)else B;C={}
		for(D,E)in B.items():G=DropDownOption(key=D,value=E);A.add_child(G);C.update({str(E):D})
		A._items=C;A.set_event_handler('change',A.change)
	def change(A,event):B=A._el.value;C=A._items.get(B,_A);A.value=B;A.key=C