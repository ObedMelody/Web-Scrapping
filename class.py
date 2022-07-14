import os
import sys
import keyword

print(dir(keyword))
# _all__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword',
# 'issoftkeyword', 'kwlist', 'softkwlist']

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print(f'{self.name} is {self.age} years old')
#
#
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# a = Person(name, age)
# a.__str__()

badge = ()


class Student:
    mark = 0

    def __init__(self, name, your_score, gender):
        self.name = name
        self.y_score = your_score
        self.gender = gender

    def score(self, score):
        v = score
        print(f'The student\'s score is {v}')

    def check_score(self):
        if p < 50:
            badge.add('Failed')
        elif p > 50:
            badge.add(' Passed')

    def talk(self):
        if self.gender == 'male'.lower():
            print(f' He just {badge}')
        elif self.gender == 'female'.lower():
            print(f'She just {badge}')


Student.call = classmethod(Student.score)
p = Student.call(int(input('What is the score: ')))
c = Student(input('What is your name: '), p, input('What is your gender: '))
c.talk()
