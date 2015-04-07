//2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

function smallestMultiple(lim){
	while(t != true){
		for(i = 0; i > lim; i++){
			if (num % lim != 0){
				return false;
	 		}
	 		else{
	 			return true;
	 		}
		}
	}
}
smallestMultiple(20);