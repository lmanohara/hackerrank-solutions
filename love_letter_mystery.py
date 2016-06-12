operations = 0

def splitEelemts(t):
    global operations
    words = [raw_input() for _ in range(0,t)]
    for word in words:
        operations = 0
        length = len(word);
        x = 0 
        while x <= length-x-1:
            compaireElement(word[x], word[length - x-1])
            x += 1
        print operations
        
def compaireElement(firstElement, lastElement):
    firstElementVal = ord(firstElement)
    lastElementVal = ord(lastElement)
    if( firstElementVal > lastElementVal):
        
        findSetps(firstElementVal, lastElementVal)
    elif(firstElementVal < lastElementVal):
        
        findSetps(lastElementVal, firstElementVal)
        
def findSetps(graterValue, lowerValue):
    global operations
    steps = graterValue - lowerValue
    operations += steps
    
    
t = input()
splitEelemts(t)
