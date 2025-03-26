_C='tag_name'
_B='hidden'
_A=None
from js import document,Element,DOMTokenList
from.m_enums import*
from pyscript import config
INTERPRETOR=config['type']
if INTERPRETOR=='mpy':0
else:from pyscript.ffi import create_proxy
make_el=document.createElement
def add_event_handler_mpy(component,event_name,handler):component._el.addEventListener(event_name,handler)
def add_event_handler_py(component,event_name,handler):component._el.addEventListener(event_name,create_proxy(handler))
if INTERPRETOR=='mpy':add_event_handler=add_event_handler_mpy
else:add_event_handler=add_event_handler_py
def make_el_template(template):
	el=make_el(template[_C]);el.className=template['roles'];children=template.get('children',[])
	for child in children:el_child=make_el_template(child);el.append(el_child)
	return el
class Component:
	_el=_A;_add_event_handler=add_event_handler;_parent=_A
	def __init__(self,tag_name='div',roles=_A):
		self._el=make_el(tag_name)
		if roles:self.roles=roles
	@property
	def parent(self):return self._parent
	@parent.setter
	def parent(self,parent=_A):
		if parent:parent.append(self)
		elif self._parent:self._parent.remove(self)
	def add_event_handler(self,event_name,handler=_A):
		handler=handler if handler else getattr(self,f"on_{event_name}",_A)
		if handler:self._add_event_handler(event_name,handler)
		return self
	def remove_event_handler(self,event_name=_A,handler=_A,remove_all=False):
		el=self._el
		if event_name and handler:
			if INTERPRETOR=='py':handler=create_proxy(handler)
			el.removeEventListener(event_name,handler)
		elif remove_all:new_el=el.cloneNode(True);el.replaceWith(new_el)
	def add_style(self,border=_A,text_align=_A,tooltip=_A,font=_A,font_size=_A,font_weight=_A,color=_A,background=_A,bold=_A,width=_A,height=_A,italic=_A,**kwargs):
		style=self._el.style;css={'font-weight':font_weight if bold==_A else f"{"bold"if bold==True else"unset"}",'color':color,'width':width if isinstance(width,str)else f"{width}px",'height':height if isinstance(height,str)else f"{height}px",'font_family':font,'font-size':f"{font_size}px"if isinstance(font_size,int)else font_size,'title':tooltip,'background-color':background,'font-style':italic,'text-align':text_align,'border':f"{border}px solid"if isinstance(border,int)else border}
		for(k,v)in kwargs.items():css[k.replace('_','-')]=v
		reset=kwargs.get('_reset',_A);css_text=';'.join([f"{k}:{v}"for(k,v)in css.items()if v!=_A])
		if not reset:style.cssText+=css_text
		else:style.cssText=css_text
		return self
	def get_style(self,name=_A):
		styles=self.el.style.cssText;styles=styles.split(';');result={}
		for style in styles:style=style.split(':');result[style[0]]=style[1]
		return result if name==_A else result.get(name,{})
	def set_style(self,border=_A,text_align=_A,tooltip=_A,font=_A,font_size=_A,font_weight=_A,color=_A,background=_A,bold=_A,width=_A,height=_A,italic=_A,**kwargs):self.add_style(border=border,text_align=text_align,tooltip=tooltip,font=font,font_size=font_size,font_weight=font_weight,color=color,background=background,bold=bold,width=width,height=height,italic=italic,_reset=True,**kwargs)
	@property
	def visible(self):value=self.role.contains(_B);return not value
	@visible.setter
	def visible(self,value):
		print('set',value)
		if value:self.role.remove(_B)
		else:self.role.add(_B)
	@property
	def roles(self):return list(self._el.classList)
	@roles.setter
	def roles(self,roles):_roles=roles if isinstance(roles,str)else' '.join(roles);self._el.className=_roles
	@property
	def role(self):return self._el.classList
	@property
	def size(self):rect=self._el.getBoundingClientRect();return rect.width,rect.height
	def display(self,parent_el=document.body):parent_el.append(self._el);return self
class Container(Component):
	_el=make_el_template({_C:'div','roles':'container'});_children:0
	def __init__(self,children=_A):
		self._el=self._el.cloneNode();self._children=set()
		if children:
			for child in children:self.append(child)
	@property
	def children(self):elements=self._el.children;current=self._children;ordered=sorted(current,key=lambda child:elements.index(child._el));return ordered
	@children.setter
	def children(self,children):self.clear();self.append(children)
	def append(self,children):
		new=children if isinstance(children,list)else[children];current_children=self._children
		for child in new:
			self._el.append(child._el);current_children.add(child)
			if child._parent:child._parent._children.discard(child)
			child._parent=self
		self._children=current_children
	def clear(self):
		self._el.innerHTML=''
		for child in self._children:child._parent=_A
		self._children.clear()
	def count(self):return len(self._children)
	def insert(self,position=0,child=_A):
		count=len(self._children)
		if position==0:self._el.prepend(child._el)
		elif position<count:children_el=list(self._el.children);after_el=children_el[position+1];self._el.insertBefore(child._el,after_el)
		else:self._el.append(child._el)
		self._children.add(child)
		if child._parent:child._parent._children.discard(child)
		child._parent=self
	def pop(self,index=-1):
		children=self.children
		if index>len(children):return
		else:child_pop=children.pop(index);self.remove(child_pop);return child_pop
	def remove(self,children):
		rem=children if isinstance(children,list)else[children];current=self._children
		for child in rem:child._el.remove();child._parent=_A;current.discard(child)
		self._children=current
	def __iadd__(self,component):self.append(component);return self
	def __isub__(self,component):self.remove(component);return self