_D='tag_name'
_C='value'
_B=True
_A=None
from.constructors import Component,Container,Element,Events,make_el_template
from.label import Label
class DropDownOption(Component):
	_el=make_el_template({_D:'option','roles':'dropdown-option'})
	def __init__(B,value=_A,text='',selected=False):
		D=value;A=text;A=A if A else D;C=B._el.cloneNode();B._el=C;C.setAttribute(_C,D);C.textContent=A;B.value=D;B.text=A
		if selected:C.selected=_B
class DropDownSelect(Container):
	_el=make_el_template({_D:'select','roles':'dropdown-select'});_items={};value=_A;key=_A
	def __init__(B,items=_A,selected_value=_A,include_placeholder=_B,placeholder='',enabled=_B):
		A=items;F=B._el.cloneNode();B._el=F;B._children=set();A=A if A else[];A={A:A for A in A}if isinstance(A,list)else A;E={};C=0
		for(D,G)in A.items():H=_B if D==selected_value else False;I=DropDownOption(text=str(D),value=C,selected=H);B.append(I);J={C:{'key':D,_C:G}};E.update(J);C+=1
		B._items=E;B.add_event_handler('change',B._on_change)
	def _on_change(A,event=_A):D=A._el.value;B=A._items[int(D)];E=B['key'];F=B[_C];A.value=F;A.key=E;C=A.parent;C.on_change(C)
class DropDown(Container):
	_items={};value=_A;key=_A
	def __init__(A,items=_A,selected_value=_A,include_placeholder=_B,placeholder='',enabled=_B,icon='expand_all'):super().__init__();A.role.add('dropdown');C=DropDownSelect(items,selected_value,include_placeholder,placeholder,enabled);A+=C;A.select=C;B=Label(icon=icon);B.role.add('dropdown-label');A+=B;A.label=B
	def on_change(A,*B,**C):0
	@property
	def value(self):return self.select.value
	@property
	def key(self):return self.select.key