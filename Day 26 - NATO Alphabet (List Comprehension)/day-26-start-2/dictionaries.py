student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
print("For every key-value pair, print key items:")
for (key, value) in student_dict.items():
    print(key)

print("\n")

print("For every key-value pair, print value items:")
for (key, value) in student_dict.items():
    print(value)
