def factorial_recursive(n):
  if n==0 or n==1:
    return 1 
  else:
    return n* factorial_recursive(n-1)
number=5
result=factorial_recursive(number)
print(" factorial of {number} is :",{result})
    