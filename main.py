player = input("What is your name? ")

print("Today we are conducting an experiment, where you are to answer questions, depending on your answer the outcome will be differnt.")
print()
print("Question 1.")
print()
print(f"{player} stands in a room, there are two ways leading out. One door on the right and one door on the left. ")
print()
print("Which side do you choose?")

answer = input("Left or Right?")

if answer == "left":
    print("Go to the left door and open it, as you grip the door handle you feel a cill going down your spine.") 
    print()
    print("It is cold but you keep walking. A voice in the speakers which are on the walls suddenly says, walk until the next door. ")
    print()
    print(f" {player} arrives at the door.")
    print()
    print("The voice speaks again.")
    print()
    print("What is your name?")

    player = input("What is your name?")
    
    print("Next question.")
    print()
    print("Which Item is more worth in Attack On Titan Revolution, attack serum or colossal serum?")
    
    answer = input()

    if answer == "Attack serum":
        print("That is wrong! For that reason it is game over for you.")
        print()
        print(f"{player} is shot to death. GAME OVER!")
    else:
        print("That is right! You will now proceed to the next question.")
        print()
        print("The next question will be harder than the last one so don't be surprised if you get it wrong.")
        print()
        print("Now the next question will be done in the next room which is located beside this one. so go there now!")
        print()
        print(f" {player} is going to the next room. ")
        print()
        print("There the voice speaks again, now colder and more robotic then before.")
        print()
        print("What is your name?")
        print()

        player = input()

        print()
        print(f"Welcome {player} ")
        print()
        print("The next question we are going to ask you is" )
        print()
        print("Who is stronger in Naruto Shippudden; Madara Uchiha or Sasuke Uchiha? ")

        answer = input()

        if answer == " Sasuke Uchiha":
            print("That is very wrong.")
            print()
            print("Madara outpasted Sasuke in every way, but sadly black zetsu killed him.")
            print()
            print("For answering wrong we have decided to test what happens if we put you into a tank full with acids.")
            print()
            print(f" {player} is thrown into a tank full with acids and gets desolved. GAME OVER!")
        else:
            print(f" {player} has gotten the right answer and gets to proceed to the next question.")
            print()
            print("The next question will be the final one, there are two doors infront of you. Choose which you will go through.")
            print()
            print("Door A, or Door B. ")

            answer = input()

            if answer == "Door A":
                print(f"{player} goes through door A, there is nothing but black space there. Then you hear an explosion and everything goes silent.")
                print()
                print(f"{player} has died and has failed the experiment. GAME OVER")
            else: 
                print(f" {player} goes through door B, and suddenly everything is burning. You feel cold and fear takes hold of {player}. ")
                print()
                print(f"After a few minutes {player} dies. GAME OVER!")
            
                
else: 
    print("Go to the right door and open it,  ")

    player = str(input("What is your name"))
    
    print(f"{player} has gone through the right door, {player} will now begin the experiment. ")
    print()
    print(f"{player} walks through a long corridor, there are old paintings of people on the walls. There in the end of the corridor there is a door slightly open, through it there is a shining light.")
    print()
    print(f"Attention {player} must go through the door otherwise you are awaiting a tragic fate. ") 
    print()
    print(f"{player} goes through the door.")
    print()
    print("Question 1.")
    print()
    print("Which mountain is higher?")
    print()
    print("A. Großglockner. B. Matterhorn C. Zugspitze.")

    answer = input("Großglockner, Matterhorn, Zugspitze")

    if answer == "Großglockner": 
        print("Wrong!")
        print()
        print("proceed to next question.")
        print(f"{player} is about to go to the next qustion, then {player} hears a noise comming from below. The floor is viberating, then it opens and {player} falls in.")
        print()
        print("Game over!")

    elif answer == "Matterhorn":
        print(f"{player} has chosen the correct answer and will now be alowed to go to the next question.")
        print()
        print("The next question will be the final one.")
        print()
        print("Final Question!")
        print()
        print("The final question will be impossible!")
        print()
        print("Which is my favorite family in AOTR")
        print()
        print("Reiss, Helos, Fritz, Ackermann. or Yeager. Choose one only.")

        answer = input()

        if answer == "Reiss":
            print("wrong")
            print()
            print("close but no.")
            print()
            print("Game Over")
            print()
            print(f"{player} is put in jail!")

        elif answer == "Fritz":
            print("So close, but it's still wrong!")
            print()
            print("Game Over")
            print(f"{player} is put in jail!")

        elif answer == "Helos":
            print("You got it right!")
            print()
            print(f"{player} has won and will be given the title Champion!")
            print()
            print("player won! and can now return home to freedom")

        elif answer == "Ackermann":
            print("Extremly close but no!")
            print()
            print("Game Over!")
            print(f"{player} is put in jail!")

        elif answer == "Yeager":
            print("Wrong!")
            print()
            print("Game Over!")
            print(f"{player} is put in jail!")

        else:
            print(f"since {player} answered wrong, {player} is thrown into a lake with water but {player} doesn't float but instead sinks to the bottom and drowns.")
            print()
            print(f"Game over! {player} has died from lack of oxygen. ")
    
    elif answer == "Zugspitze":
        print("Wrong!")
        print()
        print(f"{player} has gotten the most wrong answer but will be given a second chance.")
        print()
        print(f"If {player} answers next question right, then {player} gets a mystery price. ")
        print()
        print("Final Question!")
        print()
        print("What is more worth in aotr Gunbai or berserkers mane or devil wing?")

        answer = input("Which is worth more, (Gunbai, berserkers mane or devil wing): ")

        if answer.lower() == "Gunbai":
            print("Almost")
            print()
            print("Game over!")
        elif answer.lower() == "berserkers mane":
            print("Almost")
            print()
            print("Game Over!")
        elif answer.lower() == "devil wing":
            print("Wrong!")
            print()
            print("")

    else: 
        print("player hasn't answered the questions and will therefore be terminated.")
        print(f"{player} suddenly doesn't feel his heartbeat anymore and collapses on the floor.")
        print()
        print("Game Over!")
