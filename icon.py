from .component import Component, Dom


class Icon(Component):
    def __init__(self, icon='', text='', notification:bool=False, duotone=False, roles='icon'):
        super().__init__(tag='span', roles=roles)
        dom:Dom = self.dom

        dom.dataset.icon = icon

        if text:
            dom.dataset.text = text
        
        if duotone:
            dom.dataset.duotone = icon * 2

        if notification:
            dom.classList.add('icon-notification')



    @property
    def icon(self):
        return self.dom.dataset.icon


    @icon.setter
    def icon(self, icon:str=None):
        self.dom.dataset.icon = icon if icon else ''


    @property
    def text(self):
        return self.dom.dataset.text


    @text.setter
    def text(self, text:str=''):
        if text:
            self.dom.dataset.text = text
        else:
            self.dom.removeAttribute('data-text')
        
    @property
    def notification(self):
        return self.roles.contains('icon-notification')


    @notification.setter
    def notification(self, notification:bool=False):
        if notification == True:
            self.duotone = False
            self.roles.add('icon-notification')
        else:
            self.roles.remove('icon-notification')

    @property
    def duotone(self):
        return self.roles.contains('icon-duotone')

    

    @duotone.setter
    def duotone(self, duotone:bool):
        if duotone==True:
            self.notification = False
            self.dom.dataset.duotone = self.dom.dataset.icon * 2
        else:
            self.dom.removeAttribute('data-duotone')
