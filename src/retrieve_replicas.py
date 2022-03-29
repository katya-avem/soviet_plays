from pathlib import Path
from collections import defaultdict
from lxml import etree


groups = {
    'bosses': [
        ('Макар Дубрава.xml', '#pavel'),  # Павел
        ('Московский характер.xml', '#potapov'),  # Потапов
        ('Рассвет над Москвой.xml', '#kapitolina_andreevna'),  # Капитолина Андреевна
        ('В одном городе.xml', '#ratnikov'),  # Ратников
        ('Глина и фарфор.xml', '#atvasar'),  # Атвасар
    ],
    'deti_na_zapade': [
        ('Снежок.xml', '#dik'),  # Снежок
        ('Снежок.xml', '#djon'),  # Джон
        ('Снежок.xml', '#djein'),  # Джейн
        ('Снежок.xml', '#betti'),  # Бетти
        ('Я хочу домой.xml', '#sasha'),  # Саша
        ('Я хочу домой.xml', '#tolya'),  # Толя
        ('Я хочу домой.xml', '#villi'),  # Вилли
        ('Я хочу домой.xml', '#zhenya'),  # Женя
        ('Я хочу домой.xml', '#ira'),  # Ира
        ('Я хочу домой.xml', '#masha'),  # Маша
    ],
    'historical_leaders': [
        ('Флаг адмирала.xml', '#ushakov'),  # Ушаков
        ('Борьба без линии фронта.xml', '#peter_kondor'),  # Петер Кондор
        ('Канун грозы.xml', '#prigorov'),  # Пригоров
        ('Канун грозы.xml', '#fedorov'),  # Федоров
        ('Потопленные камни.xml', '#djemal'),  # Джемал
        ('Заговор обреченных.xml', '#ganna'),  # Ганна Лихта
    ],
    'inoagent': [
        ('Великая сила.xml', '#milyagin'),  # Милягин
        ('Чужая тень.xml', '#okunev'),  # Окунев
        ('Зеленая улица.xml', '#krutilin'),  # Крутилин
    ],
    'intelligent': [
        ('Жизнь в цитадели.xml', '#professor_miilas'),  # Профессор Мийлас
        ('Жизнь в цитадели.xml', '#pisatel_lillak'),  # Писатель Лиллак
        ('Жизнь в цитадели.xml', '#arhitektor_vyarihein'),  # Архитектор Вярихейн
        ('Илья Головин.xml', '#golovin'),  # Головин
    ],
    'kolhoz_boss': [
        ('Свадьба с приданым.xml', '#pirogov'),  # Пирогов
        ('Калиновая роща.xml', '#romanuk'),  # Романюк
        ('Поют жаворонки.xml', '#pytlevanyi'),  # Пытлеваный
        ('Семья Аллана.xml', '#bairam'),  # Байрам
        ('На новой земле.xml', '#mavlon'),  # Мавлон
    ],
    'partorg': [
        ('Макар Дубрава.xml', '#makar'),  # Макар
        ('Макар Дубрава.xml', '#hmara'),  # Хмара
        ('Макар Дубрава.xml', '#orlov'),  # Орлов
        ('Макар Дубрава.xml', '#zinchenko'),  # Зинченко
        ('Московский характер.xml', '#grineva'),  # Гринева
        ('Московский характер.xml', '#krujkova'),  # Кружкова
        ('Рассвет над Москвой.xml', '#kurepin'),  # Курепин
        ('В одном городе.xml', '#petrov'),  # Петров
        ('В одном городе.xml', '#burmin'),  # Бурмин
        ('Глина и фарфор.xml', '#gauimaliet'),  # Гауймалиет
        ('Хлеб наш насущный.xml', '#zorina'),  # Зорина
        ('Хлеб наш насущный.xml', '#rogov'),  # Рогов
        ('Поют жаворонки.xml', '#palanevich'),  # Паланевич
        ('Поют жаворонки.xml', '#kruglik'),  # Круглик
        ('На новой земле.xml', '#adylov'),  # Адылов
        ('Свадьба с приданым.xml', '#muravev'),  # Муравьев
        ('Совесть.xml', '#arkadev'),  # Аркадьев
        ('Победители.xml', '#muravev'),  # Муравьев
        ('Великая сила.xml', '#shibanov'),  # Шибанов
        ('Великая сила.xml', '#ostroumov'),  # Остроумов
    ],
    'peredovye_kolhoz': [
        ('Хлеб наш насущный.xml', '#rogova'),  # Рогова
        ('Калиновая роща.xml', '#vetrovoi'),  # Ветровой
        ('Поют жаворонки.xml', '#nastya'),  # Настя
        ('Поют жаворонки.xml', '#mikola'),  # Микола
        ('Поют жаворонки.xml', '#katya'),  # Катя
        ('Поют жаворонки.xml', '#pavlina'),  # Павлина
        ('Семья Аллана.xml', '#alty'),  # Алты
        ('На новой земле.xml', '#dehkanbai'),  # Дехканбай
        ('На новой земле.xml', '#hafiza'),  # Хафиза
        ('Свадьба с приданым.xml', '#olga'),  # Ольга
        ('Свадьба с приданым.xml', '#maksim'),  # Максим
    ],
    'peredovye': [
        ('Макар Дубрава.xml', '#gavrila'),  # Гаврила
        ('Макар Дубрава.xml', '#trofim'),  # Трофим
        ('Макар Дубрава.xml', '#galya'),  # Галя
        ('Макар Дубрава.xml', '#marfa'),  # Марфа
        ('Макар Дубрава.xml', '#olga'),  # Ольга
        ('Московский характер.xml', '#krivoshein'),  # Кривошеин
        ('Рассвет над Москвой.xml', '#anuta'),  # Анюта
        ('Рассвет над Москвой.xml', '#igor'),  # Игорь
        ('Рассвет над Москвой.xml', '#sanya'),  # Саня
        ('В одном городе.xml', '#klavdiya'),  # Клавдия
        ('Глина и фарфор.xml', '#skulte'),  # Скульте
        ('Совесть.xml', '#uliya')  # Юлия
    ],
    'prot_na_zapade': [
        ('Я хочу домой.xml', '#smaida'),  # Смайда
        ('Я хочу домой.xml', '#yanis'),  # Янис
        ('Русский вопрос.xml', '#smit'),  # Смит
        ('Голос Америки.xml', '#kidd'),  # Кидд
        ('Голос Америки.xml', '#makdonald'),  # Макдональд
    ],
    'uchenyi_patriot': [
        ('Великая сила.xml', '#lavrov'),  # Лавров
        ('Чужая тень.xml', '#trubnikov'),  # Трубников
        ('Зеленая улица.xml', '#aleksei'),  # Алексей
    ],
    'voennyi': [
        ('Победители.xml', '#vinogradov'),  # Виноградов
        ('Победители.xml', '#krivenko'),  # Кривенко
        ('Победители.xml', '#panteleev'),  # Пантелеев
        ('За тех, кто в море.xml', '#haritonov'),  # Харитонов
        ('За тех, кто в море.xml', '#maksimov'),  # Максимов
        ('За тех, кто в море.xml', '#borovskii'),  # Боровский
        ('За тех, кто в море.xml', '#shubin'),  # Шубин
        ('За тех, кто в море.xml', '#lishev'),  # Лишев
    ],
    'vragi_revolutsii': [
        ('Незабываемый 1919.xml', "#deks"),  # Дэкс
        ('Незабываемый 1919.xml', "#egar"),  # Эгар
        ('Незабываемый 1919.xml', "#m-m_butkevich"),  # М-м Буткевич
        ('Заговор обреченных.xml', "#hristina"),  # Христина
        ('Заговор обреченных.xml', "#mak-hill"),  # Мак-Xилл
        ('Заговор обреченных.xml', "#kurtov"),  # Куртов
        ('Заговор обреченных.xml', "#kardinal"),  # Кардинал
        ('Заговор обреченных.xml', "#vastis"),  # Вастис
        ('Заговор обреченных.xml', "#reichel"),  # Рейчел
        ('Борьба без линии фронта.xml', "#tiit_kondor"),  # Тийт Кондор
        ('Борьба без линии фронта.xml', "#hans"),  # Ханс
        ('Канун грозы.xml', "#demchinov"),  # Демчинов
        ('Канун грозы.xml', "#eremin"),  # Еремин
        ('Канун грозы.xml', "#gammer"),  # Гаммер
        ('Канун грозы.xml', "#polozov"),  # Полозов
        ('Канун грозы.xml', "#ispravnik"),  # Исправник
        ('Канун грозы.xml', "#baron"),  # Барон
        ('Канун грозы.xml', "#chelz"),  # Чельз
        ('Канун грозы.xml', "#ministr"),  # Министр
        ('Канун грозы.xml', "#general-gubernator"),  # Генерал-губернатор
        ('Канун грозы.xml', "#treshchevkov"),  # Трещенков
        ('Потопленные камни.xml', "#sadah"),  # Садах
        ('Потопленные камни.xml', "#rait"),  # Райт
        ('Флаг адмирала.xml', "#orfano"),  # Орфано
        ('Флаг адмирала.xml', "#traubridj"),  # Траубридж
        ('Флаг адмирала.xml', "#nelson"),  # Нельсон
        ('Флаг адмирала.xml', "#ledi_gamilton"),  # Леди Гамильтон
        ('Флаг адмирала.xml', "#uord"),  # Уорд
        ('Флаг адмирала.xml', "#ferdinand"),  # Фердинанд
        ('Флаг адмирала.xml', "#karolina"),  # Каролина
        ('Флаг адмирала.xml', "#segur"),  # Сегюр
    ],
    'zlo_na_zapade': [
        ('Голос Америки.xml', "#parkins"),  # Паркинс
        ('Голос Америки.xml', "#uiler"),  # Уилер
        ('Голос Америки.xml', "#hauston"),  # Хаустон
        ('Голос Америки.xml', "#butler"),  # Бутлер
        ('Снежок.xml', "#andjela"),  # Анджела
        ('Снежок.xml', "#bidl"),  # Бидл
        ('Снежок.xml', "#miss_feller"),  # Мисс Феллер
        ('Снежок.xml', "#taker"),  # Такер
        ('Я хочу домой.xml', "#upmanis"),  # Упманис
        ('Я хочу домой.xml', "#kuk"),  # Кук
        ('Я хочу домой.xml', "#skott"),  # Скотт
        ('Я хочу домой.xml', "#vurst"),  # Вурст
        ('Я хочу домой.xml', "#shpek"),  # Шпек
        ('Я хочу домой.xml', "#dodj"),  # Додж
        ('Я хочу домой.xml', "#eit"),  # Эйт
        ('Русский вопрос.xml', '#guld'),  # Гульд
        ('Русский вопрос.xml', '#makferson'),  # Макферсон
    ],
}



INPUT_FILES_PATH = (Path('..') / 'plays_tei').resolve()
OUTPUT_FILES_PATH = (Path('..') / 'speech_of_characters').resolve()


def check_duplicate_characters(groups):
    print()

    characters_files = defaultdict(set)

    for group_name in groups:
        for text_name, character_id in groups[group_name]:
            characters_files[character_id].add((text_name, group_name))

    for character_id, character_items in characters_files.items():
        if len(character_items) > 1:
            print(f"WARNING: character {character_id} is used more than once - {character_items}")



def check_files(speech_by_text_by_character, groups):
    print()

    all_files = set(speech_by_text_by_character.keys())
    used_files = set([text_name for group_name in groups for text_name, _ in groups[group_name]])

    diff = set(used_files) - set(all_files)
    if len(diff):
        raise Exception(f"ERROR: files {diff} are not present")

    diff = set(all_files) - set(used_files)
    if len(diff) > 0:
        print(f"WARNING: files {diff} are not used!")


def check_characters(speech_by_text_by_character, groups):
    print()

    characters_by_text_in_groups = defaultdict(set)
    for group_name in groups:
        for text_name, character_id in groups[group_name]:
            characters_by_text_in_groups[text_name].add(character_id)

    characters_by_text_in_files = defaultdict(set)
    for text_name, speech_by_character in speech_by_text_by_character.items():
        characters_by_text_in_files[text_name] = set(speech_by_character.keys())

    for text_name in characters_by_text_in_groups:  # characters_by_text_in_groups.keys() is supposed to be subset of characters_by_text_in_files.keys()
        diff = characters_by_text_in_groups[text_name] - characters_by_text_in_files[text_name]
        if len(diff) > 0:
            raise Exception(f"ERROR: characters {diff} are not present in {text_name}")

        diff = characters_by_text_in_files[text_name] - characters_by_text_in_groups[text_name]
        if len(diff) > 0:
            print(f"WARNING: file {text_name} has unused characters {diff}")


def parse_text(file):
    parser = etree.XMLParser(encoding='utf-8', recover=True)  # consider remove_blank_text=True
    tree = etree.parse(file, parser=parser)
    etree.strip_elements(tree, 'stage', 'speaker', with_tail=False)  # with_tail=False is crucial!

    speech_by_character = defaultdict(list)

    for item in tree.iter('sp'):
        who = item.get('who')
        if not who:
            print(etree.tostring(item, encoding='utf-8').decode('utf-8'))
        etree.strip_tags(item, 'l', 'lg', 'p')
        speech_by_character[who].append(item.text)

    return speech_by_character


def parse_texts():
    speech_by_text_by_character = {}

    for file in INPUT_FILES_PATH.iterdir():
        if file.is_file() and file.name.endswith('.xml'):
            speech_by_text_by_character[file.name] = parse_text(file)

    return speech_by_text_by_character


def main(groups):
    speech_by_text_by_character = parse_texts()

    check_duplicate_characters(groups)
    check_files(speech_by_text_by_character, groups)
    check_characters(speech_by_text_by_character, groups)

    speech_by_group = defaultdict(list)

    for group_name in groups:
        for text_name, character_id in groups[group_name]:
            speech_by_group[group_name].extend(
                speech_by_text_by_character[text_name][character_id]
            )

    if not OUTPUT_FILES_PATH.exists():
        OUTPUT_FILES_PATH.mkdir()

    for group_name in groups:
        file_path = OUTPUT_FILES_PATH / f"{group_name}.txt"

        with file_path.open(mode='w', encoding='utf-8') as file:
            file.writelines(speech_by_group[group_name])


if __name__ == '__main__':
    main(groups)
