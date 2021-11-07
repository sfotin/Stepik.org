text = ''
for t in input():
    if t not in '.,;:-?!':
        text += t

print(len(set(text.lower().split())))
