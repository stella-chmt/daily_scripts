#!/usr/bin/python
#coding=utf-8

import string
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
'''
for student in students:
    print student["name"]
    for item in ["homework", "quizzes", "tests"]:
        score = string.join(str(int(e))+',' for e in student[item])
        print '[' + score[0 :len(score)-1] + ']'
'''
'''
#这种方法更简单，上面的搞太复杂了
for item in students:
    print item["name"]
    print item["homework"]
    print item["quizzes"]
    print item["tests"]
'''

def average(lst):
    sum = 0
    for item in lst:
        sum += float(item)
    return sum / len(lst)

def get_average(student):
    return average(student["homework"])*0.1 + average(student["quizzes"])*0.3 + average(student["tests"])*0.6

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >=80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    elif score < 70 and score >= 60:
        return "D"
    else :
        return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(list):
    class_score = []
    for student in list:
        class_score.append(get_average(student))
    return average(class_score)

#计算整个class的分数和等级
students = [lloyd, alice, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))
