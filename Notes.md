## To do list

1. Build a basic API

	- Standard word use: Keys consist of Button and Display. Icons and Text can be written to Displays.
		- Update naming for icon vs display

	- Look into fonts more
		- https://github.com/source-foundry/Hack
		- https://github.com/jslegers/emoji-icon-font
		- https://github.com/koemaeda/gohufont-ttf
		- https://github.com/ranesr/SwiftIcons
		- https://github.com/chrissimpkins/codeface
		- https://github.com/Tecate/bitmap-fonts
		- https://github.com/romeovs/creep
		- https://github.com/MicahElliott/Orp-Font

	- Build some basic data logging functions
		+ Maybe this should be a nested class?
		+ Open log file, parse subject ID with sys.argv
			- only if None input, else use provided subject ID
		+ Log all responses to a given trial (and RT), based on key listener primitive
		+ Ability to push custom logs (e.g., for memory task, log initial positions, location of each icon name)
			* timestamp, trial number, log record type ([D]isplay,[B]utton,[C]ustom)
			* log startof button listeners and their end conditions?
		+ Close log file
			* Will require a log file handle to be stored

	- Make a boot function (open, reset, draw {cake, 'ElGateau','cMadan',version}, some screen test, clear displays)

1. Work on 'developer mode'
	- Display works, now work on button presses
		+ Best option is an interactive figure in Jupyter with mpl?
			+ Can I do imports based on if-statement and still be good with PEP8 ?


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
		+ ~~Prints color "red", "green", "blue" to command window, have to press designated button~~
		+ ~~Shuffle R/G/B buttons across trials~~
		+ Make colors flicker to make it a bit more engaging
		+ Change how shuffling works, show color label before flickering happens
			* Set 'flickering' to occur a random amount within a range
		+ Add extra colors? (pink, purple, orange, yellow, brown) -- not sure...
			* Use Brewer colors?

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

	- Config, get subject number with sys.argv, else can be passed in init call?

1. Write up basic docs
	- badges from shields.io
		+ Python 3

1. Write as short paper for JOSS? If not, maybe F1000Research?

## Existing APIs
- https://github.com/Lange/node-elgato-stream-deck
- https://github.com/danieltian/stream-deck-api

- https://github.com/OpenStreamDeck/StreamDeckSharp

- https://github.com/Number10Ox/stream-deck-driver
- https://github.com/GalacticGlum/StreamDeck
- https://github.com/WElRD/StreamDeckCore
- https://github.com/sammessina/csharp-elgato-stream-deck
- https://github.com/tchiak/NET-elgato-stream-deck