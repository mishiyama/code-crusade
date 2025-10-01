"""
 
 Project Euler Problem 1: Multiples of 3 or 5
 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

 Find the sum of all the multiples of 3 or 5 below 1000.
"""

a=3 
b=5
sum=0
for i in range(1,1000):
 if (i % a == 0 or i % b ==0):
  sum+=i
print(f"The total sum of all multiples of 3 and 5 below 1000 is {sum}")
