
name = input("Hey type your name: ")
print("Hello " + name + " welcome to my game!")
should_we_play = input("Do you want to play? ").lower()
# we use condition statement to check whether the please said yes or not
play = should_we_play.lower() == "yes"
print(play)

if play:
    print("We are gonna play")
if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play game")
    direction = input("Do you wanna go right or left? ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, Game Over, try again")
    elif direction == "right":
        choice = input(
            "Okay, you see a bridge, you want to go under the water or cross it? ")
        if choice == "swim":
            print("Eligatgor will eat you, you are die, Game Over, Try again")
        else:
            print("You have crossed the bridge, you won the GOLD")
        # print("We are goona right direction")
    else:
        print("Wrong direction! Game Over")
else:
    print("We are NOT gonna play game")
