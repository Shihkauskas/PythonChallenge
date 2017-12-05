import re

with open('text.txt', 'r', encoding='utf8') as file:
    text = file.read().split(' ')

result = []
for slovo in text:

    #Чуть извращения
    template_search = re.compile(r"\w+(?=[,.])")
    x = template_search.findall(str(text))

    if len(slovo) > 6 and slovo != x:
        result.append(slovo.capitalize())
    else:
        result.append(slovo)

    with open('resultat.txt', 'w', encoding='utf8') as final_file:
        final_file.write(' '.join([str(i) for i in result]))
