#Matthew Suriawinata
#3/26/18
#printSquares.py 

def printSquares(cols, rows):
    for i in range(rows):
        print("+--" * cols + "+")
        for i in range(1,rows):
            print("|  " * cols + "|")
