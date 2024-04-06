t = int(input())

for i in range(1, t + 1):
    n = int(input())
    pw = 5
    ans = 0
    while pw <= n:
        ans += n // pw
        pw *= 5
    print(ans)
    
