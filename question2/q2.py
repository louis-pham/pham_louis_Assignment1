import random

def factorial(x):
	product = 1;
	while x > 0:
		product *= x;
		x -= 1
	return product	

def binomialCoefficient(n, k): #2a
	if k != 0:
		return factorial(n) / (factorial(k) * factorial(n - k))
	else:
		return 1

def pascalsTriangle(r): #2b
	#each row has row+1 elements
	for row in range(0, r+1):
		rowStr = ""
		for ele in range(0,row+1):
			rowStr += str(binomialCoefficient(row, ele)) + " "
		print rowStr

def probFunc(p,n,k): #2c
	return float(binomialCoefficient(n,k)) * p**k * (1.0-p)**(n-k)

def probAtLeast(p,n,k):
	sum = 0
	for _k in range(0, k):
		sum += probFunc(p,n,_k)
	return 1-sum

if __name__ == "__main__":
	#print binomialCoefficient(5,5)
	#print pascalsTriangle(20)
	#print probFunc(0.250, 4, 1)

	#2d
	N = [10, 100, 1000, 5000, 7500, 10000, 20000, 30000, 50000, 75000, 100000, 150000]
	p = 0.25
	nCoinFlips = 25
	kHeads = 7
	print "Probability of at least", kHeads, "heads:", probAtLeast(p,nCoinFlips,kHeads)
	for run in N:
		print "---------------Number of runs:", run
		_run = run
		successes = 0
		fails = 0
		exact = 0
		while run > 0:
			#print "-------------Run No.", str(_run - run + 1) + "-------------"
			_n = nCoinFlips
			heads = 0
			tails = 0
			while _n > 0:
				if random.random() <= p:
					heads += 1
				else:
					tails += 1
				_n -= 1
			#print "Heads:", heads, "out of", nCoinFlips
			#print "Tails:", tails, "out of", nCoinFlips
			if heads == kHeads:
				exact += 1
			if heads >= kHeads:
				successes += 1
			else:
				fails += 1
			run -= 1
		print "Successes:", successes
		print "Fails:", fails
		print "Ratio:", float(successes)/(successes+fails)

