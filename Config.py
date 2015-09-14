# Config.py
# Configuration file for CSC447, Project 2 "Evil Tetris"
# In use for modularity purposes. Simple changes to the program layout can be made here without risk.
# See: https://inventwithpython.com/pygame/chapter7.html
# Jack Riales, Jim Fletcher, and Andrew Slaughter

# Window and display configuration constants
WINDOWWIDTH    = 640   # Arbitrary
WINDOWHEIGHT   = 480   # Arbitrary
FPS             = 25

# Tetris Sizing Configurations
BOXSIZE         = 20
BOARDWIDTH      = 30
BOARDHEIGHT     = 20
BLANK           = '.'

# Tetris Motion Configurations
MOVESIDEWAYSFREQ= 0.15
MOVEDOWNFREQ    = 0.1

# Tetris Misc
XMARGIN         = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN       = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

# Color Palette
WHITE           = (255, 255, 255)
GRAY            = (185, 185, 185)
BLACK           = ( 0, 0, 0)
RED             = (155, 0, 0)
LIGHTRED        = (175, 20, 20)
GREEN           = ( 0, 155, 0)
LIGHTGREEN      = ( 20, 175, 20)
BLUE            = ( 0, 0, 155)
LIGHTBLUE       = ( 20, 20, 175)
YELLOW          = (155, 155, 0)
LIGHTYELLOW     = (175, 175, 20)

# Color Configuration
BORDERCOLOR     = BLUE
BGCOLOR         = BLACK
TEXTCOLOR       = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS          = (BLUE, GREEN, RED, YELLOW)
LIGHTCOLORS     = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)

# Each color must have a corresponding light color
assert len(COLORS) == len(LIGHTCOLORS)

# EOF Config.py : Located @ /Config.py
