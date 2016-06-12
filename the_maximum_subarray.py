def maxSum(A):
    maxSoFar = 0;
    maxEndingHere = 0;
    for x in A:
        maxEndingHere = maxEndingHere + x;
        if maxEndingHere < 0:
            maxEndingHere = 0;
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere;
    if maxSoFar == 0:
        maxSoFar = max(A);
    return maxSoFar;
    
def maxSumNonContiguous(A):
    sum = 0;
    for x in A:
        if x > 0:
            sum += x;
    if sum == 0:
        sum = max(A);
    return sum;
    
T = int(raw_input());

for i in xrange(T):
    N = int(raw_input());
    A = [int(x) for x in raw_input().split(' ')];
    print maxSum(A),
    print maxSumNonContiguous(A);
