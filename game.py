#! usr/bin/env python3
# coding:utf-8

import pygame
from pygame.locals import *
import pandas as pd
import random as rd

import class_game as cl

pygame.init()

window=pygame.display.set_mode((600,600),RESIZABLE)

backgroud=pygame.Surface([600,600])

window.blit(backgroud,(0,0))
	

#Create sprite groups using for drawing sprites and collision management
wall_list=pygame.sprite.Group()
stuff_list=pygame.sprite.Group()
all_sprite=pygame.sprite.Group()

######
#Generation of Labyrinth

#Function to open the file with the labyrinth map
def data_from_csv(csv_file):
	data=pd.read_csv(csv_file, sep=",", header=None, dtype=str)
	return data

labyrinthe_map=data_from_csv('level.csv')

x_pos=0
y_pos=0

for row, series in labyrinthe_map.iterrows():
	x_pos=0
	for columns, series in labyrinthe_map.iteritems():

		#Create walls
		if labyrinthe_map.iloc[row,columns]=='1':
			wall=cl.Wall()
			wall.rect.x=x_pos
			wall.rect.y=y_pos
			#Add in groups for drawing and collision management
			wall_list.add(wall)
			all_sprite.add(wall)

		#Create player character
		if labyrinthe_map.iloc[row,columns]=='start':
			player=cl.Player()
			player.rect.x=x_pos
			player.rect.y=y_pos
			#Add to the all_sprite group for drawing
			all_sprite.add(player)

		x_pos=x_pos+40

	y_pos=y_pos+40

######

######
#Generation of object

# while cl.Stuff.COUNT != 0:
# 	#fonction de creation
# 	stuff=cl.Stuff()
# 	rect_x=rd.randrange(0,600,40)
# 	rect_y=rd.randrange(0,600,40)
# 	while pygame.sprite.spritecollide(stuff,stuff_list,False):
# 		stuff.position(rect_x,rect_y,player,wall_list)
# 		print(stuff.rect)
# 	#Add to the groups for drawing and collision management
# 	stuff_list.add(stuff)	
# 	all_sprite.add(stuff)

# 	print (stuff.rect)

# 	cl.Stuff.COUNT -=1

######


pygame.key.set_repeat(400, 30)

continuer=1

def update_screen():
	window.blit(backgroud,(0,0))
	all_sprite.draw(window)		
	pygame.display.flip()


while continuer:
	for event in pygame.event.get():
		if event.type==QUIT:
			continuer=0
		if event.type==KEYDOWN:
			direction=event.key
			player.move(direction,wall_list)

		update_screen()
