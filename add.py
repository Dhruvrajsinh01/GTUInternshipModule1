def add(*args):
	sum = 0
	args = list(args)
	x = 10
	args.append(20)
	args[2] = 4
	for i in args:
		sum = sum+i
	return sum

print(add(1,2,3,4,5,6,7,8,9))