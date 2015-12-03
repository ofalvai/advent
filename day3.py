def first():
    with open('day3.txt') as file:
        santa_houses = set()
        x = 0
        y = 0
        for char in file.readlines()[0]:
            if (x, y) not in santa_houses:
                santa_houses.add((x, y))

            if char == '^':
                y += 1
            elif char == '>':
                x += 1
            elif char == 'v':
                y -= 1
            elif char == '<':
                x -= 1

        print(len(santa_houses))

def second():
    with open('day3.txt') as file:
        santa_houses = set()
        robo_houses = set()
        santa_x = 0
        santa_y = 0
        robo_x = 0
        robo_y = 0
        santa_houses.add((0, 0))
        robo_houses.add((0, 0))

        for index, char in enumerate(file.readlines()[0]):
            player_x = 0
            player_y = 0

            if char == '^':
                player_y += 1
            elif char == '>':
                player_x += 1
            elif char == 'v':
                player_y -= 1
            elif char == '<':
                player_x -= 1

            if index % 2 == 0:
                robo_x += player_x
                robo_y += player_y
                robo_houses.add((robo_x, robo_y))
            else:
                santa_x += player_x
                santa_y += player_y
                santa_houses.add((santa_x, santa_y))

        # Union of sets
        houses = robo_houses | santa_houses
        print(len(houses))

second()