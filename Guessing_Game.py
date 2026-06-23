import random, colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

n = random.randint(1,100)
guesses = []

print(Fore.GREEN + "ggggg  u   u  eeeee   ssss   ssss  iiiii  n   n  ggggg")
print(Fore.GREEN + "g      u   u  e      s      s        i    nn  n  g    ")
print(Fore.GREEN + "g      u   u  eee     s      s       i    n n n  g    ")
print(Fore.GREEN + "g  gg  u   u  e         s      s     i    n n n  g  gg")
print(Fore.GREEN + "g   g  u   u  e          s      s    i    n  nn  g   g")
print(Fore.GREEN + "ggggg  uuuuu  eeeee  ssss   ssss   iiiii  n   n  ggggg")
print("")
print(Fore.RED + "ggggg  aaaaa  m   m  eeeee")
print(Fore.RED + "g      a   a  mm mm  e    ")
print(Fore.RED + "g      a   a  m m m  eeeee")
print(Fore.RED + "g  gg  aaaaa  m m m  e    ")
print(Fore.RED + "g   g  a   a  m   m  e    ")
print(Fore.RED + "ggggg  a   a  m   m  eeeee")
print("")

while True:
    print("Welcome to the " + Fore.YELLOW + "Guessing Game!")
    print("Type " + Fore.YELLOW + "'help'" + Fore.WHITE + " for instructions, " + Fore.YELLOW + "'exit'" + Fore.WHITE + " to exit or " + Fore.YELLOW + "'start'" + Fore.WHITE + " to begin.")
    menu = input(Style.DIM + ">")
    print("")
    if menu == "start":
        break
    elif menu == "help":
        print("In this game, you must guess a " + Fore.LIGHTGREEN_EX + "random" + Fore.WHITE + " number beetwen 1-100.")
        print("If your guess is " + Fore.LIGHTGREEN_EX + "closer" + Fore.WHITE + " to the number then your last guess, then you will see the word " + Fore.LIGHTRED_EX + "'Warm'" + Fore.WHITE + ".")
        print("Otherwise, you will see " + Fore.LIGHTCYAN_EX + "'Cold'" + Fore.WHITE + ".")
        print("To " + Fore.YELLOW + "win" + Fore.WHITE + ", you must guess the number with as " + Fore.LIGHTBLUE_EX + "least" + Fore.WHITE + " tries as possible!")
        print(Back.RED + Fore.BLACK + "You only have 10 tries.")
        print("Type " + Fore.YELLOW + "'exit'" + Fore.WHITE + " to go back to the main menu.")
        menu2 = input(Style.DIM + ">")
        print("")
        if menu2 == "exit":
            continue
        else:
            print(Back.RED + Fore.BLACK + ">Invalid answer")
            print("")
    elif menu == "exit":
        exit()
    else:
        print(Back.RED + Fore.BLACK + ">Invalid answer")
        print("")

while True:
    guess = int(input("Enter your guess here : " + Fore.YELLOW ))
    guesses.append(guess)
    if guess < 1 or guess > 100:
        print(Back.RED + Fore.BLACK + "Guess out of range")
        guesses.pop()
    elif guess == n:
        print("\n")
        print(Back.YELLOW + Fore.BLACK + "You win!")
        print(f"It took you {len(guesses)} tries.")
        print(Fore.GREEN + "Reopen" + Fore.WHITE +" the game to try again...")
        print("")
        break
    else:
        if len(guesses) == 1:
            if abs(guess - n) <= 10:
                print(Fore.LIGHTRED_EX + "Warm")
            else:
                print(Fore.LIGHTCYAN_EX + "Cold")
        else:
            if not len(guesses) >= 10:
                if abs(guess - n) < abs(n - guesses[-2]):
                    print(Fore.LIGHTRED_EX + "Warmer")
                else:
                    print(Fore.LIGHTCYAN_EX + "Colder")
            else:
                print("\n")
                print(Back.RED + Fore.BLACK + "YOU FAILED")
                print("The correct answer was "+Fore.YELLOW+f"{n}")
                print(Fore.GREEN + "Reopen" + Fore.WHITE +" the game to try again...")
                print("")
    