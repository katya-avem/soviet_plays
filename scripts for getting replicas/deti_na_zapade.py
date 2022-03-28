import os
import re
import string


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/plays_tei"
dirs = os.listdir(path)

zapad_speech = []



with open(os.path.join(path, 'Флаг адмирала.xml'), encoding='utf-8') as file:
    for line in file:
        if line.startswith('<sp who="#ushakov"><speaker>Ушаков'):
            line = line.rsplit('<p>', 1)
            line = line[1]
            line = re.sub('\<(.*?)\>', '', line)
            line = re.sub('\((.*?)\)', '', line)
            zapad_speech.append(line)



speech = list()
for line in zapad_speech:
    for p in string.punctuation:
        if p in line:
            line = line.replace(p, '')
            line.strip()
    speech.append(line)

for i in speech:
    print(i)