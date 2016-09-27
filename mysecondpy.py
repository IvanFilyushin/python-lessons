# Вторая программа на Python
# Создаёт частотный словарь в двух формах: по алфавиту и по частоте
# 27.09.2016
# Доработать: слово в конце предложения - обработка знака препинания

import sys
import re

D={}
pattern = r'[a-z]|[абвгдеёжзийклмнопрстуфхцчшщьъыэюя]+'
pattern_pm = r'[(")./:1234567890=%\]]+'
word = re.compile(pattern)
pm = re.compile(pattern_pm)

file_name = r'd:\Python\WaP'

for S in open(file_name+'.txt'):
     listWords = re.split(r'[;,\s]', S)
     for element in listWords:
         el = element.lower() 
         if el in D:
            D[el] += 1
         elif word.match(el) and not pm.search(el):
              D[el] = 1
              
L_ab = [[w,D[w]] for w in D] # словарь по алфавиту
L_ab.sort()
f = open(file_name+'_dictAB.txt','w')
for s in L_ab:
     f.write(str(s) + '\n')
f.close()

L = [[D[w],w] for w in D] # частотный словарь
L.sort(reverse=True)
f = open(file_name+'_dict.txt','w')
for s in L:
     f.write(str(s) + '\n')
f.close()

print('Cловарь из ' + str(len(L)) + ' слов')




        
