import random  

def start_message():  
    print("let's play rock-paper-scissors")

def get_player():  
    print("0: rock, 1: scissors, 2: paper")
    return int(input("your hand: "))

def get_computer():  
    return random.randint(0, 2)

def view_result(hand_diff):  
    if hand_diff == 0:
        print("draw")
    elif hand_diff == -1 or hand_diff == 2:
        print("you win")
    else:
        print("you lose")

start_message() 
player = get_player() 
computer = get_computer() 
print("my hand:", player) 
print("computer's hand:", computer) 
view_result(player - computer) 