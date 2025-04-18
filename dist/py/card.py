from.constructors import Container
from.label import Label
from.image import Image
class Card(Container):
	on_click=None
	def __init__(A,title='',info='',image='',embed=False,landscape=False,width='',height='',square='',image_proportion=None):
		H=landscape;G=title;F=height;E=width;D=square;C=image;B=image_proportion;J=f"container card{" embed"if embed else""}";super().__init__(roles=J);K=Label(G,roles='label card-title');L=Label(info,roles='label card-info');I=Container(roles='container card-content',children=[K,L]);C=Image(C,roles='image card-image');A.title=G;A.image=C;A.content=I;A+=C;A+=I
		if E or F or D:E=D if D else E;F=D if D else F;A.add_style(width=E,height=F)
		if B:
			B=B*100 if B<1 else B;B=f"{B}%"
			if H:C.add_style(width=B)
			else:C.add_style(height=B)
		if H:A.role.add('flex-row')
		if A.on_click:A.add_event_handler('click',A.on_click)