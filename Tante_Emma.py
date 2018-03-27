starting_capital = [int(input("Bitte Startkapital für Tante-Emma-Laden eingeben: ")) for i in range(5)]
end_capital = [int(input("Bitte Endkapital für Tante-Emma-Laden eingeben: ")) for i in range(5)]

store1 = ["Tante-Emma-Laden 1", starting_capital[0],end_capital[0],end_capital[0]-starting_capital[0]]
store2 = ["Tante-Emma-Laden 2", starting_capital[1],end_capital[1],end_capital[1]-starting_capital[1]]
store3 = ["Tante-Emma-Laden 3", starting_capital[2],end_capital[2],end_capital[2]-starting_capital[2]]
store4 = ["Tante-Emma-Laden 4", starting_capital[3],end_capital[3],end_capital[3]-starting_capital[3]]
store5 = ["Tante-Emma-Laden 5", starting_capital[4],end_capital[4],end_capital[4]-starting_capital[4]]

stores = [store1, store2, store3, store4, store5]

maximum_turnover = 0
minimum_turnover = 100000

for store in stores:
	if store[3] > maximum_turnover:
		maximum_turnover = store[3]
		maximum_turnover_store = store[0]
		
	if store[3] < minimum_turnover:
		minimum_turnover = store[3]
		minimum_turnover_store = store[0]
		
print("Der Tante-Emma-Laden mit dem meisten Umsatz ist:", maximum_turnover_store, "Umsatz:",maximum_turnover)
print("Der Tante-Emma-Laden mit dem geringsten Umsatz ist:", minimum_turnover_store, "Umsatz:",minimum_turnover)
		
