res = 0
min_dif = 10000

with open('27-B_demo.txt') as file:
    n = int(file.readline())
    for i in range(n):
        lst = list(map(int, file.readline().split()))
        res += min(lst)
        if max(lst) - min(lst) > 0 and max(lst) - min(lst) < min_dif:
            min_dif = max(lst) - min(lst)

    if res % 3 != 0:
        print(res)
    else:
        print(res + min_dif)
