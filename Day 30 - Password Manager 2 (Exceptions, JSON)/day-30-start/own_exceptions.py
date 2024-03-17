# Own Exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not exceed 3 meters.")
    # ValueError: value entered as args is wrong

bmi = weight / height ** 2
print(bmi)
