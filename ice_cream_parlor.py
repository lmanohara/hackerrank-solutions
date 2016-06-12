T = int(raw_input());

for z in xrange(T):
    M = int(raw_input());
    N = int(raw_input());
    flavorPrices = [int(x) for x in raw_input().split(' ')];
    
    for x in xrange(N):
        current = flavorPrices[x];
        j = x + 1;
        
        while j < N:
            if (current + flavorPrices[j]) == M:
                print x + 1, j + 1;
            j += 1;
            
        j = 0;
