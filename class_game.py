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

		#Count number of stuff for the victory condition
		self.score=0

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


class Stuff(pygame.sprite.Sprite):

	#Use to generate 7 object on the map
	COUNT=7

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load('pictures/object.png').convert_alpha()

		self.rect=self.image.get_rect()

	def position(self,rect_x,rect_y,player,wall_list):
		test_stuff=Stuff()
		test_stuff.rect.x=rect_x
		test_stuff.rect.y=rect_y

		if not pygame.sprite.spritecollide(test_stuff,wall_list,False) and not pygame.sprite.collide_rect(test_stuff,player):
			self.rect.x=rect_x
			self.rect.y=rect_y
			print("Test2")
		print('Test3')
