from.component import Component,Element,el_from_template,create_el
class Container(Component):
	_el=el_from_template({'tag_name':'div','roles':'container'})
	def __init__(A,children=None,*D,**E):
		B=children;A._el=A._el.cloneNode()
		if B:
			for C in B:A.add_child(C)
	def add_child(A,component):A._el.append(component._el)
	def add_child_as_first(A,component):A._el.prepend(component._el)
	def remove_child(A,component):component._el.remove()
	def clear(A):A._el.innerHTML=''
	def __iadd__(A,component):A.add_child(component);return A
	def __isub__(A,component):component.remove();return A