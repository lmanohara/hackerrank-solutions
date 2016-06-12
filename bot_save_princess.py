#!/bin/python
def displayPathtoPrincess(n,grid):
    myPos = (int(n/2), int(n/2));
    princessPos = (0,0);
    
    for i in xrange(0, n):
        pos = grid[i].find('p');
        if pos != -1:
            princessPos = (pos,i);
            
    steps = (princessPos[0] - myPos[0], princessPos[1] - myPos[1]);
    
    x = steps[0];
    y = steps[1];
    
    if y > 0:
        printMoves(abs( y ), "DOWN");
    elif y < 0:
        printMoves(abs( y ), "UP");
    
    if  x  > 0 :
        printMoves(abs( x ), "RIGHT");
    elif x < 0:
        printMoves(abs( x ), "LEFT");

            
#print all the moves here
def printMoves(count, movement):
    for i in xrange(count):
        print movement;

m = int(raw_input());

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
