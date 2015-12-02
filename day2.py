file = open('day2.txt')
lines = file.readlines()


def first():
    sum_paper = 0

    for line in lines:
        dims = line.split('x')
        a = int(dims[0])
        b = int(dims[1])
        c = int(dims[2])

        ab = a * b
        ac = a * c
        bc = b * c
        area =  2 * ab + 2 * ac + 2 * bc
        smallest = min(ab, ac, bc)

        paper = area + smallest
        sum_paper += paper

    print(sum_paper)


def second():
    sum_ribbon = 0

    for line in lines:
        dims = line.split('x')
        a = int(dims[0])
        b = int(dims[1])
        c = int(dims[2])        
        
        dims = [a, b, c]
        dims.sort()

        ribbon = 2 * dims[0] + 2 * dims[1]
        ribbon += a * b * c
        sum_ribbon += ribbon
        
    print(sum_ribbon)
file.close()

second()
