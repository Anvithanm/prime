def prime():
	for n in range(2,30):
		for i in range(2,n):
			if (n%i==0):
				break
		else:
			print n
prime()
