import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

bosses_speech = []

with open(os.path.join(path, 'Макар Дубрава.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#pavel"><speaker>Павел'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            bosses_speech.append(line)

with open(os.path.join(path, 'Московский характер.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#potapov"><speaker>Потапов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            bosses_speech.append(line)

with open(os.path.join(path, 'Рассвет над Москвой.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#kapitolina_andreevna"><speaker>Капитолина Андреевна'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            bosses_speech.append(line)

with open(os.path.join(path, 'В одном городе.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#ratnikov"><speaker>Ратников'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            bosses_speech.append(line)


with open(os.path.join(path, 'Глина и фарфор.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#atvasar"><speaker>Атвасар'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            bosses_speech.append(line)


punct = ['!','?','.',',','—','«','»']
speech = list()
for line in bosses_speech:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)