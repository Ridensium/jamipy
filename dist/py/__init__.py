from.constructors import Component,Container
from.label import Label,IconAlign
from.spacer import Spacer
from.pill import Pill
from.link import Link
from.image import Image
from.drop_down import DropDown
from.checkers import RadioButton,RadioGroup,CheckBox
from.container_html import ContainerHtml,Wiki,Hashtag
from.card import Card
from.styles import Style,Role
from.device import Device
def jamipy_init(device=True,css=True):
	A=css;global Device
	if device:Device.set_touch();Device.set_device_size();Device.set_user_agent();Device.on_resize();Device.on_network();Device.activate_resize();Device.activate_network()
	if A==True:
		from os import path as B;C=B.abspath(__file__);D=B.dirname(C);E=B.join(D,'jamipy.css')
		with open(E,'r')as F:A=F.read()
	if isinstance(A,str):G=Style('jamipy',A);G.append_to_element()