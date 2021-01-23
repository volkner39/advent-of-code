import sys

file = sys.argv[1]

f = open(file, "r")

location1 = 0
location2 = 0
visited = set()

visited.add(location1)
for i,v in enumerate(f.read()):
	print(i, v)

	if (v == '>'):
		if (i % 2 == 0):
			visited.add(location1+1)
			location1 += 1
		else:
			visited.add(location2+1)
			location2 += 1
	
	elif (v == '<'):
		if (i % 2 == 0):
			visited.add(location1-1)
			location1 -= 1
		else:
			visited.add(location2-1)
			location2 -= 1
	
	elif (v == '^'):
		if (i % 2 == 0):
			visited.add(location1+1j)
			location1 += 1j
		else:
			visited.add(location2+1j)
			location2 += 1j			
	
	elif (v == 'v'):
		if (i % 2 == 0):
			visited.add(location1-1j)
			location1 -= 1j
		else:
			visited.add(location2-1j)
			location2 -= 1j

print("Visited locations: ", visited)
print("# of houses visited: ", len(visited))
print("Final location1: ", location1)
print("Final location2: ", location2)
