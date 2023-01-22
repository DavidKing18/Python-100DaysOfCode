import pandas

# TODO 1. Create a dictionary in this format:

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter code: ").upper()
translated = [nato_phonetic_dict[letter] for letter in word]
print(translated)
