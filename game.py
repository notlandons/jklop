import random

list1 = [
    "banana",
    "orange",
    "guitar",
    "rabbit",
    "purple",
    "school",
    "yellow",
    "mother",
    "camera",
    "potato",
    "sister",
    "father",
    "market",
    "router",
    "laptop",
    "monkey",
    "church",
    "pepper",
    "tomato",
    "skibid"
]

def choose_word(list):
    return random.choice(list)

def check_guess(word, guess):
    if guess == word:
        return "Correct! You guessed the word."

    correctness = []
    for i in range(len(word)):
        if guess[i] == word[i]:
            correctness.append(guess[i].upper())  
        elif guess[i] in word:
            correctness.append(guess[i])  
        else:
            correctness.append("#")
    
    return " ".join(correctness)

def again():
        x = input("Would you like to play again?")
        if x.lower() == "yes":
            play_wordle()
        else:
            print("Sad to see you go, bye bye")

def play_wordle():
    print("Welcome to Wordle!")
    print("You have 6 total attempts, use them wisely!")
    print("If the letter is in the word, it will be lowercase. If it's in the correct position, it'll be capital. Else you will see a # symbol.")
    
    word = choose_word(list1)
    max_attempts = 6
    attempts = 0
    guessed = False
    
    while attempts < max_attempts and not guessed:
        print(str(attempts),"/",str(max_attempts),"attempts used.")
        guess = input("Enter your guess (6 letter word): ").lower()
        
        if len(guess) != len(word):
            print("Please enter a 6 letter word.")
            continue
        
        result = check_guess(word, guess)
        print(result)
        
        if result.startswith("Correct!"):
            guessed = True
        
        attempts += 1
    
    if guessed:
        print(f"You guessed", word, "in", attempts, "attempts.")
    else:
        print("Out of attempts. The word was ", word)

    again()
           
play_wordle()

