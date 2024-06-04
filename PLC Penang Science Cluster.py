#!/usr/bin/env python

import random

def main():
    """Start Guessing the communication Application Used."""
    print("Guess Communication App !")
    
    App = [
        "Wattssapp",
        "Telegram",
        "Facebook",
        "IG",
        "TikTok",
        "Line",
        "Frienster"
        ]

    x =random.choice(App)
    print (x)
    max_trials= 5
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What App are we thinking of? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The Application is actually {x}.".format(guess))
        
main()