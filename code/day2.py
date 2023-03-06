empty_list = []
print(empty_list)
numbers = [4, 5, -1, 6.7, 12]
print(numbers)
names = ["Denis", "Alice", "Bob"]
print(names)

print(numbers[0])
print(numbers[1])

print("for #1")
for x in numbers:
    print(x)
print("length of numbers =", len(numbers))

print("\nfor #2")
for i in range(len(numbers)):
    print(f"numbers[{i}] = {numbers[i]}")

# print(numbers[5])
print(numbers[-1])
print(numbers[-5])

print("\nfor #3")
for i in range(len(numbers)-1, -1, -1):
    print(f"numbers[{i}] = {numbers[i]}")

print("\nfor #4")
for i in range(1, len(numbers)+1):
    print(f"numbers[{-i}] = {numbers[-i]}")

print("\nfor #5")
for x in reversed(numbers):
    print(x)

print("\nfor #6")
total = 0
for x in numbers:
    total += x
print(total)

# print("\nwhile #1")
# print(names)
# answer = ""
# while answer != "exit":
#     answer = input("Enter a name: ")
#     names.append(answer)
# print(names)

# print("\nwhile #2")
# print(names)
# answer = input("Enter a name: ")
# while answer != "exit":
#     names.append(answer)
#     answer = input("Enter a name: ")
# print(names)

# print("\nwhile #3")
# print(names)
# while True:
#     answer = input("Enter a name: ")
#     if answer == "exit":
#         break
#     names.append(answer)
# print(names)

# print("\nwhile #3")
# print(numbers)
# while True:
#     answer = input("Enter a number: ")
#     if answer == "exit":
#         break
#     numbers.append(float(answer))
# print(numbers)

print(names)
names_upper1 = []
for name in names:
    names_upper1.append(name.upper())
print(names_upper1)

# print(names)
# for i in range(len(names)):
#     names[i] = names[i].upper()
print(names)

names_upper2 = [name.upper() for name in names]
print(names_upper2)

