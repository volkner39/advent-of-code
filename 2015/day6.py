import sys

file = sys.argv[1]

f = open(file, "r")
list1 = f.read().splitlines()

grid = [[0]*1000 for i in range(1000)]
'''
for x in list1:
	s = x.split()
	
	switch = ''
	action = s[0]
	if len(s) == 5:
		switch = s[1]
		x1 = int(s[2].split(',')[0])
		y1 = int(s[2].split(',')[1])
		x2 = int(s[4].split(',')[0])
		y2 = int(s[4].split(',')[1])
	else:
		x1 = int(s[1].split(',')[0])
		y1 = int(s[1].split(',')[1])
		x2 = int(s[3].split(',')[0])
		y2 = int(s[3].split(',')[1])
	
	#print(x1,y1,x2,y2)
	#print(action, switch)
	
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):

			if (action == "turn" and switch == "on"):
				if (grid[x][y] == 0):
					grid[x][y] = 1
					
			elif (action == "turn" and switch == "off"):
				if (grid[x][y] == 1):
					grid[x][y] = 0
					
			elif (action == "toggle"):
				if (grid[x][y] == 0):
					grid[x][y] = 1
					
				elif (grid[x][y] == 1):
					grid[x][y] = 0

#combine = [j for i in grid for j in i]
#print(len(combine))

count = 0
for x in grid:
	for y in x:
		if y == 1:
			count+=1
print(count)

'''
# Part 2
for x in list1:
	s = x.split()
	
	switch = ''
	action = s[0]
	if len(s) == 5:
		switch = s[1]
		x1 = int(s[2].split(',')[0])
		y1 = int(s[2].split(',')[1])
		x2 = int(s[4].split(',')[0])
		y2 = int(s[4].split(',')[1])
	else:
		x1 = int(s[1].split(',')[0])
		y1 = int(s[1].split(',')[1])
		x2 = int(s[3].split(',')[0])
		y2 = int(s[3].split(',')[1])
	
	#print(x1,y1,x2,y2)
	#print(action, switch)
	
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):

			if (action == "turn" and switch == "on"):
				grid[x][y] += 1
					
			elif (action == "turn" and switch == "off"):
				if (grid[x][y] != 0):
					grid[x][y] -= 1
					
			elif (action == "toggle"):
				grid[x][y] += 2


#combine = [j for i in grid for j in i]
#print(len(combine))

count = 0
for x in grid:
	for y in x:
		count+=y
print(count)