import io
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

filename = 'langcodes.txt'

with io.open(filename, 'r', encoding='utf8') as f:
    text = f.read()

langcodes = [[e for e in l.split("\t")] for l in text.split("\n")]

with io.open('language_to_characters.yml', 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=Loader)

for i, r in enumerate(data):
    entry = [e for e in langcodes if r['language_name'] == e[1]]
    if len(entry) == 0:
        entry = [e for e in langcodes if r['language_name'] in e[1]]

    if len(entry) == 1:
        if r['iso_639_1'] is None:
            data[i]['iso_639_1'] = entry[0][3]
        if r['iso_639_2'] is None:
            data[i]['iso_639_2'] = entry[0][4]
    else:
        print('not found: ' + r['language_name'])
        print([e for e in langcodes if r['language_name'] in e[1]])

text = ""
for r in data:
    text += "- {characters: " + r['characters'] + \
            ", language_name: " + r['language_name'] + \
            ", iso_639_1: " + str(r['iso_639_1']) + \
            ", iso_639_2: " + str(r['iso_639_2']) + "}\n"

with io.open(filename + '.out', 'w', encoding='utf8') as f:
    f.write(text)
