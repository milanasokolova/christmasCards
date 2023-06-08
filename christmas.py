names = []
with open('employees.txt', 'r') as file:
    for line in file:
        name = line.strip()
        names.append(name)

with open('template.txt', 'r') as file:
    template = file.read()

import os
if not os.path.exists('christmasCards'):
    os.mkdir('christmasCards')

for name in names:
    card_content = template.replace('NAME', name)

    with open(f'christmasCards/{name}.txt', 'w') as file:
        file.write(card_content)
