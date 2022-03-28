import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

intelligent_speech = []

with open(os.path.join(path, 'Жизнь в цитадели.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#professor_miilas"><speaker>Профессор Мийлас'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            intelligent_speech.append(line)

with open(os.path.join(path, 'Жизнь в цитадели.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#pisatel_lillak"><speaker>Писатель Лиллак'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            intelligent_speech.append(line)

with open(os.path.join(path, 'Жизнь в цитадели.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#arhitektor_vyarihein"><speaker>Архитектор Вярихейн'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            intelligent_speech.append(line)


with open(os.path.join(path, 'Илья Головин.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#golovin"><speaker>Головин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            intelligent_speech.append(line)

speech = list()
for line in intelligent_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)
