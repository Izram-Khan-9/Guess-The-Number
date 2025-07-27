import random

# Introduction
user_name = input('Enter your name: ')
print(f'\nYou are welcome {user_name}🎉👏.')
print('For help, enter 9999.')
print('\n_-_-_-_-_-_-_-_-_-_-_-_1_GUESS_THE_NUMBER_1000_-_-_-_-_-_-_-_-_-_-_-_-_\n')

# Random number generation
random_choice = random.randint(1,1000)
# Initializing the number of guesses
no_of_guesses = 1

# Game loop
while True:
    try:

        # Taking users's guess
        users_guess = int(input(f'Enter you guess number {no_of_guesses}: '))
        
        # Checking if the number is between 1 and 100
        if users_guess >= 1 and users_guess <= 1000: 
                
            # if the number is equal to the random number
            if users_guess == random_choice: 
                print('\nCongratulations🎉👏')
                print(f'You guessed it right in {no_of_guesses} guesses✅')
                print(f'The number was {random_choice}\n')

                # Asking the user if they want to play again
                print('\n')
                play_again = input('Do you want to play again? (y/n): ')
                print('\n')
    
                # if the user wants to play again
                if play_again == 'y':
                    no_of_guesses = 1
                    continue
    
                # if the user does not want to play again
                else:
                    print('\nThank you for playing the game💓😍')
                    print('I hope you enjoyed the game❤️🔥')
                    print('Follow me to get more amazing games like this one.')
                    print('Have a nice day😊')
                    break
                    
            # if the number is greater than the random number
            elif users_guess > random_choice:
                print('\nThe number is less than your guess👇\n')
                no_of_guesses += 1
                    
            # if the number is less than the random number
            elif users_guess < random_choice:
                print('\nThe number is greater than your guess👆\n')
                no_of_guesses += 1
                               
        # if the number is not between 1 and 100
        elif users_guess < 1 or users_guess > 1000:           
            
             # if the user enters 999 for help
            if users_guess == 9999: 
                print('\nWelcome to the game\'s help section.')
                print('Here are the rules:')
                print('1. You have to guess a number between 1 and 100')
                print('2. You have to guess the number in the least number of guesses')
                print('3. Everytime you guess a number, you will be told if the number is greater or less.') 
                print('4. After reading the help, the program will stop.')
                print('5. To play the game again, you have to restart the program.')
                print('6. Thanks for playing the game.💓😍')
                print('7. I hope you enjoy the game❤️🔥\n')
                break

            # if the user enters a number not between 1 and 100
            else:
                print('\nThe number you have entered is not between 1 and 100❌\n')
            
    # if the user enters a string
    except ValueError: 
     print('The number you have entered is not an integer❌')