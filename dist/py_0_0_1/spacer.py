from.component import Component,Element,el_from_template
class Spacer(Component):
	_el=el_from_template({'tag_name':'div','roles':'spacer'})
	def __init__(A):A._el=A._el.cloneNode()