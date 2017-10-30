#!/usr/bin/env python

"""ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research."""

__author__      = "Christopher Madan"
__copyright__   = "Copyright 2017, Christopher Madan"

__license__ = "MIT"
__version__ = "0.3.0"
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

# import dependencies
import os, hid, time
import numpy as np
from PIL import Image,ImageDraw,ImageFont

class ElGateau(object):
    """ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research."""

    # functions

    ########################################
    # 
    # Basic device interaction functions
    # 
    # open, reset, set_brightness, key_remap
    # 
    ########################################

    def __init__(self):
        """
        Open initial connection to Elgato Stream Deck device.
        """
        self.device = hid.device(HID_VENDOR, HID_PRODUCT)
        self.device.open(HID_VENDOR, HID_PRODUCT)
        
        # pre-generate a blank key for later functions
        self.KEY_BLANK = self.icon_solid();

    def __exit_(self):
        """
        Close connection to Elgato Stream Deck device.
        """
        self.device.close()
        
    def reset(self):
        """
        Send reset command.
        """
        self.device.send_feature_report(RESET_DATA)

    def set_brightness(self,bright):
        """
        Set brightness of displays.

        Parameters
        ----------
        bright : int, 0-100
            Brightness value to set LCD display to.
        """
        BRIGHTNESS_DATA[5] = bright
        self.device.send_feature_report(BRIGHTNESS_DATA)

    def key_remap(self,key):
        """
        Remaps key numbers.

        Parameters
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
        if type(key) == int:
            # simple remap of left-right ordering
            key = (np.floor((key-1)/5))*5 + (5-(np.mod(key-1,5)))
        elif type(key) == tuple:
            # (r,c) notation
            key = (key[0]-1)*5 + key[1]
            key = self.key_remap(key) # still need to re-map ordering
        return (int(key))    


    ########################################
    # 
    # Icon generation functions
    #
    # icon_solid, icon_prep, icon_text
    # 
    ########################################

    def hex2rgb(self,col):
        """
        Convert from hex color string to (r,g,b) tuple.

        Parameters
        ----------
        col : Hex color string for background.

        Returns
        ----------
        (r,g,b) : tuple (0-255,0-255,0-255)
        """
        if type(col)==tuple:
            # assume this is RGB in (0-1) format
            # not an intended input, but we can work with it
            (r,g,b) = np.array(col)*255
            return (r,g,b)

        # if preceded by a '#', remove it
        col = col.replace('#','')

        (r,g,b)=bytes.fromhex(col)
        return (r,g,b)

    def icon_solid(self,col='000000'):
        """
        Create a icon that is a solid color.

        Parameters
        ----------
        col : Hex color string for background.

        Returns
        ----------
        ico : 72x72 RGBA image
        """
        # make blank image of a solid color
        (r,g,b)=self.hex2rgb(col)
        ico = Image.new('RGBA', ICON_SIZE, (r,g,b,255))
        return ico

    def icon_prep(self,icon,pad=0):
        """
        Prepare icon (read from file, pad, resize).

        Parameters
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

    def icon_text(self,text,position=(31,31),ico=None,col='ffffff',back='000000',font='VeraMono-Bold',size=14):
        """
        Overlay text over icon.

        Parameters
        ----------
        text : str
            Text to write.
        ico : 72x72 RGBA image
            Should have been output from icon_prep or icon_solid.
            Optional, defaults to black background.
        col : Hex color code string for text.
            Optional, defaults to white ('ffffff').
        back : Hex color string for background.
            Optional, defaults to black ('000000').
        font : Font filename, should be in "fonts" folder. 
            Optional, defaults to VeraMono-Bold.
        size : Font size. 
            Optional, defaults to 14.

        Returns
        ----------
        ico : 72x72 RGBA image
        """
        # make a solid color background if necessary
        if back != '000000':
            ico = self.icon_solid(back)
        elif ico is None:
            ico = self.KEY_BLANK
            
        # underlay
        base = ico

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', base.size, (255,255,255,0))

        # setup font
        fnt = ImageFont.truetype(os.path.join("fonts",font+".ttf"), size)
        (r,g,b)=self.hex2rgb(col)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # write text
        # even after the recent patch, text align doesn't seem to work
        # https://github.com/python-pillow/Pillow/pull/2641
        # no error in PIL 4.3.0, but also doesn't seem to actually affect alignment
        w,h=d.textsize(text,font=fnt)
        position = (position[0]-w/2,position[1])
        # manual fix for centering
        d.text(position, text, font=fnt, fill=(r,g,b,255))

        # flatten background and text
        ico = Image.alpha_composite(base, txt)

        return (ico)


    ########################################
    # 
    # Key display functions
    #
    # display_icon, display_clear
    # 
    ########################################

    def display_icon(self,key,ico):
        """
        Push an icon to a key display on the device.

        Parameters
        ----------
        key : int, key number on device (1-15)
        OR key: tuple, key number in row,column notation (1-3,1-5)
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
        key = self.key_remap(key)

        # send pixel data to elg
        header = HEADER_PAGE1
        header[5] = key
        msg = header+pixels[range(0,NUM_PAGE1_PIXELS*3)].astype(int).tolist()
        self.device.write(msg)

        header = HEADER_PAGE2
        header[5] = key
        msg = header+pixels[range((NUM_PAGE1_PIXELS-3)*3-1,NUM_TOTAL_PIXELS*3)].astype(int).tolist()
        self.device.write(msg)

    def display_clear(self,key):
        """
        Clears the display for a key on the device.
    
        Parameters
        ----------
        key : int, key number on device (1-15)
        """
        self.display_icon(key,self.KEY_BLANK)


    ########################################
    # 
    # Key button functions
    #
    # button_getch
    # rest not implemented yet
    # 
    ########################################

    def button_getch(self):
        """
        Detect button presses for the keys on the device.
    
        Returns
        ----------
        key : int, key number on device (1-15)
        time  : tuple, unix time of key [0] monitoring start, [1] key press, and [2] key release
        """
        time_start = time.time()
        # wait for button press
        state = self.device.read(NUM_KEYS+1)
        key = np.where(np.array(state) == 1)
        key = self.key_remap(int(key[0][1]))
        time_press = time.time()
        # wait for release
        state = self.device.read(NUM_KEYS+1)
        if len(np.where(np.array(state) == 1)) > 1:
            # no keys currently pressed
            raise ValueError('Unexpected getch state.')
        time_release = time.time()
        
        return (key,(time_start,time_press,time_release))
        


