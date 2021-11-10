set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}
set3 = sorted(set1 & set2, reverse=True)
if len(set3) == 0:
    print('BAD DAY')
else:
    print(*set3)

# set1 = {int(i) for i in input().split()}
# set2 = {int(i) for i in input().split()}
#
# if set1.isdisjoint(set2):
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))