from .label import Label



class Link(Label):

    def __init__(self, text='', icon='', target=None, value=None,  icon_text=None, duotone=None, reverse=False, roles='label'):
        super().__init__(text=text, icon=icon, icon_text=icon_text, duotone=duotone, reverse=reverse, roles=roles)
        self.target = target
        self.value = value
        self.dom.onclick = self.click

    def click(self, event=None):
        try:
            self.target()
        except:
            print(self, 'click with no target')
