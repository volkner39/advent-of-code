import sys

file = sys.argv[1]

f = open(file, "r")

acc = 0
flag = 0

for i,v in enumerate(f.read()):
	
	if(v == '('):
		acc += 1
	
	if (v == ')'):
		acc -= 1
		
	if (flag == 0 and acc == -1):
		flag = 1
		print("First pos: ", i)

		
print("Final Floor: ", acc)
f.close()