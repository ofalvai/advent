import hashlib


input = 'yzbqklnj'
number = -1
found = False

while not found:
    number += 1

    hash = hashlib.md5()
    encoded_input = (input + str(number)).encode('utf-8')
    hash.update(encoded_input)
    value = hash.hexdigest()

    if value[0:6] == '000000':
        found = True

    if number % 1000000 == 0:
        print(number)

print(number)