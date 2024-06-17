"""Напишите функцию, преобразующую входную строку в выходную как в примерах,
Пусть s = "abcdef...xyz", тогда вывод будет таким:
f(s, 1) => "a"
f(s, 2) => "aba"
f(s, 3) => "abcba"
f(s, 4) => "abcdcba"
"""


def f(s, n):
    if n == 1:
        return s[0]
    part = s[:n]
    mirror = part[::-1]
    return part + mirror


s = "abcdefxyz"
print(f(s, 1))
print(f(s, 2))
print(f(s, 3))
print(f(s, 4))
