
def erasSieve(upperLimit):
    sieveBound = (upperLimit - 1)/2
    upperSqrt = (math.sqrt(upperLimit) - 1)/2

 
    BitArray PrimeBits = new BitArray(sieveBound + 1, true);
 
    for (int i = 1; i <= upperSqrt; i++) {
        if (PrimeBits.Get(i)) {
            for (int j = i * 2 * (i + 1); j <= sieveBound; j += 2 * i + 1) {
                PrimeBits.Set(j, false);
            }
        }
    }
 
    List<int> numbers = new List<int>((int)(upperLimit / (Math.Log(upperLimit) - 1.08366)));
    numbers.Add(2);
 
    for (int i = 1; i <= sieveBound; i++) {
        if (PrimeBits.Get(i)) {
            numbers.Add(2 * i + 1);
        }
    }
 
    return numbers.ToArray();
}
