import itertools
from pathlib import Path
from transliterate import transliterate
from pprint import pprint


input_folder = Path('input_txt').resolve()
output_folder = Path('output').resolve()

input_filename = 'великий_государь.txt'
output_filename = 'великий_государь.xml'

cast = [
    '1-й голос',
    '2-й голос',
    '3-й голос',
    'Hагой',
    'Акакий',
    'Алферьев',
    'Бельский',
    'Бояре',
    'Боярыня Годунова',
    'Бутурлин',
    'Василий Шуйский',
    'Вельский',
    'Воротынский',
    'Второй купец',
    'Второй сказитель',
    'Годунов',
    'Годунов и Шуйский',
    'Гонец',
    'Девушка',
    'Дмитрий Шуйский',
    'Дьяк',
    'Захарьин-Юрьев',
    'Иван',
    'Ирина',
    'Кириловна',
    'Купцы',
    'Куракин',
    'Лекарь',
    'Магнус',
    'Мария',
    'Мстиславский',
    'Нагой',
    'Одоевский',
    'Первый купец',
    'Первый сказитель',
    'Посол',
    'Сицкий',
    'Сосед Акакия',
    'Третий сказитель',
    'Царевич Иван',
    'Царевич Феодор',
    'Чернец'
]

cast = {hero: '#' + transliterate(hero).lower().replace(' ', '_') for hero in cast}
cast['Годунов и Шуйский'] = f'{cast["Годунов"]} {cast["Василий Шуйский"]}'

pprint(cast)

def main():
    input_filepath = input_folder / input_filename
    with open(input_filepath) as file:
        text = file.read()

    def is_xml_block(block):
        return block[0].startswith('<')

    def has_stage(block):
        for line in block:
            if line.startswith('<stage>'):
                return True
        return False

    def split_by_stage(body):
        groups = []
        group = []

        for line in body:
            if line.startswith('<stage>'):
                if len(group) > 0:
                    groups.append(group)

                group = [line]
                continue

            if len(group) == 1 and group[0].startswith('<stage'):
                groups.append(group)
                group = []

            group.append(line)

        if len(group) > 0:
            groups.append(group)

        return groups

    def add_lg_markup(lg):
        return [
            '<lg>',
            *[f'<l>{line}</l>' for line in lg],
            '</lg>'
        ]

    def find_hero(speaker):
        if speaker in cast:
            return cast[speaker]

        for key in cast:
            if speaker.startswith(key):
                return cast[key]

    def add_markup_to_block(block):
        if has_stage(block):
            speaker, *body = block
            groups = split_by_stage(body)
            return [
                f'<sp who="{find_hero(speaker)}">',
                f'<speaker>{speaker}</speaker>',
                *itertools.chain(*[block if is_xml_block(block) else add_lg_markup(block) for block in groups]),
                '</sp>'
            ]
        else:
            speaker, *lg = block
            return [
                f'<sp who="{find_hero(speaker)}">',
                f'<speaker>{speaker}</speaker>',
                *add_lg_markup(lg),
                '</sp>'
            ]

    blocks = [block.split('\n') for block in text.split('\n\n')]
    blocks = [block if is_xml_block(block) else add_markup_to_block(block) for block in blocks]

    output_filepath = output_folder / output_filename
    with open(output_filepath, 'w') as file:
        text = '\n\n'.join(['\n'.join(block) for block in blocks])
        file.write(text)


# if __name__ == '__main__':
    # main()
