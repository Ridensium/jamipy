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
    TOUCH:bool
    D_WIDTH:int
    D_HEIGTH:int
    WIDTH:int
    HEIGTH:int
    LANDSCAPE:bool
    PORTRAIT:bool
    ONLINE:bool
    PIXELS:int

def touch():
    """
    checking if device is touch, runs once at importing jamipy
    """
    if window.matchMedia('(pointer: coarse)').matches:
            is_touch = True
    elif window.matchMedia('(hover: none)').matches:
            is_touch = True
    else:
            is_touch = False

    document.body.classList.add('touch' if is_touch == True else 'no-touch')
    Device.TOUCH = is_touch

touch()

def device_size():
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
    pixels = int(window.devicePixelRatio)

    if width >= height:
        document.body.classList.add('wide')
    else:
        document.body.classList.add('tall')

    if height >= 1.9 * width:
        document.body.classList.add('tall-2')
    elif height >= width:
        document.body.classList.add('tall-1')

    Device.D_HEIGTH = height
    Device.D_WIDTH = width
    Device.PIXELS = pixels

device_size()

def resize(event=None, *args, **kwargs):
    """runs on window resize and update current size and orientation data"""
    width = int(window.innerWidth)
    height = int(window.innerHeight)
    Device.WIDTH = width
    Device.HEIGTH = height
    portrait = True if height > width else False
    Device.PORTRAIT = portrait
    Device.LANDSCAPE = not portrait
    document.body.dataset.orientation = 'portrait' if portrait == True else 'landscape'

resize() 
window.onresize = resize

def network(event=None, *args, **kwargs):
    """runs on network status cnanges and update current status"""
    online = navigator.onLine
    Device.ONLINE = online
    document.body.dataset.connection = 'online' if online == True else 'offline'

network()
window.ononline = network
window.onoffline = network



