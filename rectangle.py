#Matthew Suriawinata
#3/9/18
#rectangle.py - area and perimeter of rectangle

def rectangle(a,b):
    print("The area is", a*b)
    print("The perimeter is", 2*a + 2*b)
    
rectangle(3,4)



def printStars(num):
    print("*" * num)
    
printStars(6)

def countdown(num):
    for i in range(0,num):
        print(num - i)
    print("BOOM!")
    
countdown(5)


def vprint(word):
    for ch in word:
        print(ch)
        
vprint("Smeds")

