def first():
    nice_strings = 0
    blacklist = ['ab', 'cd', 'pq', 'xy']

    with open('day5.txt') as f:
        for line in f:
            if any(x in line for x in blacklist):
                continue
            
            vowels = ['a', 'e', 'i', 'o', 'u']
            vowel_count = 0
            double_letter_count = 0
            prev_char = ''
            for char in line:
                if prev_char == char:
                    double_letter_count += 1
                prev_char = char
                if char in vowels:
                    vowel_count += 1

            if vowel_count < 3:
                continue
            if double_letter_count == 0:
                continue

            nice_strings += 1

    print(nice_strings)

def second():
    nice_strings = 0

    with open('day5.txt') as f:
        for line in f:
            line = line.strip()
            pairs = list()
            for i in range(1, len(line)):
                pairs.append(line[i-1] + line[i])
            print(pairs)

            appears_twice = False
            repeat_between = False
            for pair in pairs:
                # Finding one more occurence of a pair in the list
                # We make a new list of pairs, from wich we remove:
                # - the actual pair we're looking for
                # - the next pair, since overlapping is not allowed
                _pairs = list(pairs)
                _pairs.remove(pair)
                index = pairs.index(pair)
                if index != len(pairs)-1:
                    _pairs.remove(pairs[index+1])

                if pair in _pairs:
                    appears_twice = True
                    


                # Reusing pairs for the second condition:
                # Repeating letters with one letter in between means:
                # A pair's first character is the same as the next pair's second character
                if index < len(pairs) - 1:
                    next_pair = pairs[index + 1]
                    if pair[0] == next_pair[1]:
                        repeat_between = True

            if appears_twice and repeat_between:
                print(appears_twice)
                print('nice')
                nice_strings += 1
        print(nice_strings)


second()