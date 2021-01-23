import sys

file = sys.argv[1]

f = open(file, "r")
list1 = f.read().splitlines()
total = []
places = set()


for x in list1:
	x.replace(" ", "")
	split = x.split('=')

	a = split[0].split(' to ')[0].strip()
	b = split[0].split(' to ')[1].strip()
	c = b + " to " + a
	
	places.add(a)
	places.add(b)
	
	total.append((b, a, split[1].strip()))
	total.append((a, b, split[1].strip()))

print(total)

print(places)


