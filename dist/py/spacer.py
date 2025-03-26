from.constructors import Component,Element,make_el_template
class Spacer(Component):
	_el=make_el_template({'tag_name':'div','roles':'spacer'})
	def __init__(A):A._el=A._el.cloneNode()