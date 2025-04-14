import random

def start_message():
    print("let's play rock-paper-scissors")

def get_player(hands):
    print("0:", hands[0], "1:", hands[1], "2:", hands[2])
    return int(input("your hand: "))

def get_computer():
    return random.randint(0, 2)

def get_hand_name(hand_number, hands):
    return hands[hand_number]

def view_hand(player, computer, hands):
    print("my hand is", get_hand_name(player, hands))
    print("computer's hand is", get_hand_name(computer, hands))

def get_result(hand_diff):
    if hand_diff == 0:
        return "draw"
    elif hand_diff == -1 or hand_diff == 2:
        return "win"
    else:
        return "lose"

def view_result(result, results_dict):
    print(results_dict[result])

hands = ["rock", "scissors", "paper"]
results = {"win": "you win", "lose": "you lose", "draw": "draw try again"}
start_message()
player = get_player(hands)
computer = get_computer()
view_hand(player, computer, hands)
result = get_result(player - computer)
view_result(result, results)