# Empty 1000x1000 grid initialized with zeros
grid = [[0] * 1000] * 1000
lit = 0
for y in range(0, 1000):
    for x in range(0, 1000):
        if grid[y][x] == 1:
            lit += 1
print(lit)

with open('_day6.txt') as f:
    for line in f:
        parts = line.split(' ')
        command = ''
        start = []
        end = []

        if parts[0] == 'toggle':
            command = 'toggle'
            start = parts[1].split(',')
            end = parts[3].split(',')
        elif parts[0] == 'turn':
            if parts[1] == 'on':
                command = 'on'
            elif parts[1] == 'off':
                command = 'off'
            start = parts[2].split(',')
            end = parts[4].split(',')

        start[0] = int(start[0])
        start[1] = int(start[1])
        end[0] = int(end[0])
        end[1] = int(end[1].strip())

        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):
                print(y, x, grid[y][x])
                if command == 'on':
                    grid[y][x] = 1
                elif command == 'off':
                    grid[y][x] = 0
                elif command == 'toggle':
                    if grid[y][x] == 0:
                        print('toggle on')
                        grid[y][x] = 1
                    elif grid[y][x] == 1:
                        print('toggle off')
                        grid[y][x] = 0
                print(y, x, grid[y][x])


    lit = 0
    for y in range(0, 1000):
        for x in range(0, 1000):
            if grid[y][x] == 1:
                lit += 1


    print(lit)
