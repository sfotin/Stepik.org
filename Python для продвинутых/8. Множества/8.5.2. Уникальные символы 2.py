text = ''
for _ in range(int(input())):
    text += input().lower()
print(len(set(text)))
