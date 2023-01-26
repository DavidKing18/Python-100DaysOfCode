import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_phonetic_dict)


def generate_phonetic():
    word = input("Enter code: ").upper()
    translated = []
    for letter in word:
        try:
            word_denotation = nato_phonetic_dict[letter]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
            break
        else:
            translated.append(word_denotation)
            if len(translated) == len(word):
                print(translated)


generate_phonetic()


#######
#  OR
#######
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         translated = [nato_phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(translated)
#
#
# generate_phonetic()
#
