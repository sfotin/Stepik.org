dir_set = set(input().split())
subdir_set = set(input().split())
print(*sorted(dir_set | subdir_set))
