import os
import sys


file = sys.argv[1]

f = open(file, "r")

list1 = f.read().splitlines()

print(list1)
total = 0
ribbon = 0

for y in list1:

	indices = [i for i, x in enumerate(y) if x == "x"]


	f_x = indices[0]
	s_x = indices[1]
	
	l = int(y[0:f_x])
	w = int(y[f_x+1:s_x])
	h = int(y[s_x+1:])
	
	print([l] + [w] + [h])
	

	lw = l*w
	wh = w*h
	hl = h*l

	sort_list = [l] + [w] + [h]
	print(sort_list)
	small = sorted(sort_list)[0]
	second = sorted(sort_list)[1]
	
	ribbon += ((small + small + second + second) + (l*w*h))
	
	smallest = min(lw,wh,hl)

	total += 2*l*w + 2*w*h + 2*h*l + smallest

print(total)
print(ribbon)

		

