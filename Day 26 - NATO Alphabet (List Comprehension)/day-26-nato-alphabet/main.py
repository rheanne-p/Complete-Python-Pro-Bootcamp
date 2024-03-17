import pandas

data = pandas.read_csv("nato-phonetic-alphabet.csv")

nato_dict = {data.letter[index]:data.code[index] for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
print([nato_dict[letter] for letter in user_input])
