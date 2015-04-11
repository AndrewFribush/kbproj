#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
#and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
#is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, 
#determine the number of blue discs that the box would contain.

b = 15
n = 21
lim = 1000000000000

while n < lim do
	bt = 3 * b + 2 * n - 2
	nt = 4 * b + 3 * n - 3

	b = bt
	n = nt
	if n >= lim
		puts n 
	end
end
