import sys

file = sys.argv[1]

f = open(file, "r")
list1 = f.read().splitlines()

temp = {x.split()[-1]: x for x in list1}

vals = {}

print(temp)

def rec(target):
	if target in vals:
		return vals[target]
	
	line = temp[target]
	
	parts = line.split()
	
	if parts[1] == '->':
		if (parts[0].isdigit()):
			final = int(parts[0])
		else:
			final = rec(parts[0])

	elif parts[0] == "NOT":
		final = ~rec(parts[1])
	
	elif parts[1] == "AND":
		if (parts[0].isdigit()):
			final = int(parts[0]) & rec(parts[2])
		else:
			final = rec(parts[0]) & rec(parts[2])
	
	elif parts[1] == "OR":
		final = rec(parts[0]) | rec(parts[2])
	
	elif parts[1] == "RSHIFT":
		final = rec(parts[0]) >> int(parts[2])
	
	elif parts[1] == "LSHIFT":
		final = rec(parts[0]) << int(parts[2])

	vals[target] = final
	return final




target = 'a'
value = rec(target)

print(value)

