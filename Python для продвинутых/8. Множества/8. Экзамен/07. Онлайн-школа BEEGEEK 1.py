test_set = {int(i) for i in input().split()}
user_set = {int(i) for i in input().split()}

print(('NO', 'YES')[test_set == user_set])
