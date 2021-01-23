import sys

file = sys.argv[1]

f = open(file, "r")
list1 = f.read().splitlines()
acc = 0
acc1 = 0
counter = 0

hex = "abcdef0123456789"

# loop through each string in list
for x in list1:

	# get total string length
	acc += len(x)

	# remove outside double quotes
	strip = x[1:-1]
	
	# loop through each character in string
	for y in range(0, len(strip)):

		# skip characters if we accounted for them
		if (counter != 0):
			counter -= 1
			continue

		# if we see a "\\"
		elif strip[y] == '\\' and strip[y+1] == '\\':
			acc1 += 1
			counter = 1

		# if we see a "\*"
		elif strip[y] == '\\' and strip[y+1] == '\"':
			acc1 += 1
			counter = 1

		# if we see something like "\xff"
		elif strip[y] == '\\' and len(strip[y:]) >= 4:
			if (strip[y] == '\\') and (strip[y+1] == 'x') and (strip[y+2] in hex) and (strip[y+3] in hex):
				acc1 += 1
				counter = 3
			else:
				acc1 += 1

		# otherwise it's a normal character
		else:
			acc1 += 1

print("Part1: ", acc - acc1)


# part 2
new = 0

for x in list1:
	new += len(x)
	new += 4

	# remove outside double quotes
	strip = x[1:-1]
	
	# loop through string
	for y in range(0, len(strip)):
	
		# add 1 if we see a '\'
		if strip[y] == '\\':
			new += 1
		
		# add 1 if we see a '"'
		elif strip[y] == '"':
			new += 1

print("Part2: ", new - acc)
		
		