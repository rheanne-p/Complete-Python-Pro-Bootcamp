# TODO 1. Lists
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# [inclusive: non-inclusive]
print(f"Slice a segment: {piano_keys[2:5]}")

print(f"Slice from one point until the end: {piano_keys[2:]}")

print(f"Slice everything until a specified end: {piano_keys[:5]}")

print(f"Slice with an increment: {piano_keys[2:5:2]}")

print(f"Slice every item with an increment{piano_keys[::2]}")

print(f"Slice every item backwards (negative increment): {piano_keys[::-1]}")


# TODO 2. Tuples
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti", "do")

print(f"Slice a tuple segment: {piano_tuple[2:5]}")