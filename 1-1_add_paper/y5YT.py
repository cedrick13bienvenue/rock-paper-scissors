import random  

print("0: rock, 1: scissors, 2: paper") 
player = int(input("your hand: "))  

computer = random.randint(0, 2)  

print("my hand: ", player)
print("computer's hand: ", computer)