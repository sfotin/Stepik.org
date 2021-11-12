# Напишите программу, переводящую цепь ДНК в цепь РНК.

dnk_rnk = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
for c in input():
    print(dnk_rnk[c], end='')
