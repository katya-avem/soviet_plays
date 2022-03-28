import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

leaders_speech = []

with open(os.path.join(path, 'Флаг адмирала.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#ushakov">'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            leaders_speech.append(line)

with open(os.path.join(path, 'Борьба без линии фронта.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#peter_kondor">'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            leaders_speech.append(line)


with open(os.path.join(path, 'Канун грозы.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#prigorov">'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            leaders_speech.append(line)

with open(os.path.join(path, 'Потопленные камни.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#djemal">'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            leaders_speech.append(line)




speech = list()
for line in leaders_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)

