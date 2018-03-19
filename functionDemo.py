#Matthew Suriawinata
#3/9/18
#functionDemo.py - how to write our own functions

def hw():
    print("Hello, world")
    
    

def double(thingToDouble):
    print(thingToDouble * 2)
    
double(True)

double(12)

def slope(x1, y1, x2, y2):
    print((y2-y1)/ (x2-x1))

def bigger(a,b):
    if a > b:
        print(a)
    else:
        print(b)
        
#bigger(3,4)
slope(1,1,2,2)

print("The max of 3 and 4 is", max(3,4))
print("The max of 3 and 4 is", bigger(3,4))
