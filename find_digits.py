T = int(raw_input());

for x in xrange(T):
    number = int(raw_input());
    firstVal = number;
    count = 0;
    while number:
        digit = number % 10;
        
        if digit != 0 and firstVal % digit == 0:
            count += 1;
        number /= 10;
    print count;
