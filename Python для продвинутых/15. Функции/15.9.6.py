from string import ascii_uppercase, ascii_lowercase, digits
password = input()
result = all([any([n in digits for n in password]),
              any([l in ascii_lowercase for l in password]),
              any([ul in ascii_uppercase for ul in password]),
              len(password) >= 7])
print('YES' if result else 'NO')
