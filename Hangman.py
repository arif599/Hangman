import WordSupply

# add classes for Player for multiplayer version

def main():
    print("Starting a game of Hangman...\n")
    welcome()

def startgame(attempts_int, wordLength_int):

    attemptedChars_list = []
    word_str = WordSupply.pickWord(wordLength_int)
    gameWord_str =  "*" * len(word_str)
    print(f"GAME WORD: {gameWord_str}") 

    #loop, chagne to true
    while '*' in gameWord_str:
        userGuess_char = input("Enter a character: ")

        if userGuess_char in attemptedChars_list:
            print(f"You has already tried {userGuess_char}.")
            print('-'*75)
        elif userGuess_char in word_str:
            tempWord_str = ""

            for i in range(len(word_str)-1):
                if userGuess_char != word_str[i]:
                    if gameWord_str[i] == "*":
                        tempWord_str += (word_str[i]).replace(word_str[i], "*")
                    else:
                        tempWord_str += word_str[i]
                else:
                    tempWord_str += userGuess_char
            
            gameWord_str = tempWord_str
            print(f"Correct {userGuess_char} was in word: {gameWord_str}")
            print('-'*75)
            attemptedChars_list.append(userGuess_char)
                
        else:
            attempts_int -= 1
            print(f"Wrong {userGuess_char} was not in word: {gameWord_str}. {attempts_int} more attempts remaining")    
            print('-'*75)            

            if attempts_int == 0:
                #one last attempt, say the word (use google voice)
                print(f"YOU LOST the word was: {word_str}")
                finished()
                break
    print("YOU WON")
    finished()


        
def finished():
    playAgin_char = input("Want to play again? (y/n)")
    if playAgin_char == 'y':
        welcome()
    else:
        print("Finished")
        

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