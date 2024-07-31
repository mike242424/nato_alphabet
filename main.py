from nato_dictionary import nato_alphabet

user_input = input("Enter a phrase: ").lower()

nato_phrase = [nato_alphabet[letter] for letter in user_input]
print(nato_phrase)