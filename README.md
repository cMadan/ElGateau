# ElGateau
ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research

## To do list

1. Build a basic API
	- Detect button presses
		+ Listen for *next* press
		+ Listen until specific key pressed
		+ Listen until x key presses have been made
		+ Record key press sequences and RT

	- ~~Reset screen~~
	- ~~Update icons~~
		+ ~~Separate icon 'preprocessing' (load/padding/resizing) from 'push to display'~~
		+ ~~Function to re-map key number to something more sensible~~
		+ ~~Write text to an icon~~
				* If ico=None, make it work with black background
				* Have text location as 
				* Really no fix for centering text...??
					+ https://github.com/python-pillow/Pillow/issues/2067
			- https://github.com/source-foundry/Hack
			- https://github.com/jslegers/emoji-icon-font
			- https://github.com/koemaeda/gohufont-ttf
			- https://github.com/ranesr/SwiftIcons
			- https://github.com/chrissimpkins/codeface
			- https://github.com/Tecate/bitmap-fonts
			- https://github.com/romeovs/creep
			- https://github.com/MicahElliott/Orp-Font
	- Secondary functions
		+ ~~Modify brightness~~
	- ~~Package code into a Python module~~
			- Rename 'inputs' to parameters

	- Build some basic data logging functions
		+ Open log file, parse subject ID with sys.argv
		+ Log all responses to a given trial (and RT), based on key listener primitive
		+ Ability to push custom logs (e.g., for memory task, log initial positions, location of each icon name)
			* timestamp, trial number, log record type ([K]ey,[C]ustom)
			* log startof button listeners and their end conditions?
		+ Close log file
			* Will require a log file handle to be stored

	- Make a boot function (open, reset, draw {cake, 'ElGateau','cMadan',version}, some screen test, clear displays)

1. Make simple proof-of-principle 'experiments'

	- Demo script
		+ Fill each key with an icon, spiral pattern
		+ Write key number on each, pixel text
		+ Key monitor waits for any key press
			* Check that key is released

	- Visual search
		+ Record False alarms and RT (per trial)
		+ Presents 15 different icons, find the target one, press

	- Match color
		+ Prints color "red", "green", "blue" to command window, have to press designated button
		+ Shuffle R/G/B buttons across trials

	- Devil task (look at paper again)

	- Memory game
		+ Card flips, 7 pairs, etc.

	- Go/nogo?

	- Config, get subject number with sys.argv

1. Make a windowed 'developer-mode' that doesn't require hardware??
http://pygame.org/project/3267/5313

1. Write up basic docs
	- badges from shields.io
		+ Python 3

1. Write as short paper for JOSS?

## Existing APIs
https://github.com/Lange/node-elgato-stream-deck
https://github.com/danieltian/stream-deck-api

https://github.com/OpenStreamDeck/StreamDeckSharp

https://github.com/Number10Ox/stream-deck-driver
https://github.com/GalacticGlum/StreamDeck
https://github.com/WElRD/StreamDeckCore
https://github.com/sammessina/csharp-elgato-stream-deck
https://github.com/tchiak/NET-elgato-stream-deck

## Dependencies
pip install ...
- hidapi
- Pillow

### Disclaimer

This project is not associated with Elgato Systems GmbH. 
Emoji artwork is provided by EmojiOne (v2.3) and is licensed under CC-BY 4.0.
(pixel font?)

:cake: