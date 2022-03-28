import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

kolhoz_boss = []

with open(os.path.join(path, 'Свадьба с приданым.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#pirogov"><speaker>Пирогов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

with open(os.path.join(path, 'Хлеб наш насущный.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#potapov"><speaker>Потапов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

with open(os.path.join(path, 'Калиновая роща.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#romanuk"><speaker>Романюк'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

with open(os.path.join(path, 'Поют жаворонки.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#pytlevanyi"><speaker>Пытлеваный'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

with open(os.path.join(path, 'Семья Аллана.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#bairam"><speaker>Байрам'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

with open(os.path.join(path, 'На новой земле.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#mavlon"><speaker>Мавлон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            kolhoz_boss.append(line)

speech = list()
for line in kolhoz_boss:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)