with open('file.txt') as file:
    data = list(map(int, file.readline().split()))
    capacity, users_num = data[0], data[1]
    files_vol = sorted([int(file.readline()) for i in range(users_num)])

    files_sum = 0
    last_i = 0

    for i in range(users_num):
        files_sum += files_vol[i]

        if files_sum > capacity:
            files_sum -= files_vol[i]
            break

        last_i = i

        max_el = files_vol[last_i]

    for i in range(last_i + 1, users_num):
        if (files_sum - max_el) + files_vol[i] <= capacity:
            files_sum = files_sum - max_el + files_vol[i]
            max_el = files_vol[i]
        else:
            break

    print(last_i + 1, max_el)