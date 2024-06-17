"""Напишите программу, которая принимает от пользователя строку и проверяет,
является ли она палиндромом (читается одинаково слева направо и справа налево)
"""


def is_palindrome(data):
    new_str = ''.join(data.split()).lower()
    if new_str == new_str[::-1]:
        return True
    return False


assert is_palindrome('level') == True
assert is_palindrome('qwerty') == False
assert is_palindrome('No lemon no melon') == True
