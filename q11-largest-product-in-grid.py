#!/usr/bin/python3
import time
import sys

start_time = time.time()
pa_file = sys.argv[1]

fo = open(pa_file)
grid = [ ]

[grid.append(list(map(int,fo.readline().strip().split(' ')))) for _ in range (20)]

fo.close()

max_round, product_row, product_col, product_right, product_left = 0,0,0,0,0
max_ = 0

def product(myList):
    # Multiply elements one by one
    result = 1
    for i in range (len(myList)):
         result = result*myList[i]
    return result

# main logic
for i in range (20):
  for j in range (20):
    # Get horizonal
    if j+3 < 20: 
      product_row = product([grid[i][j],
			     grid[i][j+1],
			     grid[i][j+2],
			     grid[i][j+3]])
    # Get vertical 
    if i+3 < 20:
      product_col = product([grid[i][j],
			     grid[i+1][j],
			     grid[i+2][j],
    			     grid[i+3][j]])

    # Get diagonal left to right
    if i+3 < 20 and j+3 < 20:
      product_right = product([grid[i][j],
			       grid[i+1][j+1],
			       grid[i+2][j+2],
			       grid[i+3][j+3]])
    
    # Get diagonal right to left
    if i+3 < 20 and j-3 >= 0:
      product_left = product([grid[i][j],
			      grid[i+1][j-1],
			      grid[i+2][j-2],
			      grid[i+3][j-3]])

    max_round = max(product_row, product_col,
		    product_right,product_left,
		    max_round)
  max_ = max(max_,max_round)



print ("Final max is {}".format(max_))

print ("\nThis application used {} seconds to run".format(time.time() - start_time))
