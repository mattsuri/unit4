#Matthew Suriawinata
#3/22/18
#monkey-banana.py - BEst game ever

from ggame import *

from random import randint




ROWS = 20
COLS = 40
CELL_SIZE = 20

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    

def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
    
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
    
    
def moveBanana():
    data["frames"] = 0 
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    
def updateScore():
    data["score"] += 10
    data["scoreText"].destroy() #remove old writing
    scoreBox = TextAsset("Score = " + str(data["score"]))
    data["scoreText"] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
def step():
    data["frames"] += 1
    if data["frames"] == 300:
        moveBanana()
    


if __name__ == "__main__":
    
    #hold baribales in a dicitionary
    data = {} 
    data["score"] = 0
    data["frames"] = 0
    
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00, 1)
    
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1, yellow), yellow)
    scoreBox = TextAsset("Score = 0")
    
    
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox, (CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data["scoreText"] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    
    App().listenKeyEvent("keydown","right arrow", moveRight)
    App().listenKeyEvent("keydown","left arrow", moveLeft)
    App().listenKeyEvent("keydown","up arrow", moveUp)
    App().listenKeyEvent("keydown","down arrow", moveDown)
    
    
    App().run(step)
