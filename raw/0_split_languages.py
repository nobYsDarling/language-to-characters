import io

filename = 'language_to_characters.yml'

with io.open(filename, 'r', encoding='utf8') as f:
    text = f.read()

result = []
for l in text.split("\n"):
    if l != '':
        chars = l.split('-')[0]
        lngs = l.split('-')[1]
        for lng in lngs.split(','):
            result.append({'characters': chars, 'language_name': lng})

text = ""
for r in result:
    text += "- {characters: " + r['characters'] + ", language_name: " + r['language_name'] + "}\n"

with io.open(filename + '.out', 'w', encoding='utf8') as f:
    f.write(text)
