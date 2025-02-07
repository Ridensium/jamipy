from .text import Text, Component
from .icon import Icon

class Label(Component):

    def __init__(self, text='', icon='', icon_text=None, duotone=None, reverse=False, roles='label', tag='span'):
        super().__init__(roles=roles, tag=tag)
        dom = self.dom
        icon = Icon(icon=icon, text=icon_text, duotone=duotone, roles='icon label-icon')
        text = Text(text=text, roles='text label-text')

        dom.append(icon.dom)
        if reverse == True:
            dom.prepend(text.dom)
        else:
            dom.append(text.dom)


        self.icon = icon
        self.text = text

        
        


