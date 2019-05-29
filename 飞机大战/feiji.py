#coding=utf-8
import random
import time
import pygame
from pygame.locals import *

class Base(object):
	def __init__(self,screen,name):
		self.name = name
		self.screen = screen


class Plane(Base):
	def __init__(self,screen,name):
		super().__init__(screen,name)
		self.image = pygame.image.load(self.imageName).convert()
		self.bulletList = []

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

		needDelItemList = []
		
		for i in self.bulletList:
			if i.judge():
				needDelItemList.append(i)

		for i in needDelItemList:
			self.bulletList.remove(i)

		for bullet in self.bulletList:
			bullet.display()
			bullet.move()

	def sheBullet(self):
		newBullet = PublicBullet(self.x,self.y,self.screen,self.name)
		self.bulletList.append(newBullet)


class HeroPlane(Plane):
	def __init__(self,screen,name):
		self.x = 230
		self.y = 600



		self.imageName = "./feiji/hero.gif"
		super().__init__(screen,name)


	def moveLeft(self):
		self.x -=10

	def moveRight(self):
		self.x+=10


class EnemyPlane(Plane):
	def __init__(self,screen,name):
		self.x = 0
		self.y = 0



		self.imageName = "./feiji/enemy-1.gif"
		super().__init__(screen,name)

		self.direction = 'right'

	

	def move(self):
		if self.direction == "right":
			self.x += 2
		elif self.direction == "left":
			self.x -= 2


		if self.x >480 -50:
			self.direction = "left"
		elif self.x <0:
			self.direction = "right"

	def sheBullet(self):
		num = random.randint(1,100)
		if num == 88:
			super().sheBullet()
	

class PublicBullet(Base):
	def __init__(self,x,y,screen,planeName):
		super().__init__(screen,planeName)

		if self.name == "hero":
			self.x = x+40
			self.y = y-20
			imageName = "./feiji/bullet-3.gif"

		elif self.name == "enemy":
			self.x = x+30
			self.y = y+30
			imageName = "./feiji/bullet-1.gif"
		self.image = pygame.image.load(imageName).convert()

	def move(self):
		if self.name == "hero":
			self.y -= 2
		elif self.name == "enemy":
			self.y += 2

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))	
	def judge(self):
		if self.y < 0 or self.y >890:
			return True
		else:
			return False	


if __name__ == "__main__":
	screen = pygame.display.set_mode((480,690),0,32)
	background = pygame.image.load("./feiji/background.png").convert()

	heroPlane = HeroPlane(screen,"hero")
	
	enemyPlane = EnemyPlane(screen,"enemy")


	while True:
		screen.blit(background,(0,0))

		heroPlane.display()

		enemyPlane.move()
		enemyPlane.sheBullet()
		enemyPlane.display()


		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit")
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print("left")
					heroPlane.moveLeft()
				elif event.key == K_d or event.key == K_RIGHT:
					print("right")
					heroPlane.moveRight()
				elif event.key == K_SPACE:
					print("apace")
					heroPlane.sheBullet()
		time.sleep(0.01)
		pygame.display.update()										

