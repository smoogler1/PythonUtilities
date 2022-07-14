import os

fw=open('dict.c','w');
fr=open('input.txt','r');


data = fr.readlines();

for sline in data:
    sep = '//'
    stripped = text.split(sep, 1)[0]
