n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()

min_diff = 999999999;
for x in range(0,n-k):
    temp = candies[x+k-1] - candies[x]
    if(temp < min_diff):
        min_diff = temp

print min_diff
