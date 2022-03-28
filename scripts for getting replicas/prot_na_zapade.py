import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

zapad_speech = []



with open(os.path.join(path, 'Снежок.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#dik"><speaker>Дик'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#djon"><speaker>Джон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#djein"><speaker>Джейн'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#devi"><speaker>Дэви'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)

with open(os.path.join(path, 'Я хочу домой.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#sasha"><speaker>Саша'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#ira"><speaker>Ира'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#masha"><speaker>Маша'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#smaida"><speaker>Смайда'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#yanis"><speaker>Янис'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#villi"><speaker>Вилли'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#tolya"><speaker>Толя'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#jenya"><speaker>Женя'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)

speech = list()
for line in zapad_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)