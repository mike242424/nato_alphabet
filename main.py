from nato_dictionary import nato_alphabet

user_input = input("Enter a phrase: ")
nato_phrase = []

for letter in user_input:
    nato_phrase.append(nato_alphabet[letter])

print(nato_phrase)