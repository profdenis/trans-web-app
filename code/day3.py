def read_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            # print(line, end="")
            try:
                numbers.append(int(line))
            except ValueError:
                pass
                # break
    return numbers


numbers = read_numbers("data2.txt")
print(numbers)

for c in "some string":
    print(c)

