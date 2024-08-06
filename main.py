import pandas

is_going = True
data = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter: row.code for (index, row) in data.iterrows()}

while is_going:
    user_input = input("Enter a phrase: ").upper()
    try:
        my_list = [result[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letter in the alphabet are allowed.")
    else:
        print(my_list)
        is_going = False

