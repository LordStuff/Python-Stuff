import random

fib_counter = 1
bid = 1

# fibonacci function
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
		
#fibonacci strategy
def fibonacci(result):
	global fib_counter 
	if result == 1 and fib_counter > 3:
		fib_counter -= 3
		return fib(fib_counter)

	elif result == 0:
		fib_counter += 1
		return fib(fib_counter)
	else:
		return 1
		

#martingale strategy
def martingale(result):
	global bid
	if result == 1:
		return 1	
	else:
		return bid*2
		
		
# reverse-martingale strategy
def reverse_martingale(result):
	global bid
	if result == 1:
		return bid*2
	else:
		return 1

#calculate the profit	
def profit (result, bid):
	if result == 1:
		profit = bid*2
		
	else:
		profit = 0-bid
		
	return profit
	
# calculate win or lose
def win_or_lose():
	result = random.random()
	if result <= 0.4865:
		return 1
	else:
		return 0
		
# decide if all-in or normal bid
def all_in(bid, account):
	if account >= bid:
		return bid
	else:
		return account
	
		
# Start the game
def game(account, rounds_to_play, strategy):
	start_account = account
	current_round = 0
	bid = 1
	while rounds_to_play > 0 and account > 0 and account < start_account*2:
		result = win_or_lose()
		rounds_to_play -= 1
		current_round += 1
		earned_profit = profit(result, bid)
		account += profit(result, bid)
		print("Runde:",current_round,"Einsatz:",bid,"Gewinn:",earned_profit,"Stand:",account)
		bid = all_in(strategy(result), account)
		#bid = strategy(result)
		

# main-Method
def main():
	
	print("Es wird mit 100,00€ Einsatz über maximal 200 Runden gespielt.")
	print("1 - Martingale Strategie")
	print("2 - Reverse Martingale Strategie")
	print("3 - Fibonacci Strategie")
	strategy = int(input("Welche Strategie soll gespielt werden?: "))

	if strategy == 1:
		game(100,200, martingale)
	
	elif strategy == 2:
		game(100,200,reverse_martingale)
	
	elif strategy == 3:
		game(100,200, fibonacci)
	
	else:
		print("Ungültige Eingabe!")
		main()
		
# start main ()
main() 
