# Faça um programa em Python que abra e reproduza um arquivo de música.

import pygame

pygame.init()
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play()
input()
pygame.event.wait()
