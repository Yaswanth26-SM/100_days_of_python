print(r''' _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| ''')

print("Welcome to Treasure Island.")
print("Your task is to find the treasure! ")
option = input("There are 3 paths: Left, Right, Straight, each path have treasure items!, select one at your choice......\n").lower()
if option == "left" or option == 'l' :
    print("You reached river!")
    swim = input("Do you want to swim? Type 'y' for Yes or 'n' for No....\n ").lower()
    if swim == "y":
        print("You found gold coins,your are on right path go ahead!")
    elif swim == "n":
        print("I entered on old damaged bridge, Aaaaahhh! Game over.")
    else:
        print("Something went wrong,Try again...")
elif option == "right" or option == 'r':
    cave = input("Do you like to enter in a cave? Type 'y' for Yes or 'n' for No \n").lower()
    if cave == "y":
        print("That's great, You found treasure map! ")
    elif cave == "n" :
        print("You're trapped by a snake....... Game over! ")
    else:
        print("Something went wrong,Try again...")
elif option == "straight" or option == 's':
    print("There's an old house with two different doors: Iron, Wood. ")
    door = input("Choose one door among them '.' for Iron or '_' for Wood.\n ")
    if door == ".":
        print("Poisonous gas leaked, You're dead!")
    elif door == "_":
        print("OMG! You found Tons of Gold.... Ahhh finally the treasure is yours")
    else:
        print("Something went wrong,Try again...")
else:
    print("Something went wrong,Try again...")
