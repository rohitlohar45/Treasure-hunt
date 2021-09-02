def lets_play_again():

    ans = input("\nDo you want to play again? (y or n)")
    if ans == "y" or ans == "n":
        if ans == "y":
            start()
        else:
            print("See you again")
            game_over()
    else:
        print("Please Enter correct number")
        lets_play_again()


def game_over():
    quit()


def treasure_room():
    print("\nYou are now in a rooom filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")
    a = input(">")
    if a == 1:
        print("Game Over!")
        lets_play_again()
    else:
        print("YAY !!! WIN")
        lets_play_again()


def monster_room():
    print("\nThere is a monster here.")
    print("Behind the monster, there is another door.")
    print("The monster is sleeping")
    print("What would you do? (1 or 2)")
    print("1). Go through the door sliently.")
    print("2). Kill the monster and show your courage! ")
    a = int(input())
    if a == 1 or a == 2:
        if a == 1:
            treasure_room()
        else:
            print("Game Over!")
            lets_play_again()
    else:
        print("Please Enter correct number")
        monster_room()


def snake_room():
    print("\nThere is a snake here.")
    print("Behind the Snake is another door.")
    print("The snake is having eggs!")
    print("What would you do? (1 or 2)")
    print("1). Take the eggs.")
    print("2). Taunt the snake.")
    a = int(input())
    if a == 1 or a == 2:
        if (a == 1):
            print("\nYou want the eggs not the treasure!! That's why you were dinner for him")
            lets_play_again()
        else:
            treasure_room()
    else:
        print("Please Enter correct number")
        snake_room()


def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    
    a = input()
    if a == "l" or a == "r":
        if (a == "l"):
            snake_room()
        else:
            monster_room()
    else:
        print("\nPlease Enter correct number")
        start()


start()
