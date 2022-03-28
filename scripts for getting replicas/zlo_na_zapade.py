import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

zapad_speech = []

with open(os.path.join(path, 'Незабываемый 1919.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#deks"><speaker>Дэкс'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('#egar"><speaker>Эгар'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('#m-m_butkevich"><speaker>М-м Буткевич'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)

with open(os.path.join(path, 'Голос Америки.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('#parkins"><speaker>Паркинс'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#uiler"><speaker>Уилер'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#hauston"><speaker>Хаустон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#butler"><speaker>Бутлер'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)

with open(os.path.join(path, 'Снежок.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#andjela"><speaker>Анджела'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#bidl"><speaker>Бидл'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#miss_feller"><speaker>Мисс Феллер'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#taker"><speaker>Такер'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)

with open(os.path.join(path, 'Я хочу домой.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#upmanis"><speaker>Упманис'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#kuk"><speaker>Кук'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#skott"><speaker>Скотт'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#vurst"><speaker>Вурст'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#shpek"><speaker>Шпек'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#dodj"><speaker>Додж'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)
        if line.startswith('<sp who="#eit"><speaker>Эйт'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)



for i in speech:
    print(i)