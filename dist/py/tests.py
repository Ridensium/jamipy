def test_widgets():
	C='click';from pyscript import config as Q;from.device import Device as R;from.constructors import Component as S,Container as T;from.label import Label as D,IconAlign;from.spacer import Spacer as U;from.pill import Pill;from.link import Link;from.image import Image;from.drop_down import DropDown as H;from.checkers import RadioButton as V,RadioGroup as W,CheckBox as X;E=Q['type'];A=T().display()
	def F(*A,container=A):container+=D(f"{E}: {A}")
	A+=D(E).add_style(background='lightgreen',font_size=34);I=R();Y=[A for A in dir(I)if not A.startswith('_')];F({A:getattr(I,A,None)for A in Y});G=S();G.add_style(width=100,height=100,background='pink');G._el.textContent='Component in:'+E;A+=G
	def Z(event=None):F(C,event)
	B=D('Hello World','home');B.text+=':click me';B.add_event_handler(C,Z);A+=B;a=U();A+=a;b=Pill('Vitamines');b.parent=A;A+=Link('my web page');A+=Image('/test.png',50,50);J={'A':100,'B':50,'C':0};c={100:'a',50:'b',0:'c'};K=H(J);L=H(c)
	def M(dd):F('dd value',dd.value,'dd key',dd.key)
	K.on_change=M;L.on_change=M;A+=K;A+=L
	def N(cb):print('cur',B.visible);B.visible=not B.visible
	O=X('check me');O.add_event_handler(C,N);A+=O;P=V('chose me');P.add_event_handler(C,N);A+=P;d=W(J);A.insert(2,d)