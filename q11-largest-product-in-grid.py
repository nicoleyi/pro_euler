#!/usr/bin/python3
import time
import sys

start_time = time.time()
pa_file = sys.argv[1]

fo = open(pa_file)
grid = [ ]

[grid.append(list(map(int,fo.readline().strip().split(' ')))) for _ in range (20)]

fo.close()

# main logic
def product(myList):
    # Multiply elements one by one
    result = 1
    for i in range (len(myList)):
         result = result*myList[i]
    return result
temp = product(grid[0][0:4])
#print (temp)
#print (grid[0][0:4])
max_round, product_row, product_col, product_right, product_left = 0,0,0,0,0
max_ = 0
for i in range (20):
  print ("Now i is ", i)
  for j in range (20):
    print ("Now j is ", j)
    if j+3 < 20: 
      product_row = product(grid[i][j:j+4])
    if i+3 < 20:
      product_col = product([grid[i][j],
			     grid[i+1][j],
			     grid[i+2][j],
			     grid[i+3][j]])
    if i+3 < 20 and j+3 < 20:
      product_right = product([grid[i][j],
			       grid[i+1][j+1],
			       grid[i+2][j+2],
			       grid[i+3][j+3]])
    if i-3 >= 0 and j-3 >= 0:
      product_left = product([grid[i][j],
			      grid[i-1][j-1],
			      grid[i-2][j-2],
			      grid[i-3][j-3]])

    max_round = max(product_row, product_col,
		    product_right,product_left,
		    max_round)
    print ("Round max is {}".format(max_round))
  max_ = max(max_,max_round)



print ("Final max is {}".format(max_))

print ("\nThis application used {} seconds to run".format(time.time() - start_time))