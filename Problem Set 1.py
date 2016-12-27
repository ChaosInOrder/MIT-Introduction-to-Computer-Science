#Problem Set 1

import math
#Problem 1


def isPrime(n):
    if n<=1:
        return False
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def getPrime():
    count = 0
    res=currentNum = 1
    while count<1000:
        if isPrime(currentNum):
            count+=1
            res=currentNum
        currentNum += 1
    return res

print getPrime()

#problem 2
def primeSum(n):
    sum=0
    for i in xrange(n+1):
        if isPrime(i):
            sum+=i
    return sum

print primeSum(2)
