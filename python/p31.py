'''
P31 of Project Euler

It should be more efficient than a brute force solution. For example,
it has a much better ON (ON^2 vs ON^len(denom))

In human terms, it creates something like this, with the top row being each target number 
and the bottom combinations to reach that number.
 _ _ _ _
|0|1|2|3|
 _ _ _ _
|1|1|2|2|
 _ _ _ _
'''

# British Combinations, takes one variable, target
def BritishCombs(tar):

#The given denominations as an array
	denom = [1, 2, 5, 10, 20, 50, 100, 200]
#Creates an array of 0's tar+1 long
	ways = [0] * (tar + 1)
#There is always one way to give back change for nothing.
	ways[0] = 1

#For each type of coin, but not the specific value of that
	for i in range(len(denom)):
#simple declaration
		j = denom[i]
#While j is less than or equal to tar
		while j <= tar:
#Adds the number of ways a number can be formed at a previous point to the number of ways a larger combination can be formed
			ways[j] += ways[(j - denom[i])]
#simple increment
			j += 1
#return last element of ways list
	return ways[-1]

#Call the function to demonstrate
BritishCombs(200)
