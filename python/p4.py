#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Not a great ON, but necessarily hits the answer relatively early.
def Palindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False

def numLen(num):
	return len(str(num))

def largestPalindrome():
	for Outnum in range(100, 1000)[::-1]:
		for Innum in range(100, 1000)[::-1]:
			num = Outnum * Innum
			if Palindrome(num):
				return num
				break

print(largestPalindrome())
