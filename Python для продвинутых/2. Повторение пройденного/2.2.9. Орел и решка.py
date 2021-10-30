chain = input()
count = [0]
for i in chain:
    if i == 'О':
        count.append(count[0])
        count[0] = 0
    elif i == 'Р':
        count[0] += 1
print(max(count))

# лучшее решение с форума
s = input().split('О')
print(s)
print(len(max(s)))