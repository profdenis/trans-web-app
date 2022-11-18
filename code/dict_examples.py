from random import randint

pairs = {"one": 1, "two": 2}
passwords = {"denis": "4asdasdasdasd", "john": "asdasdaser324"}

for key in passwords:
    print(key, passwords[key])

passwords["alice"] = "34wretwet"

print("second loop")
for key in sorted(passwords):
    print(key, passwords[key])

if "denis1" not in passwords:
    print("this user doesn't exist")
