import random
import time

def generateHero(role):
    with open(role) as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def menu():
    choices = int(input("What would you like to do? \n 1. Choose a random Character \n 2. Exit \n"))
    if choices == 1:
        completelyRandom = int(input("Would you like: \n 1. Any hero \n 2. A specific role \n"))
        if completelyRandom == 1:
            print("\n" + generateHero("all.txt") + "\n")
        elif completelyRandom == 2:
            roles = int(input("What role would you like to randomize? \n 1. Tanks \n 2. DPS \n 3. Supports \n"))
            if roles == 1:
                print("\n" + generateHero("tanks.txt") + "\n")
                time.sleep(2)

            elif roles == 2:
                print("\n" + generateHero("dps.txt") + "\n")
                time.sleep(2)

            elif roles == 3: 
                print("\n" + generateHero("supports.txt") + "\n")
                time.sleep(2)
                
            else:
                print("You seem to have picked something other than 1-3, generating from all heroes \n")
                print("\n" + generateHero("all.txt") + "\n")
                time.sleep(2)
                
        else:
            print("You seem to have picked something other than 1 or 2, generating from all heroes. \n")
            print("\n" + generateHero("all.txt") + "\n")
            
    elif choices == 2:
        print("Bye bye!")
        time.sleep(2)
        quit()
    else:
        print("Please choose a given option.")
        menu()

if __name__ == '__main__':
    while True:
        menu()