person = {
    "name": "Denis",
    "emails": ["denis@example.com", "denis123@example.com"],
    "address": "somewhere"
}

print(person)
print(person["name"])

for key in person:
    print(f"person[{key}] = {person[key]}")

person["address"] = "somewhere else"
print(person)
person["id"] = 3
print(person)
# print(person["abcd"])
# person["abcd"] = "sdfsdf"
print("abcd ---> ", person.get("abcd"))
print("id ---> ", person.get("id"))
print("abcd ---> ", person.get("abcd", "key doesn't exist"))

person_list = [person]
print(person_list)

person_list = [
    {
        "name": "Denis",
        "emails": ["denis@example.com", "denis123@example.com"],
        "address": "somewhere"
    },
    {
        "name": "Bob",
        "emails": ["bob@example.com", "bob123@example.com"],
        "address": "somewhere"
    }
]

# person_list.append(person)
names = ["Denis", "Alice", "Bob"]
person2 = {name: name.upper() for name in names}
print(person2)
print(person2.keys())
person3 = {key: "test" for key in person}
print(person3)


def get_data(key):
    return key.upper()


person4 = {key: get_data(key) for key in person}
print(person4)
