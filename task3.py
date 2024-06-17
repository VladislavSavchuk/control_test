"""Напишите функцию, которая принимает строку и возвращает кол-во заглавных и строчных букв.
'The quick Brow Fox' => Upper case characters: 3, Lower case characters: 12
"""


def count_upper_lower(simple_str):
    upper_count = sum(1 for char in simple_str if char.isupper())
    lower_count = sum(1 for char in simple_str if char.islower())
    return f"Upper case characters: {upper_count}, Lower case characters: {lower_count}"


s = 'The quick Brow Fox'
print(count_upper_lower(s))
