import sys
import hashlib 


key = sys.argv[1]

i = 0
while(1):
	final_key = key + str(i)
	res = hashlib.md5(final_key.encode('utf-8')).hexdigest()
	if (res[:6] == "000000"):
		print(i)
		break
	else:
		print(res)
		i += 1