def chunked(list_1, ch):
    chunked_list = []
    for i in range(0, len(text), ch):
        chunked_list.append(list_1[i:i + ch])
    return chunked_list

text = input().split()
chunk = int(input())
print(chunked(text, chunk))
