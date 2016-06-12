def findLargestVehicle(input):
    
    values = input.split();
    laneLength = int(values[0]);
    testCase = int(values[1]);
    
    laneWidths = [0 for x in xrange(laneLength)];
    
    laneWidth = raw_input();
        
    laneWidths = laneWidth.split();

    for z in xrange(testCase):
        
        test = raw_input();
        testValues = test.split();
        
        i = int(testValues[0]);
        j = int(testValues[1]);
        
        minVal = laneWidths[i];
        
        for v in xrange(i,j+1):
            if(laneWidths[v] <= minVal):
                minVal = laneWidths[v];
                
        print(minVal);
    
    
    
    

input = raw_input();
findLargestVehicle(input);
