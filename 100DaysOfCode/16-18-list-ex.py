NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
NAMES = [name.title() for name in NAMES]
print(NAMES)

def reverse_name(name):
    first,last = name.split()
    return f'{last} {first}'

n = [reverse_name(name) for name in NAMES]
print(n)
