# ElGateau
ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research

Tested in Windows 10.
(Later will test in Mac OS X 10.11.)

The Elgato Stream Deck is effectively a USB interface device with an rray of 3x5 keys. Each key has an LCD display (72x72 px resolution) on the face of it, and has physical buttons that can be pressed and released. This project is a Python API for this device (updating displays, listen for button presses), along with supporting functionality (e.g., writing text to the display, 'preprocessing' images before writing to display, monitoring for specific button presses). On top of this base functionality, the 'framework' also includes higher-level functions to support using this device in experimental psychology research, such as logging display updates and key presses as well as storing internal representations of the current displays on the device.

![Elgato Stream Deck](https://cdn.vox-cdn.com/uploads/chorus_image/image/54298497/91fukDTbNVL._SL1500_.0.jpg)


## Current Functionality

- Basic device interaction
	* Open a USB I/O connection to the Stream Deck device (`ElGateau()`)
	* Reset the LCD displays (`ElGateau.reset`) and set their brightness (`ElGateau.set_brightness`)

- Update the displays of the LCD keys (`ElGateau.display_update`)
	* This function additionally updates an internal representation of the displays (`ElGateau.display_status`)
	* Wraps around 'low-level' interaction with the device (`ElGateau.display_icon`)
	* Easy clearing of a specified key display (or multiple) (`ElGateau.display_clear`)

- Listen for key button presses (`ElGateau.button_listen`) [NOT IMPLEMENTED YET]
	* This function wraps around 'low-level' interaction with the device (`ElGateau.button_getch`)
	* Also 'high-level' button listening for either specifed key(s) to be pressed (`ElGateau.button_listen_key`) or a number of key presses (`ElGateau.button_listen_count`)

- Additional convenience functions:
	* An `Icon` class that helps with preparation of the icons to be displayed on the keys
		+ Create icons that are solid colors (`Icon.solid`)
		+ Read in images, pad them, and resize them (`Icon.prep`)
		+ Write text to an icon, including overlay on image and multi-line text, as well as specified font name/size/position (`Icon.text`)
		+ Includes some generic `label` information (image/solid/text) that gets passed on to `ElGateau.display_status` as well as specific `contents` information such as icon filenames, hex color code for solid colors, or text strings
	* Remap the key numbering to be more intuitive (`ElGateau.key_remap`), can use either a 1-15 numbering, or a (row,column) notation (not fully implemented on display and button listen functions yet)
	* Conversion of hex color strings (e.g., `E5E5E5`) to RGB tuples (`hex2rgb`)


## Coming Soon

- Basic demo experiments

- Developer mode, that doesn't require the device to be connected, with I/O through Jupyter notebook

- Logging (in-line with experimental psychology needs)

For current (unpolished) notes on the status of the project, see [Notes.md](Notes.md)


## Dependencies
pip install ...
- hidapi [https://github.com/trezor/cython-hidapi/blob/master/hid.pyx]
- Pillow [http://pillow.readthedocs.io/en/latest/index.html]


### Disclaimer

This project is not associated with Elgato Systems GmbH. 
Emoji artwork is provided by EmojiOne (v2.3) and is licensed under CC-BY 4.0.
(pixel font?)


### Acknowledgements

Comments and feedback from Olivia Guest, Michael Hoffman, and Justin Kiggins (via Twitter) greatly helped with the development of this project.

:cake: