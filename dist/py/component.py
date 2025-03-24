_C='hidden'
_B=False
_A=None
from js import document,Element,DOMTokenList
from.m_enums import*
create_el=document.createElement
def el_from_template(template=_A):
	el=create_el(template['tag_name']);el.className=template['roles'];children=template.get('children',[])
	for child in children:el_child=el_from_template(child);el.append(el_child)
	return el
class Component:
	_el=_A
	def __init__(self,tag_name='div',roles=_A):
		self._el=create_el(tag_name)
		if roles:self.roles=roles
	def set_parent(self,parent,at_begining=_B):
		if at_begining==_B:parent._el.append(self._el)
		else:parent._el.prepend(self._el)
	def remove(self):self._el.remove()
	def set_event_handler(self,event_name,handler):setattr(self._el,f"on{event_name}",handler)
	def get_event_handler(self,event_name):return getattr(self._el,f"on{event_name}",_A)
	def style(self,border=_A,text_align=_A,tooltip=_A,font=_A,font_size=_A,font_weight=_A,color=_A,background=_A,bold=_A,width=_A,height=_A,italic=_A,**kwargs):
		style=self._el.style;css={'font-weight':font_weight if bold==_A else f"{"bold"if bold==True else"unset"}",'color':color,'width':width if isinstance(width,str)else f"{width}px",'height':height if isinstance(height,str)else f"{height}px",'font_family':font,'font-size':font_size,'title':tooltip,'background-color':background,'font-style':italic,'text-align':text_align,'border':f"{border}px solid"if isinstance(border,int)else border}
		for(k,v)in kwargs.items():css[k.replace('_','-')]=v
		print(css);style.cssText+=';'.join([f"{k}:{v}"for(k,v)in css.items()if v!=_A]);return self
	def get_style(self,name=_A):
		styles=self.el.style.cssText;styles=styles.split(';');result={}
		for style in styles:style=style.split(':');result[style[0]]=style[1]
		return result if name==_A else result.get(name,{})
	@property
	def visible(self):return self.role.contains(_C)
	@visible.setter
	def visible(self,value):
		if value==_B:self.role.add(_C)
		else:self.role.remove(_C)
	@property
	def roles(self):return list(self._el.classList)
	@roles.setter
	def roles(self,roles):_roles=roles if isinstance(roles,str)else' '.join(roles);self._el.className=_roles
	@property
	def role(self):return self._el.classList
	@property
	def get_size(self):rect=self._el.getBoundingClientRect();return rect.width,rect.height
	def display(self,parent_el=document.body):parent_el.append(self._el);return self