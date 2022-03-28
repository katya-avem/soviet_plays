import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

peredovyes_kolhoz = []



with open(os.path.join(path, 'Хлеб наш насущный.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#rogova"><speaker>Рогова'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)


with open(os.path.join(path, 'Калиновая роща.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#vetrovoy"><speaker>Ветровой'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)

with open(os.path.join(path, 'Поют жаворонки.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#nastya"><speaker>Настя'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)
        if line.startswith('<sp who="#mikola"><speaker>Микола'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)
        if line.startswith('<sp who="#katya"><speaker>Катя'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)
        if line.startswith('<sp who="#pavlina"><speaker>Павлина'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)


with open(os.path.join(path, 'Семья Аллана.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#alty"><speaker>Алты'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)

with open(os.path.join(path, 'На новой земле.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#dehkanbai"><speaker>Дехканбай'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)
        if line.startswith('<sp who="#hafiza"><speaker>Хафиза'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            peredovyes_kolhoz.append(line)




punct = ['!','?','.',',','—','«','»']
speech = list()
for line in peredovyes_kolhoz:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)