#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def Palindrome(num):
	if num == num[::-1]:
		return true
	else:
		return false

def name():
	for i in