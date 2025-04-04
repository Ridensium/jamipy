"""
module for providing usefull information about the device like is it touch or offline etc.
some widgets will may need such info to chanche stylin or to be mobile friendly
all that data is avaivable in the class `Device` as well as css classes aded to the body for constants and `data-*` attributes for dynamic values.
"""
from js import window, navigator, document


class Device:
    """
    class for providing the device info to the widgets if needed
    TOUCH - True if device is with touch screen
    D_WIDTH - device screen width
    D_HEIGTH - device screen width
    WIDTH - current window width in pixels 
    HEIGHT - current window height
    PORTRAIT - True if current orientation is such
    LANDSCAPE - True if current orientation is such
    PIXELS - pixel ratio of the screen
    """
    TOUCH:bool = None
    D_WIDTH:int = None
    D_HEIGTH:int = None
    WIDTH:int = None
    HEIGTH:int = None
    LANDSCAPE:bool = None
    PORTRAIT:bool = None
    ONLINE:bool = None
    PIXELS:int = None

    USER_AGENT:str = None


    @classmethod
    def get_user_agent(cls)->str:
        agent = navigator.userAgent
        cls.USER_AGENT = agent
        return agent

    @classmethod
    def set_user_agent(cls)->'Device':
        agent = cls.get_user_agent()
        cls.USER_AGENT = agent
        return cls



    @classmethod
    def get_touch(cls)->bool:
        """
        checking if device is touch, runs once at importing jamipy
        """
        if window.matchMedia('(pointer: coarse)').matches:
                is_touch = True
        elif window.matchMedia('(hover: none)').matches:
                is_touch = True
        else:
                is_touch = False

        return is_touch


    @classmethod
    def set_touch(cls)->'Device':
        """
        checking if device is touch, runs once at importing jamipy
        """
        is_touch = cls.get_touch()

        document.body.classList.add('touch' if is_touch == True else 'no-touch')
        cls.TOUCH = is_touch
        return cls


    @classmethod
    def get_device_size(cls)->tuple[int, int]:
        """
        getting device screen size, runs once at importing jamipy
        and adding classes to the body
        wide - usefull for computer displays with combination of touch
        tall, tall-1 - for portrait screens with less than 1.9 ratio like tablets
        tall, tall-2 - usefull for distinguish smartphones
        """
        screen = window.screen
        width = int(screen.width) # need to be python obj to pass Mock in making docs
        height = int(screen.height)
        return width, height

    @classmethod
    def set_device_size(cls)->'Device':
        """
        getting device screen size, runs once at importing jamipy
        and adding classes to the body
        wide - usefull for computer displays with combination of touch
        tall, tall-1 - for portrait screens with less than 1.9 ratio like tablets
        tall, tall-2 - usefull for distinguish smartphones
        """
        width, height = cls.get_device_size()

        pixels = int(window.devicePixelRatio)

        if width >= height:
            document.body.classList.add('wide')
        else:
            document.body.classList.add('tall')

        if height >= 1.9 * width:
            document.body.classList.add('tall-2')
        elif height >= width:
            document.body.classList.add('tall-1')

        cls.D_HEIGTH = height
        cls.D_WIDTH = width
        cls.PIXELS = pixels
        return cls

    @classmethod
    def on_resize(cls, event=None, *args, **kwargs):
        """runs on window resize and update current size and orientation data"""
        width = int(window.innerWidth)
        height = int(window.innerHeight)
        Device.WIDTH = width
        Device.HEIGTH = height
        portrait = True if height > width else False
        Device.PORTRAIT = portrait
        Device.LANDSCAPE = not portrait
        document.body.dataset.orientation = 'portrait' if portrait == True else 'landscape'
        

    @classmethod
    def on_network(cls, event=None, *args, **kwargs):
        """runs on network status cnanges and update current status"""
        online = navigator.onLine
        Device.ONLINE = online
        document.body.dataset.connection = 'online' if online == True else 'offline'
    



    @classmethod
    def activate_resize(cls):
        window.onresize = cls.on_resize


    @classmethod
    def activate_network(cls):
        window.ononline = cls.on_network
        window.onoffline = cls.on_network