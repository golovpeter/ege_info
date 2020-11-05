n = int(input())

m7 = 0
m2 = 0

m14 = 0
max_value = 0

for i in range(n):
    value = int(input())
    if value % 7 == 0 and value % 2 != 0 and value > m7:
        m7 = value
    elif value % 2 == 0 and value % 7 != 0 and value > m2:
        m2 = value

    if value % 14 == 0 and value > m14:
        m14 = value
    elif value > max_value:
        max_value = value

control = int(input())

firs_res = m7 * m2
second_res = m14 * max_value
max_res = max(firs_res, second_res)


print('Вычисленное контрольное значение:', max_res)

if max_res == control:
    print('Контроль пройден')
else:
    print('Контроль не пройден')
