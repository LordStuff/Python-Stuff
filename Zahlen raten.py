list = range(1,101)

print("Denke an eine Zahl zwischen 1 und 100\n")

while len(list) > 1:
	print("Ist die Zahl kleiner als",list[int(len(list)/2)],"?")
	answer = input()
	answer.lower()
	
	left = list[:int(len(list)/2)]
	right = list[int(len(list)/2):]
	
	if answer == "ja":
		list = left
		
	else:
		list = right
		
print("Deine Zahl lautet:",list[0])
