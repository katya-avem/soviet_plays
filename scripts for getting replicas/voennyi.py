import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

voennyi_speech = []


with open(os.path.join(path, 'Победители.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#vinogradov"><speaker>Виноградов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'Победители.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#krivenko"><speaker>Кривенко'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'Победители.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#panteleev"><speaker>Пантелеев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'За тех, кто в море.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#haritonov"><speaker>Харитонов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)


with open(os.path.join(path, 'За тех, кто в море.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#maksimov"><speaker>Максимов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'За тех, кто в море.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#borovskii"><speaker>Боровский'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'За тех, кто в море.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#shubin"><speaker>Шубин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)

with open(os.path.join(path, 'За тех, кто в море.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#lishev"><speaker>Лишев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            voennyi_speech.append(line)





punct = ['!','?','.',',','—','«','»']
speech = list()
for line in voennyi_speech:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)