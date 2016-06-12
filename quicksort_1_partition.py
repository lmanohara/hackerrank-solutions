#!/bin/python
def partition(ar):
    p = ar[0];
    lList = [];
    rList = [];
    x = 0;
    size = len(ar) - 1;
    while x <= size:
        if ar[x] < p:
            lList.append(ar[x]);
        else:
            rList.append(ar[x]);
        x += 1;
            
    pList = lList + rList;
    print ' '.join(map(str, pList))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
