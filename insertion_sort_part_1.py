#!/bin/python
def insertionSort(ar,m):
    v = ar[-1];
    
    x = len(ar) - 1;
    while (ar[x] >= v and x >= 0):
        
        if x == 0:
            ar[x] = v;
        elif ar[x - 1] > v:
            ar[x] = ar[x-1];
        elif ar[x - 1] < v:
            ar[x] = v;
        x-=1;
        
        print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar,m)
