#!/usr/bin/python
#coding=utf-8

from math import sqrt
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

#求和
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total
#求均值
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average
#求方差
def grades_variance(scores, average):
    variance = 0.0
    for item in scores:
        variance += (item - average) ** 2
    variance = variance/len(scores)
    return variance
#求均方差
def grades_std_deviation(variance):
    return sqrt(variance)

print grades_std_deviation(grades_variance(grades, grades_average(grades)))