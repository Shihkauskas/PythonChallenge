with open('text.txt', 'r', encoding='utf8') as file:
    text = file.read().split(' ')
result = []
for slovo in text:
    if len(slovo) > 6:
        result.append(slovo.capitalize())
    else:
        result.append(slovo)

with open('resultat.txt', 'w', encoding='utf8') as final_file:
    final_file.write(' '.join([str(i) for i in result]))
