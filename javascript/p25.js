//Fn = [phi/sqrt(5)]
//phi**n/sqrt(5)=10**n

phi = 1.61803398875	

//i is the number of digits -1.
FibDigits = function(i){
	return Math.ceil((Math.log(10)*i+(Math.log(5)/2))/Math.log(phi))
}
