import sqlite3
import time
import os

connection = sqlite3.connect("stock.db")

cursor = connection.cursor()

#delete
#cursor.execute("""DROP TABLE employee;""")

#sql_command = """
#CREATE TABLE goods ( 
#staff_number INTEGER PRIMARY KEY, 
#sort VARCHAR(30), 
#countrycode VARCHAR(30), 
#lotnumber VARCHAR(30),
#stock VARCHAR(30),
#amount INTEGER);"""

#cursor.execute(sql_command)

# delete one position in database
def delete_entry(lotnumber):
	sql_command ="DELETE FROM goods WHERE lotnumber = "+ lotnumber + ";"
	print(sql_command)
	cursor.execute(sql_command)
	print("Eintrag gelöscht.")
	time.sleep(1)
	os.system("cls")

# add a new position to the database
def insert_entry(sort, countrycode, lotnumber, stock, amount):
	sql_command = "INSERT INTO goods (staff_number, sort, countrycode, lotnumber, stock, amount) VALUES (NULL, '" + sort + "','" + countrycode + "','" + lotnumber + "','" + stock + "'," + str(amount) +" );"
	cursor.execute(sql_command)
	print("Wareneingang eingetragen.")
	time.sleep(1)
	os.system("cls")

# show all positons at the database
# selection to choose the stock where the goods in stock would be displayed.
def show_entries():
	
	print("Welcher Lagerbestand soll abgefragt werden?\n")
	print("1 - Lagerbestand allgemein")
	print("2 - Lagerbestand Nordlicht")
	print("3 - Lagerbestand LGR")
	print("4 - Lagerbestand Hanseservice")
	x = int(input("\nEingabe: "))
	
	if x == 1:
		cursor.execute("SELECT * FROM goods")
		
	elif x == 2:
		cursor.execute("SELECT * FROM goods WHERE stock = 'Nordlicht'")
		
	elif x == 3:
		cursor.execute("SELECT * FROM goods WHERE stock = 'LGR'")
		
	elif x == 4:
		cursor.execute("SELECT * FROM goods WHERE stock = 'Hanseservice'")
		
	else:
		print("Falsche Eingabe")
		
	print("Lagerbestand:\n")
	result = cursor.fetchall()
	for r in result:
		print(r)
	back = input("\nZum Verlassen eine Enter drücken.")
	os.system("cls")
		
# reduce the amount of a position at the database
def lower_amount(lotnumber, amount):
	cursor.execute("SELECT amount FROM goods WHERE lotnumber = " + lotnumber)
	result = cursor.fetchone()
	amount = int(amount)
	in_stock = result[0]
	if in_stock < amount:
		print("Warenausgang nicht möglich, der Warenbestand ist: " + str(in_stock))
		time.sleep(1)
		os.system("cls")
	
	else:
		result = result[0] - int(amount)
		cursor.execute("UPDATE goods SET amount = " + str(result) + " WHERE lotnumber = " + lotnumber)
		print("Neuer Warenbestand:",result)
		time.sleep(1)
		os.system("cls")

variable = 0

#main programm with a selection what to do.
while variable != 5:
	
	print("Willkommen im Lagersystem es ist der:",time.strftime("%d.%m.%Y"))
	print("Was möchten Sie tun?\n")
	print("1 - Lagerbestand abfragen")
	print("2 - Wareneingang eintragen")
	print("3 - Warenausgang eintragen")
	print("4 - Artikel löschen")
	print("5 - Beenden")
	variable = int(input("\nEingabe: "))
	
	if variable == 1:
		os.system("cls")
		show_entries()
	
	elif variable == 2:
		sort = input("Bitte Art der Ware eingeben: ")
		countrycode = input("Bitte Länderkennung eingeben: ")
		lotnumber = input("Bitte Lotnummer eingeben: ")
		stock = input("Bitte Lagerot eingeben: ")
		amount = input("Bitte Menge eingeben: ")
	
		insert_entry(sort,countrycode,lotnumber,stock,amount)

	elif variable == 3:
		lotnumber = input("Bitte Lotnummer des Warenausgangs eingeben: ")
		amount = input("Bitte Menge der ausgehenden Ware eingeben: ")
		lower_amount(lotnumber, amount)
	
	elif variable == 4:
		lotnumber = input("Bitte Lotnummer des zu löschenden Artikels eingeben: ")
		delete_entry(lotnumber)
		
	elif variable == 5:
		print("Beenden")
		
	elif variable == 42:
		sql_statement = input("SQL-Statement eingeben: ")
		try:
			cursor.execute(sql_statement)
		except:
			print("Ungültiges SQL-Statement")
			print("Eingabe wird abgebrochen\n")
		
	else:
		print ("Ungültige Eingabe.")
	

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
