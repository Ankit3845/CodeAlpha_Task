import random
#step 1:define a small list of 5 predefined words
word_list=['apple','banana','grape','orange','peach']
#step 2:Randomly select one word from the list
chosen_word=random.choice(word_list)
#step 3:Initialize game variables
display=['_']*len(chosen_word)
lives=6
guessed_letters=[]
#step 4:Display welcome message
print("welcome to Hangman!")
print("Guess the word,one letter at a time.")
print("you have 6 incorrect guesses allowedd.\n")
#step 5:Main game loop
while lives > 0 and '_' in display:
    print("Word:","".join(display))
    guess=input("Enter a letter:").lower()
    #step 6:Input validation
    if not guess.isalpha() or len(guess)!=1:
        print("please enter a single letter.\n")
        continue
    if guess in guessed_letters:
        print("you already guessed that letter.\n")
        continue
    guessed_letters.append(guess)
    #step 7:check if guess is in the word
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                print("Correct!\n")
            else:
                lives-=1
                print(f"Incorrect! you have{lives} lives remaining.\n")
                #step 8: End of game
                if'_'not in display:
                    print("Congratulations! you guessed the word:",chosen_word)
                else:
                    print("Game Over! The correct word was:",chosen_word)