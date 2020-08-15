#!/usr/bin/python3
import time

start_time = time.time()

coins=[200, 100, 50, 20, 10, 5, 2, 1]
count = 0

def calc(n: int, allowed_coins: list):
    global count
    if len(allowed_coins) == 1: 
        count += 1
    else:
        for i in range(len(allowed_coins)):
            a = n//allowed_coins[i]
            if n%allowed_coins[i] == 0:
                count += 1
                a -= 1
            for j in range(a, 0, -1):
                temp = n - allowed_coins[i]*j
                calc(temp, allowed_coins[i+1:])

calc(200,coins)

print(count) 

print ("\nThis application used {} seconds to run".format(time.time() - start_time))
