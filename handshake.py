
T = raw_input();
testCase = int(T);

for x in xrange(testCase):
    
    N = int(raw_input());
    
    if N <= 1 :
        handshakes = 0;
    else:
        handshakes = N * (N - 1) / 2;
    
    print(handshakes);
