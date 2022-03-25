'''
TASK - To get an input n, where n is an integer
'''

# Imports required
import math

def check_with_root(n):
  if n>0:
    sqrt = math.sqrt(n)
    if math.ceil(sqrt) == math.floor(sqrt):
      print(True)
    else:
      print(False)
  else:
    print(None)

def check_without_root(n):
  if n <= 0 :
    print(None)
  elif n == 1:
    print(True)
  else:
    for i in range(n//2,0, -1):
      if n/i == i:
        print(True)
        break
      elif n/i < i:
        continue
      else:
        print(False)
        break
    
n = int(input("Enter number:"))
print('By taking the square root : ', end= "")
check_with_root(n)
print('Without taking the square root : ', end= "")
check_without_root(n)