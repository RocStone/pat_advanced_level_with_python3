"""
start time: 2019年2月20日21:29:59
end time:  2019年2月20日22:19:21
坑: 注意审题的时候发现的关键点都应该圈出来写下来，比如升序输出，比如id是7位数字，这意味着有可能存在0开头的数字
"""
from collections import defaultdict


class Book:
    def __init__(self, id1, book_name, author_name, key_words, publisher, year):
        self.id1 = id1
        self.book_name = book_name
        self.author_name = author_name
        self.key_words = key_words
        self.publisher = publisher
        self.year = year


def print_result(a_map, string):
    if string in a_map:
        for book in sorted(a_map[string], key=lambda x: x.id1):
            print(f"{book.id1:07d}")
    else:
        print('Not Found')


n = int(input())
book_name_map = defaultdict(list)
author_name_map = defaultdict(list)
key_words_map = defaultdict(list)
publisher_map = defaultdict(list)
year_map = defaultdict(list)

for i in range(n):
    id1 = int(input())
    book_name = input()
    author_name = input()
    key_words = input().split()
    publisher = input()
    year = input()
    book = Book(id1, book_name, author_name, key_words, publisher, year)
    book_name_map[book_name].append(book)
    author_name_map[author_name].append(book)
    for key_word in key_words:
        key_words_map[key_word].append(book)
    publisher_map[publisher].append(book)
    year_map[year].append(book)

n = int(input())

for i in range(n):
    line = input().split(":")
    no = int(line[0])
    string = line[1].strip()
    print(f"{no}: {string}")
    if no == 1:
        print_result(book_name_map, string)
    elif no == 2:
        print_result(author_name_map, string)
    elif no == 3:
        print_result(key_words_map, string)
    elif no == 4:
        print_result(publisher_map, string)
    elif no == 5:
        print_result(year_map, string)

