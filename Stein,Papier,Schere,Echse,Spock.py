import random

shapes = ["Rock","Paper","Scissors","Lizard","Spock"]

list_of_answers = {("Scissors","Paper"):"Scissors cuts Paper",
("Siccors","Lizard"):"Scissors decapitates Lizard",("Rock","Scissors"):"Rock crushes Scissors",
("Rock","Lizard"):"Rock crushes Lizard",("Paper","Stone"):"Paper covers Stone",
("Paper","Spock"):"Paper disproves Spock", ("Lizard","Spock"):"Lizard poisons Spock",
("Lizard","Paper"):"Lizard eats Paper",("Spock","Stone"):"Spock vaporizes Stone",
("Spock","Scissors"):"Spock smashes Scissors",
("Paper","Scissors"):"Scissors cuts Paper",
("Lizard","Scissors"):"Scissors decapitates Lizard",("Scissors","Rock"):"Rock crushes Scissors",
("Lizard","Rock"):"Rock crushes Lizard",("Stone","Paper"):"Paper covers Stone",
("Spock","Paper"):"Paper disproves Spock", ("Spock","Lizard"):"Lizard poisons Spock",
("Paper","Lizard"):"Lizard eats Paper",("Stone","Spock"):"Spock vaporizes Stone",
("Scissors","Spock"):"Spock smashes Scissors"}

list_of_combinations = {("Scissors","Paper"):"Scissors",
("Siccors","Lizard"):"Scissors",("Rock","Scissors"):"Rock",
("Rock","Lizard"):"Rock",("Paper","Stone"):"Paper",
("Paper","Spock"):"Paper", ("Lizard","Spock"):"Lizard",
("Lizard","Paper"):"Lizard",("Spock","Stone"):"Spock",
("Spock","Scissors"):"Spock",
("Paper","Scissors"):"Scissors",
("Lizard","Scssors"):"Scissors",("Scissors","Rock"):"Rock",
("Lizard","Rock"):"Rock",("Stone","Paper"):"Paper",
("Spock","Paper"):"Paper", ("Spock","Lizard"):"Lizard",
("Paper","Lizard"):"Lizard",("Stone","Spock"):"Spock",
("Scissors","Spock"):"Spock"}

print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")
print("4 - Lizard")
print("5 - Spock")
players_choice = int(input("Was wählst du?:"))

players_shape = shapes[players_choice-1]
computers_shape = shapes[random.randint(0,4)]

print("\nPlayer chooses:",players_shape)
print("Computer chooses:",computers_shape,"\n")


if players_shape == computers_shape:
	print("\nDraw")
else:
	print(list_of_answers[players_shape,computers_shape])
	if list_of_combinations[players_shape,computers_shape] == players_shape:
		print("\nPlayer wins")
	else:
		print("\nComputer wins")

