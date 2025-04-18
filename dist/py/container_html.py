_A=None
from.constructors import Container,Component,Element
from.label import Label
from.spacer import Spacer
from.pill import Pill
from.link import Link
from.image import Image
from.drop_down import DropDown
from.checkers import RadioButton,RadioGroup,CheckBox
class Wiki(Label):
	on_click=_A;no_ext_class=Label;no_ext_path='/';image_class=Image;img_path='/';img_ext=_A;_img_extentions={'jpg','jpeg','bmp','png','webp','svg'}
	def __new__(cls,text='',icon=_A,wiki=_A,show=False):
		if show:instance=cls.show_wiki(text=text,icon=icon,wiki=wiki)
		else:instance=super().__new__(cls)
		return instance
	def __init__(self,text='',icon=_A,wiki=_A,show=_A):
		super().__init__(text,icon)
		if self.on_click:self.add_event_handler('click',self.on_click)
		self.wiki=wiki;self.role.add('label-wiki')
	def on_click(self,event=_A):0
	@classmethod
	def show_wiki(cls,text,icon,wiki):
		wiki_parts=wiki.split('.')
		if len(wiki_parts)==1:return cls.no_ext_class(text=text,icon=icon,wiki=wiki)
		elif wiki_parts[1]in cls._img_extentions:name=wiki_parts[0];img_ext=cls.img_ext;file_name=f"{name}.{img_ext}"if img_ext else wiki;img=cls.image_class(f"{cls.img_path}/{file_name}");return img
class Hashtag(Label):
	hashtag_icon='tag';on_click=_A
	def __init__(self,text='',icon=hashtag_icon):
		super().__init__(text,icon)
		if self.on_click:self.add_event_handler('click',self.on_click)
		self.tag=text;self.role.add('label-hashtag')
class ContainerHtml(Container):
	_allowed={v.__qualname__:v for v in[Label,DropDown,Link,Spacer,Pill,Image,RadioButton,RadioGroup,CheckBox,Wiki,Hashtag]};_html=''
	def __init__(self,html='',slots=_A,roles='container container-html'):
		super().__init__(roles=roles)
		if slots:self._allowed={v.__qualname__:v for v in slots}
		if html:self._html=html;self._build(html)
	@property
	def html(self):return self._html
	@html.setter
	def html(self,value):self._build(value)
	def _build(self,html):
		allowed=self._allowed;temp_el=self._el.cloneNode();temp_el.innerHTML=html;temp_children=set();widgets_el=temp_el.querySelectorAll('widget')
		for w_el in widgets_el:
			child_class=w_el.getAttribute('component')
			if not child_class in allowed:continue
			init=w_el.getAttribute('init');child=eval(f"{child_class}({init})",allowed);w_el.replaceWith(child._el);temp_children.add(child)
		self.clear();self._el.replaceWith(temp_el);self._el=temp_el;self._children=temp_children;self._html=html