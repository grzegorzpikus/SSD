import re

postcodes = ['M1 1AA', 'M60 1NW', 'CR2 6XH', 'W1A 1HQ', 'EC1A 1BB']
pattern = "[A-Z][A-Z0-9]{1,3} [0-9][A-Z0-9]{1,2}"

result = []

for i in postcodes:
    if re.search(pattern, i):
        result.append((i, 'valid'))
    else:
        result.append((i, 'invalid'))

print(result)


