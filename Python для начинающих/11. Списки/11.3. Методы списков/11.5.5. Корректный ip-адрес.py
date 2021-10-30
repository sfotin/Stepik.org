ip_address = input().split('.')
flag = 0
for ip in ip_address:
    if 0 <= int(ip) <= 255: flag +=1
print("YES" if flag == 4 else "NO")