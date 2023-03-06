x = 5
y = 3.7
z = x + y
print(z)
print(5 / 2)
print(5 // 2)  # this is a comment
print(5 % 2)
print(2 ** 10)
print(2 ** 100)
# x = 2 ** 1000000000

x = "hello"
print(x)
x = 'hello'
x = """hello
hi
"""
print(x)
print(x)
print(f"the value of y is {y} and the value of z is {z}")

# y = 11
y = -2
# if y < 10 and y > 0:
if y < 10:
    print("y is small")
else:
    print("y is big")
print("after if 1")

if y < 0:
    print("y is negative")
elif y < 10:
    print("y is small")
else:
    print("y is big")
print("after if 2")

print("while")
i = 0
while i < 5:
    print(i)
    # i = i + 1
    i += 1

print("for 1")
for i in range(5):
    print(i)

print("for 2")
for i in range(1, 5):
    print(i)

print("for 3")
for i in range(1, 5, 2):
    print(i)

print("for 4")
for i in range(5, 0, -1):
    print(i)

print("for 5")
for i in range(4, -1, -1):
    print(i)


def some_function(x):
    result = x * x
    print(result)
    return result


print(some_function(4))
