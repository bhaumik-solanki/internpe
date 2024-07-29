import random

print("Welcome to Connect Four")
print("-----------------------")

letters = ["A", "B", "C", "D", "E", "F", "G"]
board = [["" for _ in range(7)] for _ in range(6)]

numRows = 6
numCols = 7

def displayBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for r in range(numRows):
        print("\n   +----+----+----+----+----+----+----+")
        print(r, " |", end="")
        for c in range(numCols):
            if board[r][c] == "🔵":
                print("", board[r][c], end=" |")
            elif board[r][c] == "🔴":
                print("", board[r][c], end=" |")
            else:
                print(" ", board[r][c], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def placeChip(position, chip):
    board[position[0]][position[1]] = chip

def checkWinner(chip):
    for r in range(numRows):
        for c in range(numCols - 3):
            if board[r][c] == chip and board[r][c + 1] == chip and board[r][c + 2] == chip and board[r][c + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    for c in range(numCols):
        for r in range(numRows - 3):
            if board[r][c] == chip and board[r + 1][c] == chip and board[r + 2][c] == chip and board[r + 3][c] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    for r in range(numRows - 3):
        for c in range(numCols - 3):
            if board[r][c] == chip and board[r + 1][c + 1] == chip and board[r + 2][c + 2] == chip and board[r + 3][c + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
        for c in range(3, numCols):
            if board[r][c] == chip and board[r + 1][c - 1] == chip and board[r + 2][c - 2] == chip and board[r + 3][c - 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False

def parseCoordinate(inputString):
    return [int(inputString[1]), letters.index(inputString[0])]

def isPositionAvailable(position):
    return board[position[0]][position[1]] == ""

def checkGravity(position):
    belowPosition = [None] * 2
    belowPosition[0] = position[0] + 1
    belowPosition[1] = position[1]
    if belowPosition[0] == 6:
        return True
    if isPositionAvailable(belowPosition) == False:
        return True
    return False

def main():
    turnCounter = 0
    while True:
        displayBoard()
        
        if turnCounter % 2 == 0:
            while True:
                chosenPosition = input("\nChoose a space (e.g., A0): ").strip().upper()
                try:
                    coordinate = parseCoordinate(chosenPosition)
                    if isPositionAvailable(coordinate) and checkGravity(coordinate):
                        placeChip(coordinate, '🔵')
                        break
                    else:
                        print("Not a valid coordinate")
                except (IndexError, ValueError):
                    print("Error occurred. Please try again.")
            if checkWinner('🔵'):
                displayBoard()
                break
        else:
            while True:
                aiChoice = random.choice(letters) + str(random.randint(0, 5))
                aiCoordinate = parseCoordinate(aiChoice)
                if isPositionAvailable(aiCoordinate) and checkGravity(aiCoordinate):
                    placeChip(aiCoordinate, '🔴')
                    print(f"AI chooses: {aiChoice}")
                    break
            if checkWinner('🔴'):
                displayBoard()
                break

        turnCounter += 1

if __name__ == "__main__":
    main()
