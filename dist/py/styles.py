_A=None
from js import document,Element,CSSStyleSheet
from.constructors import make_el
class Style:
	sheet=_A;id=_A
	def __init__(B,id=_A,css='',url='',parent=_A):
		C=parent
		if url:A=make_el('link');A.rel='stylesheet';A.href=url
		else:A=make_el('style');A.innerHTML=css
		if id:A.id=id;B.id=id
		B._el=A
		if C==True:B.append_to_element()
		elif C:B.append_to_element(C)
	def append_to_element(A,parent=document.head):
		B=parent;id=A.id
		if id:
			C=document.getElementById(id)
			if C:A._el=C
			else:B.append(A._el)
		else:B.append(A._el)
		A.sheet=A._el.sheet
class Role:
	roles={};index:0;data:0;name:0;_sheet=_A
	def __new__(B,role_name,**D):
		C=role_name
		if not B._sheet:E=Style('jamipy-roles');E.append_to_element();B._sheet=E.sheet
		A=B.roles.get(C,_A)
		if not A:
			A=super().__new__(B);A.name=C;A.index=_A;A.data={}
			if D:A.set_style(**D)
			B.roles[C]=A
		return A
	def __init__(B,role_name,**A):
		if A:B.set_style(**A)
	def __call__(A,*B,**C):return A.name
	def __str__(A):return f"{A.name} - {A.data}"
	def set_style(D,border=_A,text_align=_A,tooltip=_A,font=_A,font_size=_A,font_weight=_A,color=_A,background=_A,bold=_A,width=_A,height=_A,italic=_A,**G):
		F=font_size;E=border;B=height;A=width;C={'font-weight':font_weight if bold==_A else f"{"bold"if bold==True else""}",'color':color,'width':A if isinstance(A,str)else f"{A+"px"if A else""}",'height':B if isinstance(B,str)else f"{B+"px"if B else""}",'font_family':font,'font-size':f"{F}px"if isinstance(F,int)else F,'title':tooltip,'background-color':background,'font-style':italic,'text-align':text_align,'border':f"{E}px solid"if isinstance(E,int)else E};C={B:A for(B,A)in C.items()if A}
		for(H,I)in G.items():C[H]=I
		D.data=C;D.update_style();return D
	def update_style(A):
		B=A._sheet;F=A.data;D=''
		for(G,H)in F.items():D+=f"{G}:{H};"
		I=f".{A.name} {{ {D} }}";J=B.cssRules.length;E=B.insertRule(I,J);C=A.index
		if C or C==0:B.deleteRule(C);A.index=E-1
		else:A.index=E
	def add_style(A,key,value):A.data[key]=value;A.update_style();return A
	def remove_style(A,key):A.data.pop(key,_A);A.update_style();return A
	def clear(A):
		B=A.index;C=A._sheet
		if B and C:C.deleteRule(B)
		return A