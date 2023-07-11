from english_words import get_english_words_set

# english_words_set: A set of English words containing both upper- and
#     lower-case letters; with punctuation.
# english_words_lower_set: A set of English words containing lower-case
#     letters; with punctuation.
# english_words_alpha_set: A set of English words containing both upper-
#     and lower-case letters; with no punctuation.
# english_words_lower_alpha_set: A set of English words containing
#     lower-case letters; with no punctuation.

list_of_words = get_english_words_set(['web2'], lower=True)

# with open("C:\\Users\\DAVID\\Desktop\\words.txt", "w") as file:
#     for word in sorted(list_of_words):
#         file.write(f"{word}\n")
