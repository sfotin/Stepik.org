# def find_bug(text):
#     result = []
#     for b in 'anton':
#         for ch in range(len(text)):
#             if text[ch] == b:
#                 result.append(text[ch])
#                 text = text[ch + 1:]
#                 break
#     return ''.join(result) == 'anton'

def find_bug(text):
    bug, count = 'anton', 0
    for symbol in text:
        if symbol == bug[count]:
            count += 1
            if count == len(bug):
                break
    return len(bug) == count

print(*[i for i in range(1, int(input()) + 1) if find_bug(input())])


# # лучшее решение с форума решений
# for string in range(1, int(input()) + 1):
#     text, bug, j = input(), 'anton', 0
#     for symbol in text:
#         if symbol == bug[j]:
#             j += 1
#             if j == 5:
#                 print(string, end=' ')
#                 break
