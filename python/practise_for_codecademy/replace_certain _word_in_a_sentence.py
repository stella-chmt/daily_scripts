#!/usr/bin/python
#coding=utf-8

def censor(text, word):
    split_text = text.split(' ')
    censor_text = ""
    asterisks = "*" * len(word)
    for item in split_text:
        if item == word:
            censor_text += asterisks
            censor_text += " "
        else:
            censor_text += item
            censor_text += " "
    censor_text = censor_text[:len(censor_text)]
    return censor_text

print censor("this hack is wack hack", "hack")