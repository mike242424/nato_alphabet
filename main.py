import pandas

user_input = input("Enter a phrase: ").upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")

result = {row.letter: row for (index, row) in data.iterrows()}

my_list = [result[letter].code for letter in user_input]
print(my_list)
