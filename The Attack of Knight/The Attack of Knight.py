##Problem Link: https://www.codechef.com/submit/KNIGHTATTACK
##Problem Code: KNIGHTATTACK

## Created a list to record all possible positions of knight
l=[]
def XY(x,y):
    ##Knights position can not go beyond 8*8
    if 0<x<9 and 0<y<9:
        l.append((x,y))

##Recording valid moves in XY function to append in list
def validMoves(x,y):
    XY(x + 2, y + 1)
    XY(x + 2, y - 1)
    XY(x - 2, y + 1)
    XY(x - 2, y - 1)
    XY(x + 1, y + 2)
    XY(x - 1, y + 2)
    XY(x + 1, y - 2)
    XY(x - 1, y - 2)


##if the list contains same element, that means knight can kill both pieces
def checkIfDuplicates(listOfElems):
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


##Taking input for test cases
T=int(input())

##Main
for i in range(T):
    x1, y1 = input().split()
    x2, y2 = input().split()

    ##Append all the valid moves
    validMoves(int(x1),int(y1))
    validMoves(int(x2),int(y2))

    ##Checking for duplicates
    if checkIfDuplicates(l) == True:
        print("YES")
    else:
        print("No")
    ##Clear the list after returning result
    l.clear()

