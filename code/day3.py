def hello():
    return 'hello'


def hello2() -> str:
    return 'hello'


def calculate(x):
    return x * 3


def calculate2(x: int) -> int:
    return x * 3


msg = hello()
print(msg)

print(hello())
print(hello)

print(calculate(5))
print(calculate(5.5))
print(calculate('Denis'))
# print(calculate(x))

print(calculate2(5))
print(calculate2(5.5))
print(calculate2('Denis'))

answer = input('Enter a number: ')
x = float(answer)
print(x)

y = x * 2.5
print('the answer is : ' + str(y))
print('the answer is :', y)
