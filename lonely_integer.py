def loneInt(A):
    currentNum = A[0];
    size = len(A) - 1;
    x = 1;
     
    while x <= size:
        
        if currentNum == A[x]:
            del A[x];
            del A[0];
            return loneInt(A);
            
        x+= 1;
        
    return currentNum;

N = int(raw_input());

A = [int(x) for x in raw_input().split(' ')];

print loneInt(A);

