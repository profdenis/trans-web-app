# Q1
# simple implementation, doesn't preprocess the string for spaces or accents
# we could instead call the reverse function below to determine if the string
# is equal to its reverse
def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


# Q2
def is_even(x: int) -> bool:
    return x % 2 == 0


# Q3
# not the most efficient because it creates multiple strings in the loop
def reverse(s: str) -> str:
    r = ""
    for c in reversed(s):
        r += c
    return r


# Q4
# there's no char type in Python, so to make sure we get only a 1-char string for
# target_char, we could check that its length is 1
def occurrences(target_char: str, s: str) -> int:
    count = 0
    for c in s:
        if c == target_char:
            count += 1
    return count


def print_separator(title: str, line_width: int = 20) -> None:
    print(f"\n{'-' * line_width} {title} {'-' * line_width}\n")


def main():
    print_separator("Q1")
    words = ["radar", "table", "a", ""]
    for w in words:
        print(w, "is a palindrome" if is_palindrome(w) else "is not a palindrome")

    print_separator("Q2")
    for i in range(10):
        print(i, "is even?", is_even(i))

    print_separator("Q3")
    for w in words:
        print("reverse of", w, "=", reverse(w))

    print_separator("Q4")
    for c in ["a", "b", "c"]:
        for w in words:
            print(f"{c} occurs {occurrences(c, w)} time(s) in {w}")


if __name__ == '__main__':
    main()
