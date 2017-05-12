
#print instructions about how to play mancala?

LP1 = []
LP2 = []
lenofsmalldivets = 0         #length of LP1 and LP2 is lenofsmalldivets + 1
numOfStones = 0
### 2 lists, where the last index is the "basin" 

def height():
    #retrieves the value we will use for heightOfRest, and makes sure it's an
    #appropriate number
    ourHeight = int(input("How long would you like the board to be? Remember it has to be greater than zero!"))
    if ourHeight <= 0:
        print("Sorry, try a bigger number!")
        return height()
    else:
        return ourHeight

lenofsmalldivets = height()

def startingStones():
    #numOfStones retrieves the number of stones we will start with, and makes
    #sure the number is appropriate
    num = int(input("And how many stones would you like to start with? Let's say, between one and ten?"))
    if (num > 10):
        print("Too high!")
        return startingStones()
#    elif (num < 1):
#        print("Too low!")
#        return startingStones()
    else:
        return num

numOfStones = startingStones()

def makeBoard():
    #creates the Mancala board, for technical use (fills with the appropriate
    #number of stones)
    i = 0
    for i in range(0, lenofsmalldivets):
        LP1.append(numOfStones)
        LP2.append(numOfStones)
    LP1.append(0)
    LP2.append(0)

makeBoard()

def printBoard():
    #prints the current board for the user
    print("\nP2\n")
    print("(  %s  )" % LP1[lenofsmalldivets])
    for i in range(0, lenofsmalldivets):
        print("(%s) (%s)" % (LP2[i], LP1[lenofsmalldivets - 1 - i]))
    print("(  %s  )" % LP2[lenofsmalldivets])
    print("\n     P1\n")
    
    
printBoard()


def gameOverWon():
    #checks if the smaller divets are empty, and if so, who won
    ### MAYBE IF NOONE WON TAKE IT BACK TO MOVES
    P1Count = 0
    for x in range(0, lenofsmalldivets):
        P1Count += LP1[x]
    P2Count = 0
    for x in range(0, lenofsmalldivets):
        P2Count += LP2[x]
    if P1Count == 0 or P2Count == 0:
        print("Game over!")
        if P1Count + LP1[lenofsmalldivets] > P2Count + LP2[lenofsmalldivets]:
            print("And the winner is ... Player 1!")
        elif P1Count + LP1[lenofsmalldivets] < P2Count + LP2[lenofsmalldivets]:
            print("And the winner is ... Player 2!")
        else:
            print("And the winner is ... oh wait, it's a tie!")
            
        
            

gameOverWon()


#Function ideas

#one that 'does a move' and you input which player does the move (P1 or P2)
#    maybe split into moves stones and landing on empty next to stones
#checks to see if the game is over (no more stones in the small divets) and who
#    won
