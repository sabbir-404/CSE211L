def upscale(n):
    type_1 = '##..'
    type_2 = '..##'

    res = []

    if n == 1:
        print("##")
        print("##")
    else:
        hash_count = 1
        for i in range(n * 2, 2):
            row = ""
            for j in range(n * 2):
                if i % 2 == 0:
                    row += type_1[j % 4]
                else:
                    row += type_2[j % 4]
            res.append(row)
            if i % 2 == 1:
                hash_count += 2
        print("\n".join(res))


for i in range(int(input())):
    upscale(int(input()))