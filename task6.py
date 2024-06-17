"""Реализуйте функцию которая умеет работать с файлами (читать из заданного файла, записывать в заданный файл).
Программа считает количество строк, слов и букв в заданном файле и дописывает эту информацию обратно в файл,
так же выводит эту информацию на экран
"""


def counts_content_in_file():

    with open('song.txt', 'r', encoding='utf-8') as song:
        content = song.readlines()
        num_lines = len(content)
        num_words = sum(len(line.split()) for line in content)
        num_letters = sum(len(line.replace(' ', '').replace('\n', ''))
                          for line in content)

        with open('song.txt', 'a', encoding='utf-8') as song:
            song.write(f"\nNumber of lines: {num_lines}\n")
            song.write(f"Number of words: {num_words}\n")
            song.write(f"Number of letters: {num_letters}\n")


counts_content_in_file()
