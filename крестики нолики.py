# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:09:15 2021

@author: Паша
"""

import pygame
import sys

pygame.init()



size = (510, 510)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GAME")



while True:
    for evet in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame,quit()
            sys.exit(0)


 #if event.type == pygame.QUIT: