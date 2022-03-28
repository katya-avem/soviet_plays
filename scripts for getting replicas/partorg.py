import os
import re
import string

path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

part = []

with open(os.path.join(path, 'Макар Дубрава.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#makar"><speaker>Макар'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#hmara"><speaker>Хмара'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#orlov"><speaker>Орлов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#zinchenko"><speaker>Зинченко'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Московский характер.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#grineva"><speaker>Гринева'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#krujkova"><speaker>Кружкова'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)


with open(os.path.join(path, 'Рассвет над Москвой.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#kurepin"><speaker>Курепин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)


with open(os.path.join(path, 'В одном городе.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#petrov"><speaker>Петров'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#burmin"><speaker>Бурмин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)


with open(os.path.join(path, 'Глина и фарфор.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#gauimaliet"><speaker>Гауймалиет'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Хлеб наш насущный.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#zorina"><speaker>Зорина'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#rogov"><speaker>Рогов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)


with open(os.path.join(path, 'Поют жаворонки.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#palanevich"><speaker>Паланевич'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#kruglik"><speaker>Круглик'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'На новой земле.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#adylov"><speaker>Адылов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Свадьба с приданым.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#muravev"><speaker>Муравьев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Совесть.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#arkadev"><speaker>Аркадьев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Победители.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#muravev"><speaker>Муравьев'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)

with open(os.path.join(path, 'Великая сила.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#shibanov"><speaker>Шибанов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)
        if line.startswith('<sp who="#ostroumov"><speaker>Остроумов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            part.append(line)




punct = ['!','?','.',',','—','«','»']
speech = list()
for line in part:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)
