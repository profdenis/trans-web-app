def writefile(filename):
    with open(filename, 'a') as f:
        f.write('hello\n')


def writefile2(filename, numbers):
    with open(filename, 'w') as f:
        for x in numbers:
            f.write(str(x))
            f.write('\n')


def writefile3(filename, numbers):
    with open(filename, 'a') as f:
        f.writelines(numbers)


writefile('data2.txt')
writefile2('data3.txt', [3, 4.5, 234, 12.3])
writefile3('data4.txt', ['3\n', '4.5\n', '234\n', '12.3\n'])


msg = 'hello'
for c in msg:
    print(c)
