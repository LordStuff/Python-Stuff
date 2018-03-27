def temperatur ():
	print("(1) Umrechnung von Celsius nach Kelvin")
	print("(2) Umrechnung von Celsius nach Fahrenheit")
	print("(3) Umrechnung von Kelvin nach Celsius")
	print("(4) Umrechnung von Kelvin nach Fahrenheit")
	print("(5) Umrechnung von Fahrenheit nach Celsius")
	print("(6) Umrechnung von Fahrenheit nach Kelvin\n")
	choice = int(input("Umrechnungsart wählen: "))

	if choice==1:
		# C nach K
		celsius = float(input("Temperatur in Celsius eingeben: "))
		kelvin = celsius-273.15
		print("%3.2f °C sind %3.2f °K" % (celsius, kelvin))
	
	elif choice==2:
		#C nach F
		celsius = float(input("Temperatur in Celsius eingeben: "))
		fahrenheit = celsius/(5/9)+32
		print("%3.2f °C sind %3.2f °F" % (celsius, fahrenheit))
		
	elif choice==3:
		#K nach F
		kelvin = float(input("Temperatur in Kelvin eingeben: "))
		fahrenheit = (kelvin-273.15)/(5/9)+32
		print("%3.2f °K sind %3.2f °F" % (kelvin, fahrenheit))
		
	elif choice==4:
		#K nach C
		kelvin = float(input("Temperatur in Kelvin eingeben: "))
		celsius = kelvin-273.15
		print("%3.2f °K sind %3.2f °C" % (kelvin, celsius))
	
	elif choice==5:
		#F nach C
		fahrenheit = float(input("Temperatur in Fahrenheit eingeben: "))
		celsius = (fahrenheit-32)*(5/9)
		print("%3.2f °F sind %3.2f °C" % (fahrenheit, celsius))
		
	elif choice==6:
		#F nach K
		fahrenheit = float(input("Temperatur in Fahrenheit eingeben: "))
		kelvin = (5/9)*(fahrenheit-32)+273.15
		print("%3.2f °F sind %3.2f °K" % (fahrenheit, kelvin))
		
	else:
		print("Bitte einen Wert zwischen 1 und 6 eingeben\n ")
		temperatur()
		
temperatur()
