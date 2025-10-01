
"""
Project Euler Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

number = 600851475143
factor = 2
largest_prime_factor = 1

while factor * factor <= number:
    if number % factor == 0:
        number //= factor
        largest_prime_factor = factor
    else:
        factor += 1

# If remaining number is greater than 1, it is prime
if number > 1:
    largest_prime_factor = number

print(f"The largest prime factor is {largest_prime_factor}")
