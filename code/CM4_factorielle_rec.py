## Factorielle : n! = 1 * 2 * .... * (n-1) * n
##                  = (n-1)! * n
##  Convention 0! = 1    , 1! = 1

def factorielle(n):
  if n < 2:
    return 1
  return factorielle(n-1) * n 

print(factorielle(5))
