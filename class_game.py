#! usr/bin python3
# coding:utf-8

import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load('pictures/wall-40x40.png').convert_alpha()

		self.rect=self.image.get_rect()

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load('pictures/macgyver.png').convert_alpha()

		self.rect=self.image.get_rect()

	def move(self, direction,wall_list):
		
		new_player=Player()
		new_player.rect=self.rect

		if direction==K_DOWN:
			new_player.rect=new_player.rect.move(0,40)
			if not pygame.sprite.spritecollide(new_player,wall_list,False):
				self.rect=new_player.rect
		if direction==K_UP:
			new_player.rect=new_player.rect.move(0,-40)
			if not pygame.sprite.spritecollide(new_player,wall_list,False):
				self.rect=new_player.rect
		if direction==K_LEFT:
			new_player.rect=new_player.rect.move(-40,0)
			if not pygame.sprite.spritecollide(new_player,wall_list,False):
				self.rect=new_player.rect
		if direction==K_RIGHT:
			new_player.rect=new_player.rect.move(40,0)
			if not pygame.sprite.spritecollide(new_player,wall_list,False):
				self.rect=new_player.rect



