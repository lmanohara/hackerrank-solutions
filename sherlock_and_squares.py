import math

def squareCount(a,b):
    x = 1;
    currentSquare = 1;
    count = 0;
    while currentSquare < b:
        currentSquare = pow(x,2);
        if currentSquare >= a and currentSquare <= b:
            count += 1;
        x += 1;
    return count;
    
    
T = int(raw_input());
for x in xrange(T):
    a,b = [int(x) for x in raw_input().split(' ')];
    print squareCount(a,b);
