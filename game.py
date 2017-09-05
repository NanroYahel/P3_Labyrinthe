#! usr/bin python3
# coding:utf-8

import pygame
from pygame.locals import *
import pandas as pd

pygame.init()

window=pygame.display.set_mode((600,600),RESIZABLE)

backgroud=pygame.Surface([600,600])

window.blit(backgroud,(0,0))

class Wall(pygame.sprite.Sprite):

	def __init__(self,image):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load(image).convert_alpha()

		self.rect=self.image.get_rect()


#Création d'un groupe de sprite pour la suite
wall_list=pygame.sprite.Group()

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
		if labyrinthe_map.iloc[row,columns]=='1':
			wall=Wall('pictures/wall-40x40.png')
			wall.rect.x=x_pos
			wall.rect.y=y_pos
			wall_list.add(wall)
		x_pos=x_pos+40
	y_pos=y_pos+40

######




wall_list.draw(window)

pygame.display.flip()


continuer=1

while continuer:
	for event in pygame.event.get():
		if event.type==QUIT:
			continuer=0
