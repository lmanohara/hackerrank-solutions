string = raw_input()
found = False
sum = 0

letters = [0 for x in range(0, 26)]

for letter in string:
    letters[ord(letter) - 97] += 1
    
for x in range(0, 26):
    sum = sum + (letters[x]%2)
    
    

if sum >= 2:
    print("NO")
else:
    print("YES")
