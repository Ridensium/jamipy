_B=True
_A=None
from js import window,navigator,document
class Device:
	TOUCH=_A;D_WIDTH=_A;D_HEIGTH=_A;WIDTH=_A;HEIGTH=_A;LANDSCAPE=_A;PORTRAIT=_A;ONLINE=_A;PIXELS=_A;USER_AGENT=_A
	@classmethod
	def get_user_agent(B):A=navigator.userAgent;B.USER_AGENT=A;return A
	@classmethod
	def set_user_agent(A):B=A.get_user_agent();A.USER_AGENT=B;return A
	@classmethod
	def get_touch(B):
		if window.matchMedia('(pointer: coarse)').matches:A=_B
		elif window.matchMedia('(hover: none)').matches:A=_B
		else:A=False
		return A
	@classmethod
	def set_touch(A):B=A.get_touch();document.body.classList.add('touch'if B==_B else'no-touch');A.TOUCH=B;return A
	@classmethod
	def get_device_size(D):A=window.screen;B=int(A.width);C=int(A.height);return B,C
	@classmethod
	def set_device_size(A):
		B,C=A.get_device_size();D=int(window.devicePixelRatio)
		if B>=C:document.body.classList.add('wide')
		else:document.body.classList.add('tall')
		if C>=1.9*B:document.body.classList.add('tall-2')
		elif C>=B:document.body.classList.add('tall-1')
		A.D_HEIGTH=C;A.D_WIDTH=B;A.PIXELS=D;return A
	@classmethod
	def on_resize(D,event=_A,*E,**F):B=int(window.innerWidth);C=int(window.innerHeight);Device.WIDTH=B;Device.HEIGTH=C;A=_B if C>B else False;Device.PORTRAIT=A;Device.LANDSCAPE=not A;document.body.dataset.orientation='portrait'if A==_B else'landscape'
	@classmethod
	def on_network(B,event=_A,*C,**D):A=navigator.onLine;Device.ONLINE=A;document.body.dataset.connection='online'if A==_B else'offline'
	@classmethod
	def activate_resize(A):window.onresize=A.on_resize
	@classmethod
	def activate_network(A):window.ononline=A.on_network;window.onoffline=A.on_network