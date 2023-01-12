"CEASER CIPHER PROJECT"
import english_words

words = english_words.english_words_lower_alpha_set

from art import logo

print(logo)
print("WELCOME TO MY CEASER CIPHER DECRYPTER 🙂")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decrypt(message):
    print("All possible outcomes")
    possible_message = []
    for shift in range(1, 26):
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        end_text_list = []
        for letter in message:
            if letter in alphabet:
                index = shifted_alphabet.index(letter)
                end_text_list.append(alphabet[index])
            else:
                end_text_list.append(letter)
        end_text = "".join(end_text_list)
        print(f"The Decoded text with shift {shift} is: {end_text}")
        possible_combination = end_text.split()
        possible_message.append(possible_combination)
    count1 = 0
    for possible in possible_message:
        count2 = 0
        for word in possible:
            if word in words:
                count2 += 1
                if count2 == len(possible):
                    hidden_message = " ".join(possible_message[count1])
                    print(f"\n 😁 The hidden message is: {hidden_message}\n")
        count1 += 1


should_end = False
while not should_end:
    text = input("Type your message:\n").lower()
    decrypt(message=text)
    should_restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if should_restart == "no":
        should_end = True
        print("Goodbye✌️")
