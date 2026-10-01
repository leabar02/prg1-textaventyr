player = input("What is your name?")

print("Today we are conducting an experiment, where you are to answer questions, depending on your answer the outcome will be differnt.")
print("Question 1.")
print(f"{player} stands in a room, there are two ways leading out. One door on the right and one door on the left. ")
print("Which side do you choose, left or right?")

answer = input("Left or Right?")

if answer == "left":
    print("Go to the left door and open it, as you grip the door handle you feel a cill going down your spine.") 
    print("It is cold but you keep walking. A voice in the speakers which are on the walls suddenly says, walk until the next door. ")
    print(f" {player} arrives at the door.")
    print("The voice speaks again.")
    
    player = input()
    
    print("Next question.")
    print("Which Item is more worth in Attack On Titan Revolution, attack serum or colossal serum?")
    
    answer = input()

    if answer == "Attack serum":
        print("That is wrong! For that reason it is game over for you.")
        print(f"{player} is shot to death. GAME OVER!")
    else:
        print("That is right! You will now proceed to the next question.")

else:
    print("Go to right door and open it, ")




