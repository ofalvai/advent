input = '1113122113'

for i in range(0, 50):
    output = ''
    last_duplicate = ''
    for index, char in enumerate(input):
        if char == last_duplicate:
            continue

        index2 = index + 1
        duplicate_count = 1
        last_duplicate = input[index]

        while index2 < len(input) and input[index2] == char:
            index2 += 1
            duplicate_count += 1
        
        output += str(duplicate_count)
        output += char

    input = output

print(len(output))
