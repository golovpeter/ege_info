m7 = 0 
max_value = 0

count = 0

while True:
    value = int(input())
    if value == 0:
        break 

    if value % 7 != 0 and value > max_value:
        max_value = value

    if value % 7 == 0 and value % 49 != 0 and value > m7:
        m7 = value

    count += 1


control = int(input())

max_res = m7 * max_value

if max_res == 0:
    max_res += 1

print('Введено чисел:', count)
print('Контрольное значение:', control)
print('Вычисленное значение:', max_res)

if max_res == control:
    print('Значения совпали')
else:
    print('Значения не совпали')

