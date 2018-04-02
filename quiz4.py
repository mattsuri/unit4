#Matthew Suriawinata
#4/2/18
#quiz4.py

def count(num):
    for i in range(1,(num+1)):
        print(i)
        
count(7)
        

def excitedPrint(statement):
    print(statement.upper(), "!!!")

excitedPrint("i love <3 programming")

def firstLetter(word):
    for i in word:
        return(i)
        break
    
print(firstLetter("Smeds"))

def repeats(num1,num2,num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        return True
    else:
        return False



print(repeats(5,6,5))
