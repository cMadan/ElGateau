# ElGateau
ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research

Tested in Windows 10.
(Later will test in Mac OS X 10.11.)

## To do list

1. Build a basic API
	- DONE
		- ~~Reset screen~~
		- ~~Update icons~~
			+ ~~Separate icon 'preprocessing' (load/padding/resizing) from 'push to display'~~
			+ ~~Function to re-map key number to something more sensible~~
				- ~~Allow for (row,column) notation too, also gets re-mapped~~
			+ ~~Write text to an icon~~
					* ~~If ico=None, make it work with black background~~
					* ~~Have text location as parameter~~ 
					* ~~Really no fix for centering text...??~~
						+ https://github.com/python-pillow/Pillow/issues/2067
			+ ~~'clear key' that is an alias for fill with solid color of black~~
				- ~~ICON_BLANK as a constant, use in the ico=None case too~~
		- Secondary functions
			+ ~~Modify brightness~~
		- ~~Package code into a Python module~~
			+ ~~Rename 'inputs' to parameters~~
			+ ~~Add some additional structure/comments to the module to make it more interpretable~~

	- IN PROGRESS
		- Standard word use: Keys consist of Button and Display. Icons and Text can be written to Displays.
			- Update naming for icon vs display

		- Fix Page 2 header code, should be longer, then can fix start number for pixels being sent
			+ Change page info, reset, etc, from hex to dec

		- Look into fonts more
			- https://github.com/source-foundry/Hack
			- https://github.com/jslegers/emoji-icon-font
			- https://github.com/koemaeda/gohufont-ttf
			- https://github.com/ranesr/SwiftIcons
			- https://github.com/chrissimpkins/codeface
			- https://github.com/Tecate/bitmap-fonts
			- https://github.com/romeovs/creep
			- https://github.com/MicahElliott/Orp-Font

		- Detect button presses
			+ ~~Listen for *next* press~~
				* Remove the start time in getch

			+ Listen until specific key pressed
			+ Listen until x key presses have been made
			+ Record key press sequences and RT

		- Build some basic data logging functions
			+ Open log file, parse subject ID with sys.argv
				- only if None input, else use provided subject ID
			+ Log all responses to a given trial (and RT), based on key listener primitive
			+ Ability to push custom logs (e.g., for memory task, log initial positions, location of each icon name)
				* timestamp, trial number, log record type ([D]isplay,[B]utton,[C]ustom)
				* log startof button listeners and their end conditions?
			+ Close log file
				* Will require a log file handle to be stored

		- Make a boot function (open, reset, draw {cake, 'ElGateau','cMadan',version}, some screen test, clear displays)


1. Reorganize useful links from above (other APIs, fonts) into a useful list

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
		+ Use emoji font
			* http://jslegers.github.io/emoji-icon-font/
			* definitely: 1f608 or 1f47f (devil) or 1f4a3 (bomb), 1f4b5 (money in box), 1f4b0 (money total) 
			* maybe: 229e (+ box), 1f3e6 (bank) 
			* bank icon, trial number, amount saved (from previous trials) -- top row
		+ https://stackoverflow.com/questions/11411746/drawing-multilingual-text-using-pil
		
		+ Brassen et al. (2012)
			* "On each trial, an array of eight boxes was presented, where seven boxes con- tained a gain (“gold”) and one contained a loss (“devil”)."
				- Will do 10 here
			* "Boxes could be opened from left to right. At any stage, volunteers could either open the next box or stop and collect the gains ac- quired so far in this round. Exposing the random- ly distributed devil ended the trial, and all gains from this round were lost."
			* "If volunteers decided to stop and collect their gains, the position of the devil was revealed, indicating how far they could have safely continued (“missed chance”)." 

	- Memory game
		+ Card flips, 7 pairs, etc.

	- Go/nogo?

	- Config, get subject number with sys.argv

1. Make a windowed 'developer-mode' that doesn't require hardware??
http://pygame.org/project/3267/5313

1. Write up basic docs
	- badges from shields.io
		+ Python 3

1. Write as short paper for JOSS? If not, maybe F1000Research?

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

### Acknowledgements

Comments and feedback from Olivia Guest, Michael Hoffman, and Justin Kiggins (via Twitter) greatly helped with the development of this project.

:cake: