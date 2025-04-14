import random  

print("0: rock, 1: scissors, 2: paper")  
player = int(input("your hand: "))  
computer = random.randint(0, 2) 

print("my hand: ", player)  
print("computer's hand: ", computer) 

if player == computer: 
    print("draw")
elif (player == 0 and computer == 1) or \
     (player == 1 and computer == 2) or \
     (player == 2 and computer == 0): 
    print("you win")
else:
    print("you lose") 