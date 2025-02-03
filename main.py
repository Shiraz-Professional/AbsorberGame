from pygame_functions import *
import math, random, time, pickle

screenSize(1800,1000)
setBackgroundColour("black")


class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(1,15)
        self.angle = random.randint(1,360)
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)

    def move(self):
        self.xspeed = self.speed * math.cos(self.angle/180*math.pi)
        self.yspeed = self.speed * math.sin(self.angle/180*math.pi)

        self.x = (self.x + self.xspeed) % 1800
        self.y = (self.y + self.yspeed) % 1800
        moveSprite(self.sprite, self.x, self.y, centre=True)



setAutoUpdate(False)
creatures = []
for i in range(20):
    c1 = Creature(random.randint(0,1000),random.randint(0,1000), "enemy.png", random.randint(10,100)) 
    creatures.append(c1)

while True:
    for creature in creatures:
        creature.move()
    updateDisplay()
    tick(50)
   
endWait()
