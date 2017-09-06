#! usr/bin/env python3
# coding:utf-8

import pygame
from pygame.locals import *
import pandas as pd

#Importe le module comportant les classes
import class_game as cl

pygame.init()

window=pygame.display.set_mode((600,600),RESIZABLE)

backgroud=pygame.Surface([600,600])

window.blit(backgroud,(0,0))


#Création d'un groupe de sprite pour la suite
wall_list=pygame.sprite.Group()
all_sprite=pygame.sprite.Group()

######
#Génération du Labyrinthe

#Fonction permettant d'ouvrir le fichier contenant la map du labyrinthe
def data_from_csv(csv_file):
	data=pd.read_csv(csv_file, sep=",", header=None, dtype=str)
	return data

labyrinthe_map=data_from_csv('level.csv')

x_pos=0
y_pos=0

for row, series in labyrinthe_map.iterrows():
	x_pos=0
	for columns, series in labyrinthe_map.iteritems():

		#Création des murs
		if labyrinthe_map.iloc[row,columns]=='1':
			wall=cl.Wall()
			wall.rect.x=x_pos
			wall.rect.y=y_pos
			#Ajout dans les groupes de sprite pour affichage et gestion des collisions
			wall_list.add(wall)
			all_sprite.add(wall)

		#Création personnage
		if labyrinthe_map.iloc[row,columns]=='start':
			player=cl.Player()
			player.rect.x=x_pos
			player.rect.y=y_pos
			#Ajout dans le groupe all_sprite pour affichage
			all_sprite.add(player)

		x_pos=x_pos+40

	y_pos=y_pos+40

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
