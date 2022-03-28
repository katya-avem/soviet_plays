import os
import re
import string

path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

pered_speech = []

with open(os.path.join(path, 'Макар Дубрава.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#gavrila"><speaker>Гаврила'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('<sp who="#trofim"><speaker>Трофим'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('<sp who="#galya"><speaker>Галя'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('sp who="#marfa"><speaker>Марфа'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('<sp who="#olga"><speaker>Ольга'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)


with open(os.path.join(path, 'Московский характер.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#krivoshein"><speaker>Кривошеин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)

with open(os.path.join(path, 'Рассвет над Москвой.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#anuta"><speaker>Анюта'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('<sp who="#igor"><speaker>Игорь'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)
        if line.startswith('<sp who="#sanya"><speaker>Саня'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)

with open(os.path.join(path, 'В одном городе.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#klavdiya"><speaker>Клавдия'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)


with open(os.path.join(path, 'Глина и фарфор.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#skulte"><speaker>Скульте'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            pered_speech.append(line)




punct = ['!','?','.',',','—','«','»']
speech = list()
for line in pered_speech:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)