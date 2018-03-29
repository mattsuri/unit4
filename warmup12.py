#Matthew Suriawinata
#3/29/18
#warmup12.py - GCF of two numbers


def GCF(num1,num2):
    
    for i in range (0,num1):
        if num1%(num2-i) == 0:
            return(num1 - i)
            break
        
        
GCF(16,64)
