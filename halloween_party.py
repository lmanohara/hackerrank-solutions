def calculateMaxPieces(times):
    verticalCuts = (times / 2 )+ (times % 2);
    horizontalCuts = times / 2;
    result = verticalCuts * horizontalCuts;
    print(result);
    
T = int(raw_input());
for x in xrange(T):
    K = int(raw_input());
    calculateMaxPieces(K);
