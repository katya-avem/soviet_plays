import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

inoagent_speech = []

with open(os.path.join(path, 'Великая сила.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#milyagin"><speaker>Милягин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            inoagent_speech.append(line)

with open(os.path.join(path, 'Чужая тень.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#okunev"><speaker>Окунев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            inoagent_speech.append(line)

with open(os.path.join(path, 'Зеленая улица.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#krutilin"><speaker>Крутилин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            inoagent_speech.append(line)

speech = list()
for line in inoagent_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)