from random import randint
 
print("==============================================")
print("Let's play Janken!")
print("==============================================\n\n")

startGame = input("Shall we start?(y/n)\n")
username = input("Enter Your Username: ")

while startGame == "y":
	
    #list of play options
    playList = ["Rock", "Paper", "Scissors"]
     
    #random play to the computer
    computer = playList[randint(0,2)]
     
    #loop starts: player set to False

    game = int(input("How many game would you play?: "))

    count = 0

    win_score = 0
    tie_score = 0
    lose_score = 0
     
    while (count < game):

        computer = playList[randint(0,2)]

        count += 1

        player = input("\nRock, Paper, Scissors?\n")
        if player == computer:
            print("Tie! \n")
            tie_score += 1
        elif player == "Rock":
            if computer == "Paper":
                print(username + " lose!", computer, "covers", player, "\n")
                lose_score += 1
            else:
                print(username + " win!", player, "smashes", computer, "\n")
                win_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print(username + " lose!", computer, "cut", player, "\n")
                lose_score += 1
            else:
                print(username + " win!", player, "covers", computer,"\n")
                win_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print(username + " lose...", computer, "smashes", player,"\n")
                lose_score += 1
            else:
                print(username + " win!", player, "cut", computer, "\n")
                win_score += 1
        else:
            print("That's not a valid play. Check your spelling!\n")
        
        print("\nYour Score: ", win_score ," win(s) " , tie_score ," tie(s) " , lose_score ," lose(s)\n")


if startGame == "n":
    print("Come again later")