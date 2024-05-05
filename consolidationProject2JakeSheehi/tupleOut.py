import random

def rollDice():
    #simulates rolling three dice and returns a tuple of their values
    return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

def isTupleOut(diceRolls):
    #checks if all three dice have the same value
    return len(set(diceRolls)) == 1

def getFixedDice(diceRolls):
    #returns a list of indices corresponding to fixed dice
    fixed = []
    for i in range(len(diceRolls)):
        if diceRolls.count(diceRolls[i]) >= 2:
            fixed.append(i)
    return fixed

def playerTurn():
    #implements one player's turn
    score = 0
    diceRolls = rollDice()

    while True:  
        print("You rolled:", diceRolls)

        if isTupleOut(diceRolls):
            print("Tuple out! No points this turn.")
            return 0

        fixedDice = getFixedDice(diceRolls)
        if fixedDice:
            print(f"Dice at positions {fixedDice} are fixed.")
            reroll = input("Reroll unfixed dice? (y/n): ").lower()
        elif not any(diceRolls): 
            reroll = 'y'  
        else:
            reroll = input("Reroll all dice? (y/n): ").lower()

        if not any(diceRolls) or reroll != 'y':  
            score = sum(diceRolls)
            print("You ended your turn with a score of", score)
            return score

        # Reroll unfixed dice
        if diceRolls:  # Check if diceRolls is not empty
            newRolls = []  # Create an empty list for new rolls
            for i in range(len(diceRolls)): 
                if i not in fixedDice:
                    newRolls.append(random.randint(1, 6))  # Add new roll
                else:
                    newRolls.append(diceRolls[i])  # Keep fixed dice
            diceRolls = newRolls  # Update diceRolls

def main():
    print("Welcome to Tuple Out!")
    numPlayers = int(input("How many players? "))

    targetScore = int(input("What is the target score? "))  
    playerScores = [0] * numPlayers

    currentPlayer = 0
    while max(playerScores) < targetScore: 
        print(f"\nPlayer {currentPlayer + 1}'s turn.")
        score = playerTurn()
        playerScores[currentPlayer] += score

        currentPlayer = (currentPlayer + 1) % numPlayers

    winner = playerScores.index(max(playerScores))
    print(f"\nGame Over! Player {winner + 1} wins!")

if __name__ == "__main__":
    main()