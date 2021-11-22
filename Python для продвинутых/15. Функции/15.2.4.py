def greet(name, *args):
    result = ''
    for n in args:
        result += f' and {n}'
    return f'Hello, {name}{result}!'



print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))