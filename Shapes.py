# Shapes.py
# Shapes Template file for CSC447, Project 2 "Evil Tetris"
# See: https://inventwithpython.com/pygame/chapter7.html
# Jack Riales, Jim Fletcher, and Andrew Slaughter

# Block Template Matrix Width
TEMPLATEWIDTH = 5

# Block Template Matrix Height
TEMPLATEHEIGHT= 5

# Block Templates
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     'OOOOO'],
                    ['..O..',
                     '..O..',
                     '..OOO',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOOO',
                     '..O..',
                     '..O..'],
                    ['..O..',
                     '..O..',
                     'OOO..',
                     '..O..',
                     '..O..']]

# Too hard.
#CF_SHAPE_TEMPLATE = [['O.O.O',
#					  '.O.O.',
#					  'O.O.O',
#					  '.O.O.',
#					  'O.O.O'],
#					 ['O.O.O',
#					  '.O.O.',
#					  'O.O.O',
#					  '.O.O.',
#					  'O.O.O'],
#					  ['O.O.O',
#					  '.O.O.',
#					  'O.O.O',
#					  '.O.O.',
#					  'O.O.O'],
#					  ['O.O.O',
#					  '.O.O.',
#					  'O.O.O',
#					  '.O.O.',
#					  'O.O.O']]

ROTATOR_SHAPE_TEMPLATE = [['..O..',
						   '..O..',
						   '..OO.',
						   '..O..',
						   '..O..'],
						  ['.....',
						   '..O..',
						   'OOOOO',
						   '.....',
						   '.....'],
						   ['..O..',
						   '..O..',
						   '.OO..',
						   '..O..',
						   '..O..'],
						   ['.....',
						   '.....',
						   'OOOOO',
						   '..O..',
						   '.....']]
PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
#		  'CF': CF_SHAPE_TEMPLATE,
		  'ROTATOR': ROTATOR_SHAPE_TEMPLATE}

# EOF Shapes.py : Located @ /Shapes.py
