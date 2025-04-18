"""
**JAMIPY** - @Ridensium - 2025 - MIT License

UI widget library for building web apps with **PyScript**.

"""

from .constructors import Component, Container
from .label import Label, IconAlign
from .spacer import Spacer
from .pill import Pill
from .link import Link
from .image import Image
from .drop_down import DropDown
from .checkers import RadioButton, RadioGroup, CheckBox
from .container_html import ContainerHtml, Wiki, Hashtag
from .card import Card
from .styles import Style, Role
from .device import Device


def jamipy_init(device=True, css:bool|str=True):
    global Device

    if device:
        Device.set_touch()
        Device.set_device_size()
        Device.set_user_agent()
        Device.on_resize() 
        Device.on_network()
        Device.activate_resize()
        Device.activate_network()

    if css == True:
        from os import path as Path
        script_path = Path.abspath(__file__)
        parent_dir = Path.dirname(script_path)
        css_path = Path.join(parent_dir, 'jamipy.css')
        with open(css_path, 'r') as file:
            css = file.read()

    if isinstance(css, str):
        style = Style('jamipy', css)
        style.append_to_element()
       

