#Matthew Suriawinata
#3/22/18
#monkey-banana.py - BEst game ever

from ggmae import *
if __name__ == "__main__":
    
    #colors
    green = Color(0x006600,1)
    
    jungleBos = RectangleAsset(800,500,LineStyle(1,green),green)
    
    Sprite(jungleBos)
    
    App().run()
