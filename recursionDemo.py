#Matthew Suriawinata
#3/29/18
#recursionDemo.py - recursive version of countdown

def countdown(n):
    if n == 0:
        print("BOOM!")
    else:
        print(n)
        countdown(n-1)
    
countdown(5)
coundown(15)
