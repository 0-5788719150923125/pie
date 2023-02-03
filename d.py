from re import sub
from sys import getsizeof


def encode(text):
    return sub(r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), text)


def decode(text):
    return sub(r"(\d+)(\D)", lambda m: m.group(2) * int(m.group(1)), text)


raw = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print("raw string is " + str(getsizeof(raw)) + " bytes")

encoded = encode(raw)
print(encoded)
print(decode(encoded))
