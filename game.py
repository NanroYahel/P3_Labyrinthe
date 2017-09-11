#! usr/bin/env python3
# coding:utf-8

import pygame
from pygame.locals import *
import pandas as pd
import random as rd

import class_game as cl

pygame.init()

window=pygame.display.set_mode((680,680),RESIZABLE)

backgroud=pygame.Surface([680,680])

gameover=pygame.image.load('pictures/gameover.png').convert()

youwin=pygame.image.load('pictures/win.png').convert()

window.blit(backgroud,(0,0))
	

#Create sprite groups using for drawing sprites and collision management
edge_list=pygame.sprite.Group()
wall_list=pygame.sprite.Group()
stuff_list=pygame.sprite.Group()
all_sprite=pygame.sprite.Group()


######
#Generation of Labyrinth

#Function to open the file with the labyrinth map
def data_from_csv(csv_file):
	data=pd.read_csv(csv_file, sep=",", header=None, dtype=str)
	return data

labyrinthe_map=data_from_csv('level2.csv')

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

		#Create guardian
		if labyrinthe_map.iloc[row,columns]=='finish':
			guardian=cl.Guardian()
			guardian.rect.x=x_pos
			guardian.rect.y=y_pos
			#Add to the all_sprite group for drawing
			all_sprite.add(guardian)


		x_pos=x_pos+40

	y_pos=y_pos+40

######

######
#Generation of object

while cl.Stuff.COUNT != 0:
	#fonction de creation
	stuff=cl.Stuff()


	while pygame.sprite.spritecollide(stuff, wall_list,False)\
	 or pygame.sprite.spritecollide(stuff,stuff_list,False):
		# while pygame.sprite.spritecollide(stuff,stuff_list,False):
		rect_x=rd.randrange(40,600,40)
		rect_y=rd.randrange(40,600,40)
		stuff.position(rect_x,rect_y,player,wall_list)

	#Add to the groups for drawing and collision management
	stuff_list.add(stuff)	
	all_sprite.add(stuff)

	cl.Stuff.COUNT -=1

######




pygame.key.set_repeat(400, 30)

continuer=1

def update_screen():

	if win_condition!='no' and win_condition!='yes':
		window.blit(backgroud,(0,0))
		all_sprite.draw(window)	

	if win_condition=='no':
		window.blit(gameover,(0,0))
	if win_condition=='yes':
		window.blit(youwin,(0,0))
	# else:
	# 	window.blit(backgroud,(0,0))
	# 	all_sprite.draw(window)	

	pygame.display.flip()

win_condition=''

while continuer:
	for event in pygame.event.get():
		if event.type==QUIT:
			continuer=0
		if event.type==KEYDOWN:
			direction=event.key
			player.move(direction,wall_list)
			if pygame.sprite.spritecollide(player,stuff_list,True):
				player.score+=1
				print(player.score)
			if pygame.sprite.collide_rect(player,guardian):
				if player.score==7:
					win_condition='yes'
				else:
					win_condition='no'

	update_screen()

