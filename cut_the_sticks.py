def stickCut(A):
    
    
    if len(A) == 0:
        return;
    else:
        print len(A);
        minLenStick = min(A);
        size = len(A) - 1;
        B = [];
        x = 0;
        
        while x <= size:
            # print A[x];
            # print x
            remaning = A[x] - minLenStick ;
            # print remaning;
            if remaning != 0:
                B.append(A[x]);
                
            x+= 1;
        
            
        return stickCut(B);
        
    

N = int(raw_input());

A = [int(x) for x in raw_input().split(' ')];

stickCut(A);
