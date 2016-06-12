#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
    maxXOR = 0;
    
    for x in xrange(l,r+1):
        for y in xrange(x,r+1):
            valXOR = x ^ y;
            if maxXOR < valXOR :
                maxXOR = valXOR;
      
    return maxXOR;  

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res
