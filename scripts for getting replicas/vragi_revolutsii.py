import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

vragi = []

with open(os.path.join(path, 'Незабываемый 1919.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#deks"><speaker>Дэкс'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('#egar"><speaker>Эгар'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('#m-m_butkevich"><speaker>М-м Буткевич'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)

with open(os.path.join(path, 'Заговор обреченных.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('#hristina"><speaker>Христина'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#mak-hill"><speaker>Мак-Xилл'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#kurtov"><speaker>Куртов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#kardinal"><speaker>Кардинал'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#vastis"><speaker>Вастис'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#reichel"><speaker>Рейчел'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)


with open(os.path.join(path, 'Борьба без линии фронта.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#tiit_kondor"><speaker>Тийт Кондор'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#hans"><speaker>Ханс'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)

with open(os.path.join(path, 'Канун грозы.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#demchinov"><speaker>Демчинов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#eremin"><speaker>Еремин'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#gammer"><speaker>Гаммер'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#polozov"><speaker>Полозов'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#ispravnik"><speaker>Исправник'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#baron"><speaker>Барон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#chelz"><speaker>Чельз'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#ministr"><speaker>Министр'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#general-gubernator"><speaker>Генерал-губернатор'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#treshchevkov"><speaker>Трещенков'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)

with open(os.path.join(path, 'Потопленные камни.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#sadah"><speaker>Садах'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#rait"><speaker>Райт'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)

with open(os.path.join(path, 'Флаг адмирала.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#orfano"><speaker>Орфано'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#traubridj"><speaker>Траубридж'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#nelson"><speaker>Нельсон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#ledi_gamilton"><speaker>Леди Гамильтон'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#uord"><speaker>Уорд'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#ferdinand"><speaker>Фердинанд'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#karolina"><speaker>Каролина'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)
        if line.startswith('<sp who="#segur"><speaker>Сегюр'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            vragi.append(line)



punct = ['!','?','.',',','—','«','»']
speech = list()
for line in vragi:
    for p in punct:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)