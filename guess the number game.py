import random


def guess(x):
    random_number = random.randint(1, x)  # for getting random number we have to use this
    # random.randint(1,x) return the number between as (1 <= N <= x)
    # once the computer has number we need to guess the number and computer tells us that it is too high or too low or exact the number
    guess = 0
    while guess != random_number:
        guess = int(input(f'yo maboy guess the number (between 1 & {x}):  '))
        print(guess)

        # and we have to keep looping the number untill we got the number
        # but we also want that computer give us some clue , some kind of hint
        if guess < random_number:
            print('No, you are wrong guess some big number  dude!')
        elif guess > random_number:
            print('nah man! go some down guess low number')
    print(f'Damn! you hit the right number {random_number}' 'you WANT TO GUESS again!')

# if we want that our computer guess the number and we give some hint to computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)  # random.randint could throw some error here so we use the if else loop
        else:
            guess = low
        feedback = input(f'tell my boss the {guess} too high (H), too low (L), correct(C)?  '.lower())  # lower case call inputs
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
    print(f'yo motherboard! this is brilliant it guess {guess} the correctly ')

computer_guess(500) #guess(10) for we guess the number or computer_guess() for .
