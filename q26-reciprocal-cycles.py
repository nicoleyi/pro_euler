#!/usr/bin/python

'''
This is in response to https://projecteuler.net/problem=26

Solution Approach: 

Let me illustrate with 1/7.  First calculation of the remainder of 1/7 gives us 1.

Second calculation to analyse the remainder on the first decimal place we multiply by 10,  and divide by 7. The remainder of 10/7 is 3.

In the third calculation we get 30/7 which gives us a remainder of 2.

In the fourth calculation we get 20/7 which gives us a remainder of 6.

In the fifth calculation we get 60/7 which gives us a remainder of 4.

In the sixth calculation we get 40/7 which gives us a remainder of 5.

In the seventh calculation we get 50/7 which gives us a remainder of 1.

We already have had a remainder of 1 on the first calculation which means that we continue the calculations we will see the same pattern emerge again, since 10/7 gives us 3 and so on.  Thus we have found the longest recurring cycle in 1/7. Or rather we have found the length of the recurring cycle in 1/7 which is 7-1 = 6 digits long.

This is a pretty simple solution approach, where all we need to do is to keep calculating the remainder and keep track of the already found remainders.

One more thing to note is that the maximum recurring cycle length of 1/d is d-1, as it is pretty obvious from the example. We can get d-1 different possible remainders from the number, since if the result is equal to or greater than d, then it is not a remainder.

'''

import time

start_time = time.time()

'''
n is the number needs to be checked
'''

def cycle(n):
  i = 0 # if there is any cycle, what it might be. 
  d = 1
  remainders = set()

  # ocycle upper bound is itself. 
  # break if there is a cycle or reach the upper bound 
  while i < n:
    d = d % n
    if d in remainders:
      break
    remainders.add(d)
    d = 10 * d
    i += 1

  # in this case, I just want to find out the max cycle, so I just return the length. If I want to know the remainder in order, set wouldn't be a good choice to store the data. 
  return i

upper = 1000
max_l = 0
num = 0
for d in range(3, upper+1):
  result = cycle(d)
  if max_l < result:
    max_l = result
    num = d

print ("Max reciprocal number found in {}, the length is {}".format(num, max_l))

print ("\nThis application used {} seconds to run".format(time.time() - start_time))
