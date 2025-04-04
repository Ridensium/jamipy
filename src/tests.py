from pyscript import config, display

from .device import Device
from .constructors import Component, Container

from .label import Label, IconAlign
from .spacer import Spacer
from .pill import Pill
from .link import Link
from .image import Image
from .drop_down import DropDown
from .checkers import RadioButton, RadioGroup, CheckBox
from .container_html import ContainerHtml
from .styles import Role



def test_widgets():




    interpretor = config['type']

    lr = Role('label', color='red', outline='2px solid gray')

    print(lr)
  
    #test Container
    container = Container().display()
 
  
    #modify print
    def display(*args, container=container):
        container += Label(f'{interpretor}: {args}')

    container += Label(interpretor).add_style(background='lightgreen', font_size=34)

    #test Device
    display(Device.USER_AGENT)

    #test Component
    component = Component()
    component.add_style(width=100, height=100, background='pink')
    component._el.textContent = 'Component in:' + interpretor
    container += component

    #test Label
    def click(event=None):
        display('click', event)

    label = Label('Hello World', 'home')
    label.text += ':click me'
    label.add_event_handler('click', click)
    container += label



    #test Spacer
    spacer = Spacer()
    container += spacer

    #test Pill
    pill = Pill('Vitamines')
    pill.parent = container
    pill.role.add('test')

    #test Link
    container += Link('my web page')

    #test Image
    container += Image('/test.png', 50, 50)

    #test DropDown
    dd_data = {'A':100, 'B':50, 'C':0}
    dd_data2 = {100:'a', 50:'b', 0:'c'}
    drop_down = DropDown(dd_data)
    drop_down2 = DropDown(dd_data2)

    def print_value(dd:DropDown):
        display('dd value', dd.value, 'dd key', dd.key)

    drop_down.on_change = print_value
    drop_down2.on_change = print_value

    container += drop_down
    container += drop_down2
    
    #test CheckBox
    def toggle_label(cb):
        print('cur', label.visible)
        label.visible = not label.visible
    check_box = CheckBox('check me')
    check_box.add_event_handler('click', toggle_label)
    container += check_box


    #test RadioButton
    radio_button = RadioButton('chose me')
    radio_button.add_event_handler('click', toggle_label)
    container += radio_button


    #test Radio Group
    radio = RadioGroup(dd_data)
    container.insert(2, radio)

 
 
    
    html = """<dir>COOL!!!</dir><widget component="Label" init="'HTML L TEXT'"></widget>"""
    ch = ContainerHtml(html)
    container += ch
    #print(interpretor, ch)
    #ch.display()
    #print(ch.allowed)

    #print(interpretor, locals().keys())