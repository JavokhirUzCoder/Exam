num = int(input())


def PrimeNumber(Number):
	if Number <= 1:
		return False

	for i in range(2, int(Number**0.5)+1):
		if Number % i == 0:
			return False

	return True


for i in range(num):
    if PrimeNumber(i):
        print(i, end = " ")