T = int(raw_input());

for x in xrange(T):
    minAmount  = 0;
    amounts = [];
    bCount, wCount = [int(x) for x in raw_input().split(' ')];
    xUnits, yUnits, zUnits = [int(y) for y in raw_input().split(' ')];
    
    amounts.append((bCount * xUnits) + (wCount * yUnits));
    amounts.append((bCount + wCount) * xUnits + (wCount * zUnits));
    amounts.append((bCount + wCount) * yUnits + (bCount * zUnits));
    
    minAmount = min(amounts);
    
    print(minAmount);
