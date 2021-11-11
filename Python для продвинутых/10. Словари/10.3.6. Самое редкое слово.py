text = [word.strip('.,!?:;-') for word in input().lower().split()]  # список слов без знаков препинания
dict1 = {word:text.count(word) for word in text}  # словарь {слово:повторений}
result = [word for word in dict1 if dict1[word] == min(dict1.values())]  # список редких слов
print(min(result))  # меньшее по лексикографическое
