T = int(raw_input());

for x in xrange(T):
    
    totalRoutes = 1;
    towns = int(raw_input());
    routes = raw_input();
    for y in routes.split(' '):
        totalRoutes = int(y) * totalRoutes;
    
    print(totalRoutes % 1234567);
