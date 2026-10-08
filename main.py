player_name = input("name?")

print("Today we are conducting an experiment, where you are to answer questions, depending on your answer the outcome will be differnt.\n")
print("Question 1. \n")
print(f"{player_name} stands in a room, there are two ways leading out. One door on the right and one door on the left. \n")
print("Which side do you choose?\n")

answer = input("Left or Right?")

if answer == "left":
    print("Go to the left door and open it, as you grip the door handle you feel a cill going down your spine. \n") 
    print("It is cold but you keep walking. A voice in the speakers suddenly speaks, walk to the next room which is located around the corner. \n ")
    print(f"When {player_name} arrives at the room, {player_name} opens the door. \n")
    print("Then the voice speaks again, this time though it is slightly diffrent from before. \n")
    print("What is your name subject? \n")

    player = input("name?")
    
    print(f"Hello! {player}, Do you know why you are in this room.\n")
    
    know = input("Do you know why you are here, (Yes or No)?")

    if know == "Yes":
        print("Good!")
    elif know == "No": 
        print("You are here today to answer a few questions.")
    else:
        print("You are here to answer questions.")

    print("Here comes the question.")
    print("Which Item is worth the most (keys), in Attack On Titan Revolution, The Attack serum or Colossal serum?\n")
    
    answer = input("Attack or Colossal")

    if answer == "Attack serum":
        print("Wrong! For that reason it is now game over for you. And you will be remembered as a jerk for thinking Colossal is worth so liitle. \n")
        print(f"{player} is shot to death. GAME OVER! \n")
    elif answer == "Colossal serum":
        print("That is right! You will now proceed to the next question. \n")
        print("The next question will be harder than the last one, so don't be surprised if you get it wrong. \n")
        print("The next question will be done in the room next door, so go there now! \n")
        print(f" {player} is going to the room. \n")
        print("There the voice speaks again, now colder and more robotic than before. \n")
        print("What is your name? \n")
  

        player = input("name?")

   
        print(f"Welcome {player} \n")
        print("The next question is... \n")
        print("Who is stronger in Naruto Shippudden, Madara Uchiha or Sasuke Uchiha? ")

        answer = input()

        if answer == " Sasuke Uchiha":
            print("That is very wrong! \n")
            print("Madara outclassed Sasuke in every way, but sadly black zetsu killed him. \n")
            print("For answering wrong you are to die! \n")
            print(f" {player} is thrown into a tank full with acids and gets desolved. GAME OVER! \n")
        elif answer == "Madara Uchiha":
            print(f" {player} has gotten the right answer and gets to proceed to the next question. \n")
        else:
            print("Game over! not related to the topic, you are sent to shiganshina right as the the titans storm in. You are torn to shreds in seconds because yor fear is to great to even take a single step forward. After screaming endlessly you finally die. ")
            
            print("The next question will be the final one, there are two doors infront of you. Choose which you will go through. \n")
            print("Door A, or Door B. \n")
            
            answer = input("A or B")

            if answer == "Door A":
                print(f"{player} goes through door A, there is nothing but black space there. Then you hear an explosion and everything goes silent. \n")
                print(f"{player} has died and has failed the experiment. GAME OVER \n")
            elif answer == "Door B":
                print(f" {player} goes through door B, and suddenly everything is burning. You feel cold and fear takes hold of {player}. \n")
                print(f"After a few minutes {player} dies. GAME OVER! \n")
            else:
                print("You are killed through severall holes that appear in your body.")
            
                
elif answer == "Right": 
    print("Go to the right door and open it, \n ")

    player = input("What is your name? ")
    
    print(f"{player} has gone through the right door, {player} will now begin the experiment.\n ")
    print(f"{player} walks down a long corridor, there are old paintings of people on the walls. There in the end of the corridor there is a door slightly open, through it there is a shining light.\n")
    print(f"Attention {player} must go through the door otherwise you are awaiting a tragic fate.\n ") 
    print(f"{player} goes through the door.\n")
    print("Question 1.\n")
    print("Which mountain is higher?\n")
    print("A. Großglockner. B. Matterhorn C. Zugspitze.\n")

    answer = input("Großglockner, Matterhorn, Zugspitze? ")

    if answer == "Großglockner": 
        print("Wrong!\n")
        print("proceed to next question.\n")
        print(f"{player} is about to go to the next qustion, then {player} hears a noise comming from below. The floor is viberating, then it opens and {player} falls in.\n")
        print("Game over!\n")

    elif answer == "Matterhorn":
        print(f"{player} has chosen the correct answer and will now be alowed to go to the next question.\n")
        print("The next question will be the final one.\n")
        print("Final Question!\n")     
        print("The final question will be impossible!\n")
        print("Which is my favorite family in AOTR\n")
        print("Reiss, Helos, Fritz, Ackermann. or Yeager. Choose one only.\n")

        answer = input()

        if answer == "Reiss":
            print("wrong \n")
            print("close but no. \n")
            print("Game Over\n")
            print(f"{player} is put in jail!\n")

        elif answer == "Fritz":
            print("So close, but it's still wrong!\n")
            print("Game Over\n")
            print(f"{player} is put in jail!\n")

        elif answer == "Helos":
            print("You got it right!\n")
            print(f"{player} has won and will be given the title Champion!\n")
            print("player won! and can now return home to freedom\n")
        elif answer == "Ackermann":
            print("Extremly close but no!\n")
            print("Game Over!\n")
            print(f"{player} is put in jail!\n")

        elif answer == "Yeager":
            print("Wrong!\n")
            print("Game Over!\n")
            print(f"{player} is put in jail!\n")

        else:
            print(f"since {player} answered wrong, {player} is thrown into a lake with water but {player} doesn't float but instead sinks to the bottom and drowns.\n")
            print(f"Game over! {player} has died from lack of oxygen. \n")
    
    elif answer == "Zugspitze":
        print("Wrong!\n")
        print(f"{player} has gotten the most wrong answer but will be given a second chance.\n")
        print(f"If {player} answers next question right, then {player} gets a mystery price. \n")   
        print("Final Question!\n")
        print("What is more worth in aotr Gunbai or berserkers mane or devil wing?\n")

        answer = input("Which is worth more, (Gunbai, berserkers mane or devil wing): ")

        if answer.lower() == "gunbai":
            print("Almost\n")
            print("Game over!\n")
        elif answer.lower() == "berserkers mane":
            print("Almost!\n")
            print("Game Over!\n")
        elif answer.lower() == "devil wing":
            print("Wrong!\n")
            print("Game Over!\n")
            print(f"{player} is shot!\n")
    else: 
        print("player hasn't answered the questions and will therefore be terminated.\n")
        print(f"{player} suddenly doesn't feel his heartbeat anymore and collapses on the floor.\n")
        print("Game Over!\n")
else:
    print("Game Over! for no reason.")
