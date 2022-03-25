'''
Armstrong number - 
If the sum of cube of digits of a number is equal to the number itself, it is called an Armstrong number.
'''

def naive_approach(n):
  remainder=sum_val=0
  m = int(n)
  while n > 0:
    remainder = n%10
    sum_val += remainder**3
    n = n//10 
  if sum_val == m :
    print('An armstrong number')
  else:
    print('Not an armstrong number')


def with_lambda(n):
  digits = [int(x) for x in str(n)]
  sum_val = sum(map(lambda i : i ** 3, digits))
  if sum_val == n :
    print('An armstrong number')
  else:
    print('Not an armstrong number')
    

n = int(input('Enter number to check : '))
naive_approach(n)
with_lambda(n)
  