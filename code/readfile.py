def readfile(filename):
    f = open(filename)
    for line in f:
        # print(line.strip())
        print(line, end='')
    f.close()


def readfile2(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            try:
                numbers.append(float(line))
            except:
                print(line.strip(), 'is not a number')
    return numbers


print(readfile2('data.txt'))
