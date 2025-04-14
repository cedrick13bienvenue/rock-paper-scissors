import random  

def start_message():
    print("let's play rock-paper-scissors")

def get_player(): 
    hands = ["rock", "scissors", "paper"] 
    print("0: rock, 1: scissors, 2: paper")
    return int(input("your hand: "))

def get_computer(): 
    return random.randint(0, 2)

def get_hand_name(hand_number): 
    hands = ["rock", "scissors", "paper"]
    return hands[hand_number]

def view_hand(player, computer):
    print("my hand is", get_hand_name(player))
    print("computer's hand is", get_hand_name(computer))

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
view_hand(player, computer)  
view_result(player - computer)  