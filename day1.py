second = True

with(open('day1.txt')) as file:
    lines = file.readlines()

    floor = 0
    for index, char in enumerate(lines[0]):
        print(index)
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if second and floor < 0:
            print('entering basement: ' + str(index + 1))
            break

    print(floor)
