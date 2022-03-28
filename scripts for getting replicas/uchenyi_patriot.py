import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

uchenyi_speech = []

with open(os.path.join(path, 'Великая сила.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#lavrov"><speaker>Лавров'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            uchenyi_speech.append(line)

with open(os.path.join(path, 'Чужая тень.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#trubnikov"><speaker>Трубников'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            uchenyi_speech.append(line)

with open(os.path.join(path, 'Зеленая улица.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#aleksei"><speaker>Алексей'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            uchenyi_speech.append(line)

speech = list()
for line in uchenyi_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)