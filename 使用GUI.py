import easygui 
import random
secret = random.randint(1,99)
guess = 0
tries = 0

easygui.msgbox('''hi! i'm the dread pirate roberts, and i have a secret!
it is a number from 1 to 99.i'll give you 6 tries.''')

while guess  != secret and tries < 6:
    guess = easygui.integerbox("waht's your guess,matey?")
    if not guess:break
    if guess < secret:
        easygui.msgbox(str(guess) + "is too low,ye scurvy dog!")
    elif guess >secret:
        easygui.msgbox(str(guess) + "is too high,landlubber!")
        tries += 1
if guess == secret:
     easygui.msgbox("Avast! Ye got it! Found my secret,ye did!")
else:
    easygui.msgbox("No more guesses! Better luck next time,matey!")
