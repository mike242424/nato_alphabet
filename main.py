import pandas
user_input = input("Enter a phrase: ").upper()
data = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter: row.code for (index, row) in data.iterrows()}
print(result)
my_list = [result[letter] for letter in user_input]
print(my_list)
