m = int(input())
data = [{input() for n in range(int(input()))} for _ in range(m)]
result_set = set(data[0])
for list in data:
    result_set.intersection_update(list)
print(*sorted(result_set), sep='\n')

# n = int(input())
# result = {input() for _ in range(int(input()))}
# for _ in range(n - 1):
#     result &= {input() for _ in range(int(input()))}
# print(*sorted(result), sep='\n')