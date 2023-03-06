# numbers = [5, 2, 6, 1, -2, 0]
# print(numbers)
# print("length:", len(numbers))
#
# for i in range(len(numbers)):
#     print(i, numbers[i])
#
# for x in numbers:
#     print(x)

words = []
print(words)
# while True:
#     answer = input("Enter a word: ")
#     if answer == "exit":
#         break
#     else:
#         words.append(answer)

# answer = ""
# while answer != "exit":
#     answer = input("Enter a word: ")
#     if answer != "exit":
#         words.append(answer)

keep_going = True
while keep_going:
    answer = input("Enter a word: ")
    # if answer == "" or answer == "exit":
    if answer in ["", "exit"]:
        keep_going = False
    else:
        words.append(answer)

# while answer != "exit":
#     answer = input("Enter a word: ")
#     words.append(answer)
# words.pop()

print(words)

