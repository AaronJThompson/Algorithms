#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  actions = ["rock", "paper", "scissors"]

  def rps_recur(n):
    nonlocal actions
    set = list()
    if n == 0:
      set.append([])
    elif n <= 1:
      for a in actions:
        set.append([a])
    else:
      for a in actions:
        for perm in rps_recur(n - 1):
          perm.insert(0, a)
          set.append(perm)
    return set

  return rps_recur(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')