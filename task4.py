"""Напишите программу, которая умеет добавлять единицу к числу и возвращает список.
Число хранится в виде списка. Например, число 123 будет храниться в виде списка: [1, 2, 4].

[9] => [1, 0]
[1,2,3] => [1,2,4]
[1,1,9] => [1,2,0]
[9,9,9] => [1,0,0,0]
"""


def new_list_numbers(my_list):
    num_str = ''.join(map(str, my_list))

    num = int(num_str) + 1

    return list(map(int, str(num)))


print(new_list_numbers([9]))
print(new_list_numbers([1, 2, 3]))
print(new_list_numbers([1, 1, 9]))
print(new_list_numbers([9, 9, 9]))
