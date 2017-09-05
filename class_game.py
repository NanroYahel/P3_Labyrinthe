#! usr/bin python3
# coding:utf-8

import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):

	def __init__(self,image):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load(image).convert_alpha()

		self.rect=self.image.get_rect()

class Player(pygame.sprite.Sprite):

	def __init__(self,image):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load(image).convert_alpha()

		self.rect=self.image.get_rect()

	def move(self, direction):

		if direction==K_DOWN:
			self.rect=self.rect.move(0,40)
		if direction==K_UP:
			self.rect=self.rect.move(0,-40)
		if direction==K_LEFT:
			self.rect=self.rect.move(-40,0)
		if direction==K_RIGHT:
			self.rect=self.rect.move(40,0)

		