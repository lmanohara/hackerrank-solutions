import re
T = int(raw_input());
pattern  = "\.*[A-Z]{5}\d{4}\.*[A-Z]{1}";

for x in xrange(T):
    number = raw_input();
    match = re.match(pattern, number);
    
    if match == None:
        print "NO";
    else:
        print "YES";
