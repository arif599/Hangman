import WordSupply

def main():
    print("Starting a game of Hangman...\n")
    welcome()

def startgame(attempts_int, wordLength_int):

    gameWord_str = WordSupply.pickWord(wordLength_int)
    print("GAME WORD:", "*" * len(gameWord_str)) 

    #loop, chagne to true
    while "*" in gameWord_str:
        userGuess_char = input("Enter a character: ")
        
        if userGuess_char in gameWord_str:
            newGameWord_str = (gameWord_str).replace(userGuess_char, "*")
            print(f"GAME WORD: {newGameWord_str}")


        

def welcome():

    attempts_int = wordLength_int = 0

    while True:

        attempts_int = int(input("Select the number of attempts [1-15]: "))
        if(attempts_int > 15 or attempts_int < 0):
            print("You entered a wrong number for the number of attempts, try again.")
            continue

        wordLength_int = int(input("Select the minimum word length [4-12]: "))
        if(wordLength_int > 12 or attempts_int < 4):
            print("You entered a wrong number for the number of attempts, try again")
            continue

        break

    startgame(attempts_int, wordLength_int)
















if __name__ == "__main__":
    main()