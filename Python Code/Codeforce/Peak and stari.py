for i in range(int(input())):
    a, b, c = input().split()
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print('PEAK')
    else:
        print("NONE")
    