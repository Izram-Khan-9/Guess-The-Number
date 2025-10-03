import random
import time

# Introduction
user_name = input('Enter your name: ')
print(f'\nYou are welcome {user_name}🎉👏.')

# Description
print('\n------Game-Description------')
print('\nGuess the hidden number within the correct range!')
print('You can choose from 5 difficulty levels:')
print('Level 1 (Easy): 1 - 10')
print('Level 2 (Medium): 1 - 100')
print('Level 3 (Hard): 1 - 1,000')
print('Level 4 (Extreme): 1 - 10,000')
print('Level 5 (Impossible): 1 - 100,000\n')
print('------Scoring-System------')
print('\nFirst try → 💎 Diamond')
print('Less than 4 tries → 🔴 Ruby')
print('Less than 6 tries → 🟢 Emerald')
print('Less than 11 tries → 🟡 Gold')
print('Less than 21 tries → ⚪ Silver')
print('21 or more tries → 🟤 Bronze')
print('If your guess is very close (within 5), you’ll get a hint.')

print('\n_-_-_-_-_-_-_-_-_-_-_-GUESS_THE_NUMBER-_-_-_-_-_-_-_-_-_-_-_-_\n')

# Random number generation
random_number = None
level_1_choice = random.randint(1,10)
level_2_choice = random.randint(1,100)
level_3_choice = random.randint(1,1000)
level_4_choice = random.randint(1,10000)
level_5_choice = random.randint(1,100000)


# Random message when the user is close
close_messages = [
    "🔥 Hot! You’re very close!",
    "❄️ Cold… but warming up!",
    "🎯 Almost hit the bullseye!",
    "👀 You’re just a few steps away!",
    "⚡ So close, I can feel the sparks!",
    "🚀 You’re nearly there, just a small leap!",
    "🧩 You’re fitting the last piece of the puzzle!",
    "💡 Very near… your guess is glowing!"
]

# Messages for choosing each level

# Level 1 (Easy: 1–10)
level_1_messages = [
    "So you’ve chosen the easiest one… afraid of real numbers? 😏",
    "Baby mode unlocked! 🍼 Let’s see if you can even handle this.",
    "Numbers from 1 to 10… wow, such bravery 👏.",
    "The training wheels are still on, huh? 🚲",
    "Level 1: Where legends *don’t* start 😂."
]

# Level 2 (Medium: 1–100)
level_2_messages = [
    "A little more courage this time! 🔥 Medium mode chosen.",
    "100 numbers, 1 winner. Will it be you? 🎯",
    "Not too easy, not too hard… the comfort zone level 🛋️.",
    "Medium mode… the level for cautious warriors ⚔️.",
    "Let’s see if your guessing skills stretch beyond 10 😏."
]

# Level 3 (Hard: 1–1,000)
level_3_messages = [
    "Now we’re talking! 😈 A thousand numbers await you.",
    "Hard mode? Respect 🫡… but don’t cry later.",
    "This is where amateurs break and champions rise 🏆.",
    "You really think you can outsmart the odds of 1 in 1000? 🤯",
    "Your brain vs 1000 numbers… place your bets 💸."
]

# Level 4 (Extreme: 1–10,000)
level_4_messages = [
    "Extreme mode?! Okay, now I’m impressed 😳.",
    "10,000 numbers… do you have infinite patience? 🕰️",
    "This isn’t a game anymore, it’s a war 💣.",
    "Extreme mode: where hope goes to die 💀.",
    "You’ve chosen madness… may the RNG gods bless you 🙏."
]

# Level 5 (Impossible: 1–100,000)
level_5_messages = [
    "Impossible mode?! Who hurt you? 💔",
    "1 in 100,000… you’re basically buying a lottery ticket 🎟️.",
    "If you win this, I’ll call you a legend forever 👑.",
    "Impossible mode: where sanity takes its final breath 🥀.",
    "You just unlocked Ultra Madness 🔥… prepare to suffer!"
]

# Function for the dot animation

def animation(message='Loading', delay=0.2):
    print(message, end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(delay)
    print()
    
# Initializing the number of tries
tries = 1

# Asking user the select the level

while True:
    try:
        ask_level = int(input('Choose a level(1/2/3/4/5): '))
        
        if ask_level == 1: # If user chooses level 1
            random_number = level_1_choice
            print('\n')
            print(random.choice(level_1_messages))
            break
            
        elif ask_level == 2: # If user chooses level 2
            random_number = level_2_choice
            print('\n')
            print(random.choice(level_2_messages))
            break
        
        elif ask_level == 3: # If user chooses level 3
            random_number = level_3_choice
            print('\n')
            print(random.choice(level_3_messages))
            break
        
        elif ask_level == 4: # If user chooses level 4
            random_number = level_4_choice
            print('\n')
            print(random.choice(level_4_messages))
            break
        
        elif ask_level == 5: # If user chooses level 5
            random_number = level_5_choice
            print('\n')
            print(random.choice(level_5_messages))
            break
        
        else: # If user enters any number except (1/2/3/4/5)
            print('Choose (1/2/3/4/5)')
            
    except ValueError: # If user doesn't enters a number
        print('❌Invalid input❌')
        print('Please enter (1/2/3/4/5)')

# Main code
while True:
    
    try:
        # Taking users's guess
        user_guess = int(input(f'\nEnter you guess No. {tries}: '))
                
        # if the number is equal to the random number in first try
        if user_guess == random_number and tries == 1: 
            print('🎉 Perfect Guess')
            print('Diamond → 💎 Diamond! Incredible guesser!')
            break
        
        # if the number is equal to the random number in n number of tries
        elif user_guess == random_number:
            print('\n🎉 You have guessed it right!')
            print(f'The actual number was {random_number}')
            print(f'It took you {tries} tries to guess the actual number')
            
            # Defining scoring system
            if tries <= 3: # Ruby
                print('❤️ Ruby! Amazing skills!')
                break
            
            elif tries <= 6: # Emerald
                print('Emerald → 💚 Emerald! Well done')
                break
            
            elif tries <= 10: # Gold
                print('🥇 Gold! Solid effort!')
                break
            
            elif tries <= 21: # Silver
                print("🥈 Silver! Took a while, but you got it!")
                break
            
            else: # Bronze
                print('You guessed it! 🥉 Bronze earned after 20+ tries.')
                
        # If the difference between the random number and user guess is less than or equal 5
        elif abs(random_number - user_guess) <= 5: 
            tries += 1
            animation()
            print(random.choice(close_messages))
        
        # If the user guess is greater then the random number
        elif user_guess > random_number:
            animation()
            print('Guess is higher then the actual number⬆️')
            tries += 1
        
        # If the user guess is less then the random number
        elif user_guess < random_number:
            animation()
            print('Guess is lower then the actual number⬇️')
            tries += 1
                
        else:
            print('Guess out of range!')
    
    # If user enters anything except a number
    except ValueError:
        print('❌Invalid input❌')
        print('Enter a number')
            
 #____________________________________END____________________________________