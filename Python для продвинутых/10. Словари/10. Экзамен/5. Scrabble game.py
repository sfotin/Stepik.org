dic = {1: 'AEILNORSTU',
       2: 'DG',
       3: 'BCMP',
       4: 'FHVWY',
       5: 'K',
       8: 'JX',
       10: 'QZ'}
score = 0
for c in input():
    for point, letters in dic.items():
        if c in letters:
            score += point
print(score)
