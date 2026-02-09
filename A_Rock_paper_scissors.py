ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"

beats = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}

floyed, matroskin, sharic = input(), input(), input()

if floyed == matroskin and beats[sharic] == floyed:
    print("S")
    
elif floyed == sharic and beats[matroskin] == floyed:
    print("M")

elif matroskin == sharic and beats[floyed] == matroskin:
    print("F")
    
else:
    print("?")