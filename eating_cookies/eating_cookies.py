#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=dict()):
  if n in cache:
    return cache[n]
  if n <= 0:
    return 1
  total = 0
  for i in range(1, 4):
    if i < n:
      total += eating_cookies(n - i)
    elif i == n:
      total += 1
  cache[n] = total
  return total
    

""" if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]') """

eating_cookies(50)