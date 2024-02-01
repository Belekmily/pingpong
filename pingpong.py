from pygame import *
from random import randint

score_L = 0
score_P = 0

predkosc_pilki_x = -8
predkosc_pilki_y = 8

img_paletka = "paletka.png"
img_pilka = "pilka.png"

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill((51, 102, 255))


class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #Call for the class (Sprite) constructor:
      sprite.Sprite.__init__(self)
 
 
       #every sprite must store the image property
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
 
 
       #every sprite must have the rect property – the rectangle it is fitted in
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   #method to control the sprite with arrow keys
   def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
         self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80:
         self.rect.x += self.speed



class PlayerP(GameSprite):
   #method to control the sprite with arrow keys
   def update(self):
      keys = key.get_pressed()
      if keys[K_UP] and self.rect.y > 0:
          self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < 400:
          self.rect.y += self.speed

#klasa gracza
class PlayerL(GameSprite):
  #method to control the sprite with arrow keys
   def update(self):
      keys = key.get_pressed()
      if keys[K_w] and self.rect.y > 0:
          self.rect.y -= self.speed
      if keys[K_s] and self.rect.y < 400:
          self.rect.y += self.speed