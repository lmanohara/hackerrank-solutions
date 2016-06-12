def calculateGemElements(rocks):
    rocksArry = [ [0 for x in xrange(27)] for x in xrange(101)]
    ans = 0;
    for x in xrange(rocks):
        rock = raw_input();
        length = len(rock);
        for y in xrange(length):
            place = ord(rock[y]) - 97;
            rocksArry[x][place] += 1;
        
     
    for z in xrange(26):
        flag = 0;
        for v in xrange(rocks):
            if(rocksArry[v][z] == 0):
                flag = 1;
        if(flag == 0):
            ans += 1;
    print(ans);

        
N = int(raw_input());
calculateGemElements(N);
