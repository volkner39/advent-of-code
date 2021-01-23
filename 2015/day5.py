import sys

file = sys.argv[1]

f = open(file, "r")
list1 = f.read().splitlines()

# Part 1
cond1 = False
cond2 = False
cond3 = True
prev_char = ''
vowel = 0
sol1 = 0

for x in list1:
	for y in x:
	
		if (prev_char + y) in ['ab', 'cd', 'pq', 'xy']:
			cond3 = False
	
		if (prev_char == y):
			cond1 = True
			
		if y in 'aeiou':
			vowel += 1
			
		if (vowel == 3):
			cond2 = True

		prev_char = y
			
	if (cond1 and cond2 and cond3):
		sol1 += 1

	cond1 = False
	cond2 = False
	cond3 = True
	prev_char = ''
	vowel = 0

print(sol1)


# Part 2
cond1 = False
cond2 = False
prev_char = ''
sol2 = 0
for x in range(len(list1)):
	for y in range(len(list1[x])):
	
		if (prev_char != '' and (prev_char + list1[x][y]) in list1[x][y+1:]):
			cond1 = True
	
		if (y+1 < len(list1[x]) and prev_char != list1[x][y]):
			if (list1[x][y+1] == prev_char):
				cond2 = True

		prev_char = list1[x][y]
			
	if (cond1 and cond2):
		sol2 += 1

	cond1 = False
	cond2 = False

	prev_char = ''

print(sol2)