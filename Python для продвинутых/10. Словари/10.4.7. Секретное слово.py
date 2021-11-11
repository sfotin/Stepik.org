crypto_word = input()
crypto_dict = {}
for _ in range(int(input())):
    letter, count = input().split(': ')
    crypto_dict[int(count)] = letter

for ch in crypto_word:
    print(crypto_dict[crypto_word.count(ch)], end='')
