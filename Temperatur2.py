def celsius_fahrenheit(celsius):
	fahrenheit = celsius/(5/9)+32
	print("%3.2f °C sind %3.2f °F\n" % (celsius, fahrenheit))
	calculate()
	
def celsius_kelvin(celsius):
	kelvin = celsius-273.15
	print("%3.2f °C sind %3.2f °K\n" % (celsius, kelvin))
	calculate()
	
def fahrenheit_kelvin(fahrenheit):
	kelvin = (5/9)*(fahrenheit-32)+273.15
	print("%3.2f °F sind %3.2f °K\n" % (fahrenheit, kelvin))
	calculate()
	
def fahrenheit_celsius(fahrenheit):
	celsius = (fahrenheit-32)*(5/9)
	print("%3.2f °F sind %3.2f °C\n" % (fahrenheit, celsius))
	calculate()
	
def kelvin_fahrenheit(kelvin):
	fahrenheit = (kelvin-273.15)/(5/9)+32
	print("%3.2f °K sind %3.2f °F\n" % (kelvin, fahrenheit))
	calculate()
	
def kelvin_celsius(kelvin):
	celsius = kelvin-273.15
	print("%3.2f °K sind %3.2f °C\n" % (kelvin, celsius))
	calculate()

def calculate():
	print("(1) Umrechnung von Celsius nach Kelvin")
	print("(2) Umrechnung von Celsius nach Fahrenheit")
	print("(3) Umrechnung von Kelvin nach Celsius")
	print("(4) Umrechnung von Kelvin nach Fahrenheit")
	print("(5) Umrechnung von Fahrenheit nach Celsius")
	print("(6) Umrechnung von Fahrenheit nach Kelvin")
	print("(7) Beenden\n")
	choice = int(input("Umrechnungsart wählen: "))
	
	if choice==1:
		#C to K
		celsius = float(input("Bitte Temperatur in Celsius angeben: "))
		celsius_kelvin(celsius)
		
	elif choice==2:
		#C to F
		celsius = float(input("Bitte Temperatur in Celsius angeben: "))
		celsius_fahrenheit(celsius)
		
	elif choice==3:
		#K to C
		kelvin = float(input("Bitte Temperatur in Kelvin angeben: "))
		kelvin_celsius(kelvin)	
	
	elif choice==4:
		#K to F
		kelvin = float(input("Bitte Temperatur in Kelvin angeben: "))
		kelvin_fahrenheit(kelvin)
		
	elif choice==5:
		#F to C
		fahrenheit = float(input("Bitte Temperatur in Fahrenheit angeben: "))
		fahrenheit_celsius(fahrenheit)
		
	elif choice==6:
		#F to K
		fahrenheit = float(input("Bitte Temperatur in Fahrenheit angeben: "))
		fahrenheit_kelvin(fahrenheit)
		
	elif choice==7:
		#exit program
		exit()
		
	else:
		print("Bitte eine Zahl zwischen 1 und 7 eingeben")
		calculate()
		
calculate()
