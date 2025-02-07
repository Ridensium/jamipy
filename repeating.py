from .container import Container, Component


class RepeitingTemplate(Component):
    #just for testing purpouse
    def __init__(self, roles = 'repeiting-template', *args, **kwargs):
        super().__init__(roles)
        
        for arg in args:
            self.dom.dataset[arg] = arg

        for k,v in kwargs.items():
            self.dom.dataset[k] = v

class Repeating(Container):
    def __init__(self, items:list[dict|list]=None, template:Component=None, roles='repeating'):
        super().__init__(roles)
        items = items if items else []
        
        template = template if template else RepeitingTemplate
        

        for item in items:
            if isinstance(item, dict):
                self >> template(**item)
            elif isinstance(item, list):
                self >> template(*item)
            else:
                self >> template(item)



