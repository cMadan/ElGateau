# init
from ElGateau import *
ElGateau = ElGateau()
ElGateau.display_clear('all')

# import dependencies
import random
from matplotlib import colors as mcolors
col = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# define constants
ntrials = 10
list_colors = {'red': 'firebrick', 'blue': 'slateblue', 'green': 'limegreen'}
list_keys = [7, 8, 9]

# prep variables
colors = list(list_colors.keys())
trial = 0
ico = {}
for color in colors:
    ico[color] = ElGateau.icon_solid(col[list_colors[color]])
flicker = 20

# run experiment!
while trial < ntrials:
    # populate keys
    positions = list(range(0, len(list_keys)))

    # shuffle a bunch to make it more interesting
    flick = 0
    while flick < flicker:
        random.shuffle(colors)
        for pos in positions:
            ElGateau.display_icon(list_keys[pos], ico[colors[pos]])
        flick += 1

    # choose a color
    random.shuffle(positions)
    print(colors[positions[0]])

    # wait for that key press
    ElGateau.button_listen_key(list_keys[positions[0]])

    trial += 1

# end
ElGateau.display_clear('all')
ElGateau.display_icon(8, ElGateau.icon_text('Great\nJob', size=20))
ElGateau.display_icon(13, ElGateau.icon_prep('cake', 300))
