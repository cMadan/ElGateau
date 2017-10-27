#!/usr/bin/env python

"""ElGateau.py:A Framework for Using the Elgato Stream Deck for Experimental Psychology Research."""

__author__      = "Christopher Madan"
__copyright__   = "Copyright 2017, Christopher Madan"

__license__ = "MIT"
__version__ = "0.0.6"
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

# dependencies
import os, hid
import numpy as np
from PIL import Image,ImageDraw,ImageFont

# functions

def open():
    """open initial connection to device"""
    elg = hid.device(HID_VENDOR, HID_PRODUCT)
    elg.open(HID_VENDOR, HID_PRODUCT)
    return (elg)


def reset(elg):
    """send reset command"""
    elg.send_feature_report(RESET_DATA)
    
def set_brightness(elg,bright):
    """set brightness to 'bright'"""
    BRIGHTNESS_DATA[5] = bright
    elg.send_feature_report(BRIGHTNESS_DATA)
    
    
def icon_prep(icon,pad=0):
    """prepare icon (read from file, pad, resize)"""
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
    """overlay text over icon"""
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
    
def icon_solid(col):
    """create a icon that is a solid color"""
    # make blank image of a solid color
    (r,g,b)=bytes.fromhex(col)
    ico = Image.new('RGBA', ICON_SIZE, (r,g,b,255))
    return ico

def key_display(elg,key,ico):
    """push an icon to a key on the device"""
    # icon gets mirrored, so need to flip
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

def key_remap(key):
    """remaps key numbers to a more intuitive order"""
    key = (np.floor((key-1)/5))*5 + (5-(np.mod(key-1,5)))
    return (int(key))






