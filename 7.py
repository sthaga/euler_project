def check(num, lst):
	for i in lst:
		if x%i == 0:
			return False

	return True

x = 3
lst = [2]

while len(lst) < 10001:
	if check(x, lst):
		lst.append(x) 	

	x += 2

print(lst[10000])