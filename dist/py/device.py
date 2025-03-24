_A=True
from js import window,navigator,document
class Device:TOUCH:0;D_WIDTH:0;D_HEIGTH:0;WIDTH:0;HEIGTH:0;LANDSCAPE:0;PORTRAIT:0;ONLINE:0;PIXELS:0
def touch():
	if window.matchMedia('(pointer: coarse)').matches:A=_A
	elif window.matchMedia('(hover: none)').matches:A=_A
	else:A=False
	document.body.classList.add('touch'if A==_A else'no-touch');Device.TOUCH=A
touch()
def device_size():
	C=window.screen;A=int(C.width);B=int(C.height);D=int(window.devicePixelRatio)
	if A>=B:document.body.classList.add('wide')
	else:document.body.classList.add('tall')
	if B>=1.9*A:document.body.classList.add('tall-2')
	elif B>=A:document.body.classList.add('tall-1')
	Device.D_HEIGTH=B;Device.D_WIDTH=A;Device.PIXELS=D
device_size()
def resize(event=None,*D,**E):B=int(window.innerWidth);C=int(window.innerHeight);Device.WIDTH=B;Device.HEIGTH=C;A=_A if C>B else False;Device.PORTRAIT=A;Device.LANDSCAPE=not A;document.body.dataset.orientation='portrait'if A==_A else'landscape'
resize()
window.onresize=resize
def network(event=None,*B,**C):A=navigator.onLine;Device.ONLINE=A;document.body.dataset.connection='online'if A==_A else'offline'
network()
window.ononline=network
window.onoffline=network