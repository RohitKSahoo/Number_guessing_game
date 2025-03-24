import random
import pyttsx3

comp_num = random.randint(1, 100)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    try:
        num = int(input("Guess a number between 1 and 100: "))

        if num < comp_num:
            print("Too low")
        elif num > comp_num:
            print("Too high")
        else:
            print("Correct guess. Congratulations!")
            engine.say("Correct guess. Congratulations!")
            engine.runAndWait()
            break
    except ValueError:
        print("Sorry, that's not a number.")






