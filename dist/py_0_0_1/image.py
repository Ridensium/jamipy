_A=None
from.component import Component,Element,el_from_template
class Image(Component):
	_el=el_from_template({'tag_name':'img','roles':'image'})
	def __init__(A,url='',height=_A,width=_A,display_mode=_A,border_radius=_A):B=A._el.cloneNode();B.src=url;A._el=B;A.style(width=width,height=height,displayMode=display_mode,borderRadius=border_radius)