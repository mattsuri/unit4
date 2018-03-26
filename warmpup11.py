#Matthew Suriawinta
#3/26/18
#warmup11.py

def prime(num):
    for i in range (2,num):
        if num % i == 0:
            return False
    return True
        
       
print(prime(3))