s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
dict1 = {}
for word in list(s.split()):
    dict1[word] = dict1.get(word, 0) + 1
mx = max(dict1.values())  # максимальное количество повторений
result = [word for word, count in dict1.items() if count == mx]  # список самых часто встречающихся слов
print(min(result))

# result = {i:s.count(i) for i in s.split()}
# print(min([i for i,j in result.items()if j==max(result.values())]))
