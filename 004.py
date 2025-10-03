
"""
Project Euler 4 :Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
""" 


def isPalindrome(product):
    return str(product) == str(product)[::-1]

max_palindrome = 0

for i in range(1, 1000):
    for j in range(i, 1000):
        product = i * j
        if isPalindrome(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
