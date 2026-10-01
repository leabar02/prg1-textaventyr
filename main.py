
print("What is your name?")

player = input()

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
    print("What is your name?")
    
    player = input()
    
    print("Next question.")
    print("Which Item is more worth in Attack On Titan Revolution, attack serum or colossal serum?")
    
    answer = input()

    if answer == "Attack serum":
        print("That is wrong! For that reason it is game over for you.")
        print(f"{player} is shot to death. GAME OVER!")
    else:
        print("That is right! You will now proceed to the next question.")
        print("The next question will be harder than the last one so don't be surprised if you get it wrong.")
        print("Now the next question will be done in the next room which is located beside this one. so go there now!")
        print(f" {player} is going to the next room. ")
        print("There the voice speaks again, now colder and more robotic then before.")
        print("What is your name?")

        player = input()

        print(f"Welcome {player} ")
        print("The next question we are going to ask you is" )
        print("Who is stronger in Naruto Shippudden; Madara Uchiha or Sasuke Uchiha? ")

        answer = input()

        if answer == " Sasuke Uchiha":
            print("That is very wrong.")
            print("Madara outpasted Sasuke in every way, but sadly black zetsu killed him.")
            print("For answering wrong we have decided to test what happens if we put you into a tank full with acids.")
            print(f" {player} is thrown into a tank full with acids and gets desolved. GAME OVER!")
        else:
            print(f" {player} has gotten the right answer and gets to proceed to the next question.")
            print("The next question will be the final one, there are two doors infront of you. Choose which you will go through.")
            print("Door A, or Door B. ")

            answer = input()

            if answer == "Door A":
                print(f"{player} goes through door A, there is nothing but black space there. Then you hear an explosion and everything goes silent.")
                print(f"{player} has died and has failed the experiment. GAME OVER")
            else: 
                print(f" {player} goes through door B, and suddenly everything is burning. You feel cold and fear takes hold of {player}. ")
                print(f"After a few minutes {player} dies. GAME OVER!")
            
                
else:
    print("Go to right door and open it, ")




