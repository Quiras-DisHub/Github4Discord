"""
This is a simple Connect Four game
"""
import sys

emptySpace = '.'
player1 = 'X'
player2 = 'O'
boardWidth = 7
boardHeight = 6
columnLabels = ('1','2','3','4','5','6','7')
assert len(columnLabels) == boardWidth

def connectFour():
    print("Welcome to Connect Four!")
    gameBoard = getNewBoard()
    playerTurn = player1
    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn,gameBoard)
        gameBoard[playerMove] = playerTurn
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print('Player ' + playerTurn + ' has won!')
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print('There is a tie!')
            sys.exit()
        if playerTurn == player1:
            playerTurn = player2
        elif playerTurn == player2:
            playerTurn = player1
    
def getNewBoard():
    board = {}
    for columnIndex in range(boardWidth):
        for rowIndex in range(boardHeight):
            board[(columnIndex, rowIndex)] = emptySpace
    return board

def displayBoard(board):
    tileChars = []
    for rowIndex in range(boardHeight):
        for columnIndex in range(boardWidth):
            tileChars.append(board[(columnIndex, rowIndex)])
    print("""
           1234567
          +-------+
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          |{}{}{}{}{}{}{}|
          +-------+""".format(*tileChars))

def askForPlayerMove(playerTile, board):
    while True:
        print("Player {}, enter a column or QUIT:".format(playerTile))
        response = input("> ").upper().strip()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if response not in columnLabels:
            print("Enter a number from 1 to {}.".format(boardWidth))
            continue
        columnIndex = int(response) - 1
        if board[(columnIndex, 0)] != emptySpace:
            print("That column is full, select another one.")
            continue
        for rowIndex in range(boardHeight - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == emptySpace:
                return(columnIndex, rowIndex)
            
def isFull(board):
    for rowIndex in range(boardHeight):
        for columnIndex in range(boardWidth):
            if board[(columnIndex, rowIndex)] == emptySpace:
                return False
    return True

def isWinner(playerTile, board):
    for columnIndex in range(boardWidth - 3):
        for rowIndex in range(boardHeight):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    for columnIndex in range(boardWidth):
        for rowIndex in range(boardHeight - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    for columnIndex in range(boardWidth - 3):
        for rowIndex in range(boardHeight - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile1 = board[(columnIndex + 2, rowIndex + 1)]
            tile1 = board[(columnIndex + 1, rowIndex + 2)]
            tile1 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False

if __name__ == '__main__':
    connectFour()