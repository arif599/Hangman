

def main():
    print("Starting a game of Hangman...\n")
    welcome()

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

    






if __name__ == "__main__":
    main()