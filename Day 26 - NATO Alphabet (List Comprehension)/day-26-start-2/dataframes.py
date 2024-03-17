import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through a data frame:
student_data_frame = pandas.DataFrame(student_dict)

for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
print("Executing row.student:")
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "Angela":
        print(row.score)
        # each row is a Series object
