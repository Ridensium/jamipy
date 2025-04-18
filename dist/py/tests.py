from pyscript import config,display
from.device import Device
from.constructors import Component,Container
from.label import Label,IconAlign
from.spacer import Spacer
from.pill import Pill
from.link import Link
from.image import Image
from.drop_down import DropDown
from.checkers import RadioButton,RadioGroup,CheckBox
from.container_html import ContainerHtml
from.styles import Role
def test_widgets():
	C='click';D=config['type'];A=Container().display()
	def E(*A,container=A):container+=Label(f"{D}: {A}")
	A+=Label(D);E(Device.USER_AGENT);F=Component();F._el.textContent='Component in:'+D;A+=F
	def O(event=None):E(C,event)
	B=Label('Hello World','home');B.text+=':click me';B.add_event_handler(C,O);A+=B;P=Spacer();A+=P;G=Pill('Vitamines');G.parent=A;G.role.add('test');A+=Link('my web page');A+=Image('/test.png',50,50);H={'Ak':100,'Bk':50,'Ck':0};Q={100:'a',50:'b',0:'c'};I=DropDown(H);J=DropDown(Q)
	def K(self):E('value',self.value,'key',self.key)
	I.on_change=K;J.on_change=K;A+=I;A+=J
	def L(cb):print('cur',B.visible);B.visible=not B.visible
	M=CheckBox('check me');M.add_event_handler(C,L);A+=M;N=RadioButton('chose me');N.add_event_handler(C,L);A+=N;R=RadioGroup(H);A.insert(2,R);S='<dir>COOL!!!</dir><widget component="Label" init="\'HTML L TEXT\'"></widget>';T=ContainerHtml(S);A+=T