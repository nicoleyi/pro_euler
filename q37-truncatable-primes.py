#!/usr/bin/python3
import time

start_time = time.time()
f = open("primes.data","r")
primes = set(map(int,f.read().strip().split(",")))

results = set()

#check the first digit is within (2,3,5,7), 
# the middle part is (1,3,5,7,9), the last digit is in (3,7)
def precheck(n):
    array = [int(d) for d in str(n)]
    if array[0] not in (2,3,5,7):
        return False
    for i in range (2, len(array)-1):
        if array[i] not in (1,3,5,7,9):
            return False
    if array[len(array)-1] not in (3,7):
        return False
    return True

counter = 0

def check(n):
    array = [int(d) for d in str(n)]
    l = len(array)
    last = 0
    for i in range(l): 
        last = last*10
        current = array[i]+last
        last = current
        if current not in primes:
            return False

    i=l
    j=1
    new=array[i-1]
    while i>0:
        if new not in primes:
            return False
        i -= 1
        if i >0:
            new += array[i-1]*(10**j)
            j += 1

    return True

for p in primes:
    if precheck(p):
        if check(p):
            results.add(p)

# minus 10 to remove 3 and 7
print(sum(results)-10)


f.close()

print ("\nThis application used {} seconds to run".format(time.time() - start_time))
