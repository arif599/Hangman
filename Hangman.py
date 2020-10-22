import WordSupply

def main():
    print("Starting a game of Hangman...\n")
    welcome()

def startgame(attempts_int, wordLength_int):

    word_str = WordSupply.pickWord(wordLength_int)
    gameWord_str =  "*" * len(word_str)
    print(f"GAME WORD: {gameWord_str}") 

    #loop, chagne to true
    while "*" in gameWord_str:
        userGuess_char = input("Enter a character: ")
        
        if userGuess_char in word_str:
            tempWord_str = gameWord_str
            gameWord_str = ""

            for i in range(len(word_str)-1):
                if userGuess_char != word_str[i]:
                    if tempWord_str[i] == "*":
                        gameWord_str += (word_str[i]).replace(word_str[i], "*")
                    else:
                        gameWord_str += word_str[i]
                else:
                    gameWord_str += userGuess_char
            print(f"Correct {userGuess_char} was in word: {gameWord_str}")
            
        else:
            print(f"Wrong {userGuess_char} was in word: {gameWord_str}")

        

def welcome():

    attempts_int = wordLength_int = 0

    while True:

        attempts_int = int(input("Select the number of attempts [1-15]: "))
        if(attempts_int > 15 and attempts_int < 0):
            print("You entered a wrong number for the number of attempts, try again.")
            continue

        wordLength_int = int(input("Select the minimum word length [4-12]: "))
        if(wordLength_int > 12 and attempts_int < 4):
            print("You entered a wrong number for the number of attempts, try again")
            continue

        break

    startgame(attempts_int, wordLength_int)
















if __name__ == "__main__":
    main()