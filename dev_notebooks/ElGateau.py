#!/usr/bin/env python

"""ElGateau.py:A Framework for Using the Elgato Stream Deck for Experimental Psychology Research."""

__author__      = "Christopher Madan"
__copyright__   = "Copyright 2017, Christopher Madan"

__license__ = "MIT"
__version__ = "0.0.8"
__maintainer__ = "Christopher Madan"
__email__ = "christopher.madan@nottingham.ac.uk"
__status__ = "Development"


# define constants
HID_VENDOR = 4057
HID_PRODUCT = 96

NUM_KEYS = 15;
ICON_SIZE = 72,72

NUM_TOTAL_PIXELS = ICON_SIZE[0]*ICON_SIZE[1];
NUM_PAGE1_PIXELS = 2583;
NUM_PAGE2_PIXELS = NUM_TOTAL_PIXELS-NUM_PAGE1_PIXELS;

RESET_DATA = [0x0B, 0x63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
BRIGHTNESS_DATA = [0x05, 0x55, 0xAA, 0xD1, 0x01, 0x0A, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

HEADER_PAGE1 = [0x02, 0x01, 0x01, 0x00, 0x00, 0, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42, 0x4d, 0xf6, 0x3c, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x36, 0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x48, 0x00, 0x00, 0x00, 0x48, 0x00, 0x00, 0x00, 0x01, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x3c, 0x00, 0x00, 0xc4, 0x0e, 0x00, 0x00, 0xc4, 0x0e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
HEADER_PAGE2 = [0x02, 0x01, 0x02, 0x00, 0x01, 0]

KEY_BLANK = icon_solid();


# dependencies
import os, hid
import numpy as np
from PIL import Image,ImageDraw,ImageFont

# functions

def open():
    """
    Open initial connection to Elgato Stream Deck device.
    
    Returns
    ----------
    elg : USB HID handle
        Required to pass commands to the device.
    """
    elg = hid.device(HID_VENDOR, HID_PRODUCT)
    elg.open(HID_VENDOR, HID_PRODUCT)
    return (elg)


def reset(elg):
    """
    Send reset command.
    
    Inputs
    ----------
    elg : USB HID handle
    """
    elg.send_feature_report(RESET_DATA)
    
def set_brightness(elg,bright):
    """
    Set brightness of displays.
    
    Inputs
    ----------
    elg : USB HID handle
    bright : int, 0-100
        Brightness value to set LCD display to.
    """
    BRIGHTNESS_DATA[5] = bright
    elg.send_feature_report(BRIGHTNESS_DATA)
    
    
def icon_prep(icon,pad=0):
    """
    Prepare icon (read from file, pad, resize).
    
    Inputs
    ----------
    icon : Filename for icon to prepare, needs to be a PNG in the "icons" folder.
    bright : px
        Pad the icon before resizing, this way the icon doesn't go right to edge of display.
        
    Returns
    ----------
    ico : 72x72 RGBA image
    """
    # read icon
    ico = Image.open(os.path.join("icons",icon+".png"))

    # pad with blank space if don't know
    padded_size = ico.size[0]+pad,ico.size[1]+pad
    padded_im = Image.new("RGBA", padded_size)
    padded_im.paste(ico, (int((padded_size[0]-ico.size[0])/2),int((padded_size[1]-ico.size[1])/2)))
    ico = padded_im

    # ensure final image is 72x72
    ico.thumbnail(ICON_SIZE)
    return (ico)


def icon_text(ico,text,font='VeraMono-Bold',col='000000',size=14):
    """
    Overlay text over icon.
    
    Inputs
    ----------
    ico : 72x72 RGBA image
        Should have been output from icon_prep or icon_solid.
    text : str
        Text to write.
    font: Font filename, should be in "fonts" folder. Optional.
    col: Hex color code for text. Optional.
    size: Font size. Optional.
    
    Returns
    ----------
    ico : 72x72 RGBA image
    """
    # underlay
    base = ico

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # setup font
    fnt = ImageFont.truetype(os.path.join("fonts",font+".ttf"), size)
    (r,g,b)=bytes.fromhex(col)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # write text
    d.text((0,30), text, font=fnt, fill=(r,g,b,255))
    # even after the recent patch, text align doesn't seem to work
    # https://github.com/python-pillow/Pillow/pull/2641
    # no error in PIL 4.3.0, but also doesn't seem to actually affect alignment
    
    # flatten background and text
    ico = Image.alpha_composite(base, txt)
    
    return (ico)
    
def icon_solid(col='000000'):
    """
    Create a icon that is a solid color.
    
    Inputs
    ----------
    col: Hex color string for text.
    
    Returns
    ----------
    ico : 72x72 RGBA image
    """
    # make blank image of a solid color
    (r,g,b)=bytes.fromhex(col)
    ico = Image.new('RGBA', ICON_SIZE, (r,g,b,255))
    return ico

def key_display(elg,key,ico):
    """
    Push an icon to a key on the device.
    
    Inputs
    ----------
    elg : USB HID handle
    key : int, key number on device (1-15)
    ico : 72x72 RGBA image
    """
    # icon gets written to display from right to left, 
    # so need to mirror it before sending so it looks correct
    ico = ico.transpose(Image.FLIP_LEFT_RIGHT)

    # buffer pixel data into a list and shuffle colors to BGR
    icobuffer = list(ico.getdata()) # RGBA
    pixels = np.array([])
    for px in range(0, NUM_TOTAL_PIXELS):
        r = icobuffer[px][0]
        g = icobuffer[px][1]
        b = icobuffer[px][2]
        pixels = np.concatenate([pixels,np.array([b,g,r])])

    # remap the key locations to make more sense
    key = key_remap(key)
    
    # send pixel data to elg
    header = HEADER_PAGE1
    header[5] = key
    msg = header+pixels[range(0,NUM_PAGE1_PIXELS*3)].astype(int).tolist()
    elg.write(msg)

    header = HEADER_PAGE2
    header[5] = key
    msg = header+pixels[range((NUM_PAGE1_PIXELS-3)*3-1,NUM_TOTAL_PIXELS*3)].astype(int).tolist()
    elg.write(msg)

def key_clear(elg,key):
    """
    Clears the display for a key on the device.
    
    Inputs
    ----------
    elg : USB HID handle
    key : int, key number on device (1-15)
    """
    key_display(elg,key,KEY_CLEAR)
    
def key_remap(key):
    """
    Remaps key numbers.
    
    Inputs
    ----------
    key : int, key number on device (1-15)
    (5,4,3,2,1,10,9,8,7,6,15,14,13,12,11)
    OR
    (int,int) for (row,column) notation (1-3,1-5)

    Returns
    ----------
    key : int, key number on device (1-15)
    (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    """
    if len(key) == 1
        # simple remap of left-right ordering
        key = (np.floor((key-1)/5))*5 + (5-(np.mod(key-1,5)))
    elif len(key) == 2
        # (r,c) notation
        key = (key[0]-1)*5 + key[1]
    return (int(key))






