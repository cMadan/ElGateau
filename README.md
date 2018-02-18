# ElGateau
#### ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research

In experimental psychology research, we often ask participants to press specific keys to correspond to responses in the experiment. For instance, one key for 'old' and another for 'new' in an old/new recognition memory test, 'word' and 'nonword' in a lexical decision task, or red/green/blue in a Stroop test. Sometimes we put stickers over keys on a keyboard to remind participants of these key mappings, but often they are merely included as part of the experiment instructions. What if we could easily just write 'old' and 'new' on the keys themselves? This approach could additionally lead to more manageable (and automatically logged) counterbalancing across participants, but we could further counterbalance key mappings across trials (or blocks of trials) if desired. In some cases, a whole experiment could be implemented on an LCD keypad. This project is the infrastructure for implementing experiments with an LCD keypad called the Elgato Stream Deck.

The Elgato Stream Deck is effectively a USB interface device with an rray of 3x5 keys. Each key has an LCD display (72x72 px resolution) on the face of it, and has physical buttons that can be pressed and released. This project, 'ElGateau' is a Python API for using the Stream Deck device (updating displays, listen for button presses), along with supporting functionality (e.g., writing text to the display, 'preprocessing' images before writing to display, monitoring for specific button presses). On top of this base functionality, the ElGateau also includes higher-level functions to support using this device in experimental psychology research, such as logging display updates and key presses as well as storing internal representations of the current displays on the device. A 'developer mode' is also included to allow for experiment development without needing the Stream Deck device on hand.

![Elgato Stream Deck](https://cdn.vox-cdn.com/uploads/chorus_image/image/54298497/91fukDTbNVL._SL1500_.0.jpg)

### Current Functionality

Tested in Windows 10 and Mac OS X 10.11.

- Basic device interaction
	* Open a USB I/O connection to the Stream Deck device (`ElGateau()`)
	* Reset the LCD displays (`ElGateau.reset`) and set their brightness (`ElGateau.set_brightness`)

- Update the displays of the LCD keys (`ElGateau.display_update`)
	* This function additionally updates an internal representation of the displays (`ElGateau.display_status`)
	* Wraps around 'low-level' interaction with the device (`ElGateau.display_icon`)
	* Easy clearing of a specified key display (or multiple) (`ElGateau.display_clear`)
	* When in developer mode (`dev_mode`), display info is instead passed to an display updating function (`ElGateau.dev_display_icon`), which updates an image representing the Stream Deck, rather than the actual device
		+ This 'virtual display' can be accessed at any time as `ElGateau.display_state`
			- This virtual display is only maintained if in developer mode, as it otherwise is unneeded and would slow interactions with the Stream Deck device

- Listen for key button presses (`ElGateau.button_listen_key`)
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
	* Developer mode for demonstrating experiments without the device needed (`ElGateau(dev_mode=True)`)
		+ Developed using QT5 to build the interface as an interactive figure in Jupyter notebook (`%matplotlib qt5`)

- Demo experiments
	* Color name-hue matching task (`demo_colours`)
		+ Simple experiment using just mainly solid colors
		+ Has a 'flickering' animation for each trial
	* 'Devil' risk-taking task (`demo_deviltask`)
		+ Only uses characters from an emoji/unicode font (no pictures)
	

### Coming Soon

- More demo experiments

- Logging (in-line with experimental psychology needs)
	* Not automatically, just a convenience class, like `Icon`

For current (unpolished) notes on the status of the project, see [Notes.md](Notes.md)


### Dependencies
pip install ...
- hidapi [https://github.com/trezor/cython-hidapi/blob/master/hid.pyx]
	+ Needs to be hidapi *not* hid!
- Pillow [http://pillow.readthedocs.io/en/latest/index.html]
	+ This is a Python 3 compatible fork of PIL


### Disclaimer

This project is not associated with Elgato Systems GmbH. 
Emoji artwork is provided by EmojiOne (v2.3) and is licensed under CC-BY 4.0.
(pixel fonts?)


### Acknowledgements

Comments and feedback from Olivia Guest, Michael Hoffman, and Justin Kiggins (via Twitter) greatly helped with the development of this project.

:cake:
