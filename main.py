from pygame_functions import *
import math, random, time, pickle

screenSize(1920,1080)
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

    def move(self, player):
        self.xspeed = self.speed * math.cos(self.angle/180*math.pi)
        self.yspeed = self.speed * math.sin(self.angle/180*math.pi)

        self.x = (self.x + self.xspeed) % 10000
        self.y = (self.y + self.yspeed) % 10000

        
        moveSprite(self.sprite, (self.x - player.x)+960, (self.y - player.y)+540, centre=True)

class Player(Creature):
    def __init__(self,x,y,image,size):
        super().__init__(x,y,image,size)
        moveSprite(self.sprite,960,540,centre=True)

    def move(self, creatures):
        #work out the angle from the player to the mouse
        dx = mouseX() - 960
        dy = mouseY() - 540
        dist = math.sqrt(dx**2 + dy**2)
        self.speed = dist /200 *10

        self.angle = math.degrees(math.atan2(dy, dx))
        transformSprite(self.sprite,self.angle, self.size/100)

        self.xspeed = self.speed * math.cos(self.angle/180*math.pi)
        self.yspeed = self.speed * math.sin(self.angle/180*math.pi)

        self.x = (self.x + self.xspeed) % 10000
        self.y = (self.y + self.yspeed) % 10000
        for c in creatures:
            if touching(self.sprite,c.sprite):
                if self.size > c.size:
                    #print("Nom")
                    creatures.remove(c)    
                    hideSprite(c.sprite)
                    self.size += 5
                elif c.size >= self.size:
                    return 0
                

                
def drawBoundary(player):
    clearShapes()
    drawRect(900-player.x, 500-player.y, 10000,10000, (0,0,40),0)
    drawRect(900-player.x, 500-player.y, 10000,10000, (255,255,255),5)



setAutoUpdate(False)
creatures = []
for i in range(200):
    c1 = Creature(random.randint(0,10000),random.randint(0,10000), "enemy.png", random.randint(10,100)) 
    creatures.append(c1)

p = Player(5000,5000,"player.png",20)

while True:
    drawBoundary(p)
    for creature in creatures:
        creature.move(p)
    if p.move(creatures) != 0:
        p.move(creatures)
    else:
        break
    updateDisplay()
    tick(50)



game_over = makeSprite("gameover.png")
showSprite(game_over)
moveSprite(game_over,960,540,centre=True)
updateDisplay()
endWait()
