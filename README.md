# ElGateau
ElGateau: A Framework for Using the Elgato Stream Deck for Experimental Psychology Research

## To do list

1. Build a basic API
	- Detect button presses
		+ Listen for *next* press
		+ Listen until specific key pressed
		+ Listen until x key presses have been made
		+ Record key press sequences and RT

	- Reset screen -- DONE
	- Update icons -- DONE
		+ Separate icon 'preprocessing' (load/padding/resizing) from 'push to display' -- DONE
		+ Function to re-map key number to something more sensible -- DONE
		+ Write text to an icon -- DONE
			- https://github.com/chrissimpkins/codeface
			- https://github.com/romeovs/creep
			- https://github.com/MicahElliott/Orp-Font
	- Secondary functions
		+ Modify brightness -- DONE
	- Package code into a Python module -- DONE

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

