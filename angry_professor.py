T = int(raw_input());

for x in xrange(T):
    
    studentCount = 0;
    students, expectedStudent = [int(x) for x in raw_input().split(' ')];
    times = [int(y) for y in raw_input().split(' ')];
    times.sort();
    
    for y in xrange(expectedStudent):
        time = times[y];
        if(time <= 0):
            studentCount += 1;
            
    if(studentCount == expectedStudent):
        print("NO");
    else:
        print("YES");
