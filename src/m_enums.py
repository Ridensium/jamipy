"""
enum like data classes
micropython hasn't enum
they are only to help of autosugestion typing
"""


class Align: # no enum in micropython
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'
    NONE = None

class IconAlign:
    LEFT = 'row'
    RIGHT = 'row-reverse'
    TOP = 'column'
    BOTTOM = 'column-reverse'
    NONE = ''


class Events:
    #because seting them with attribute will have on at begining
    CLICK = 'click'


class Justify:
    #justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left | right ... + safe | unsafe;
    START:str = 'flex-start'
    END:str = 'flex-end'
    CENTER:str = 'center'
    BETWEEN:str = 'space-between'
    AROUND:str = 'space-around'
    EVENLY:str = 'space-evenly'
    LEFT:str = 'left'
    RIGHT:str = 'right'