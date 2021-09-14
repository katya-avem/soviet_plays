import re
from functools import reduce

_RU = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'є': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i', 'ї': 'yi', 'й': 'i',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'u', 'я': 'ya'
}


def _reducer(string, letter):
    if letter in _RU:
        return string + _RU.get(letter)
    elif letter.lower() not in _RU:
        return string + letter
    else:
        return string + _RU.get(letter.lower()).upper()


def transliterate(text):
    text = re.sub("[ъь]+", "", text)
    return reduce(_reducer, text, '')