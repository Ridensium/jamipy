from .constructors import Container
from .label import Label
from .image import Image

class Card(Container):
    on_click = None
    def __init__(self, title='', info='', image='', embed=False, landscape=False, width='', height='', square='', image_proportion:int|float=None):
        roles = f'container card{' embed' if embed else ''}'
        super().__init__(roles=roles)

        title_label = Label(title, roles='label card-title')
        info_label = Label(info, roles='label card-info')
        content = Container(roles='container card-content', children=[title_label, info_label])
        image = Image(image, roles='image card-image')

        self.title:str = title
        self.image = image
        self.content = content


        self +=  image
        self += content           

        if width or height or square:
            width = square if square else width
            height = square if square else height
            self.add_style(width=width, height=height)

        if image_proportion:
            image_proportion = image_proportion * 100 if image_proportion < 1 else image_proportion
            image_proportion = f'{image_proportion}%'
            if landscape:
                image.add_style(width=image_proportion)
            else:
                image.add_style(height=image_proportion)


        if landscape:
            self.role.add('flex-row')

        if self.on_click:
            self.add_event_handler('click', self.on_click)


