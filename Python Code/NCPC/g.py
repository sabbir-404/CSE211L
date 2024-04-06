def remove(lstA, lstB):
    count = 0
    for i, a_val in enumerate(lstA):
        b_val = lstB[i]
        if a_val != b_val:
            count += 1
    return count

test_case = int(input())
inputs = []

for _ in range(test_case):
    length = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    inputs.append((a, b))

for i, (a, b) in enumerate(inputs, start=1):
    print(f"Case {i}: {remove(a, b)}")