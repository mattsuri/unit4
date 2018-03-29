#Matthew Suriawinata
#3/29/18
#warmup12.py - GCF of two numbers


def GCF(num1,num2):
    if num1 < num2:
        num1 = smaller
        num2 = greater
    else:
        num2 = smaller
        num1 = greater
    for i in range (0,smaller):
        if greater%(smaller-i) == 0:
            return(smaller - i)
            break
