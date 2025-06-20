import random

word_list= ['havana', 'banana','scenario','purple','elizabeth']
lives = 6

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += '_'
print("Word to guess: ", placeholder)

game_over = False
correct_letters = []
print("****************************<???>/6 LIVES LEFT****************************")

while not game_over:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    print("Word to guess: " + display)
    
    if guess not in chosen_word:
        print(f"You've guessed {guess},that's not in the word. You lose a life!")
        lives -= 1
        print(f"****************************<???>/{lives} LIVES LEFT****************************")
        
        if lives == 0:
            game_over =True
            print(f"It was {chosen_word}! You Lose!!!!")
            print(f"***********************YOU LOSE**********************")
            
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        