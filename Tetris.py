# Tetris.py
# Main file for CSC447, Project 2 "Evil Tetris"
# Program written by Jack Riales, Jim Fletcher, and Andrew Slaughter

# Import necessary libraries
import os, random, sys
import pygame
from pygame.locals import *

# [Check] Pygame Import
if not pygame.font: print 'Warning, fonts disabled.'
if not pygame.mixer: print 'Warning, sound disabled.'

# [Import] Game configuration file
import Config

# [Test] File imports
# print Config.WINDOW_WIDTH

# EOF Tetris.py : Located @ /Tetris.py
