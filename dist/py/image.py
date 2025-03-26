_A=None
from.constructors import Component,Element,make_el_template
class Image(Component):
	_el=make_el_template({'tag_name':'img','roles':'image'})
	def __init__(A,url='',height=_A,width=_A,display_mode=_A,border_radius=_A):B=A._el.cloneNode();B.src=url;A._el=B;A.set_style(width=width,height=height,displayMode=display_mode,borderRadius=border_radius)