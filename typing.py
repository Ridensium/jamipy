class Document:
    body:'Dom'
    head:'Dom'
    def createElement(tag:str)->'Dom':pass

class Screen:
    width:int
    height:int

class Window:
    document:Document
    screen:Screen
    onresize:callable
    def matchMedia(arg:str):pass

class classList:
    def add(value:str):pass
    def remove(value:str):pass
    def replace(value:str):pass
    def toggle(value:str):pass
    def contains(value:str):pass

class Dataset:
    icon:str
    icon2:str
    duotone:str

class Style:
    fontSize:str

class Dom:
    id:str
    textContent:str
    src:str
    dataset:Dataset
    onclick:callable
    classList:classList
    style:Style
    className:str
    parentElement:'Dom'
    children:list['Dom']
    innerHTML:str
    offsetWidth:int
    offsetHeight:int
    def setAttribute(name:str, value:str):pass
    def removeAttribute(name:str):pass
    def append(dom:'Dom'):pass
    def prepend(dom:'Dom'):pass
    def hasOwnProperty(arg:str)->bool:pass
    def cloneNode(arg:bool)->'Dom':pass
    def append(arg:'Dom')->None:pass
    def remove()->None:pass
    def getElementById(arg:str):pass
    def replaceWith(dom:'Dom'):pass