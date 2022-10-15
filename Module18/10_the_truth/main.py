text=input('введите текст').split()


def decryption(messenge):
    translated = ""
    for i_word in messenge:
        if i_word in letters:
            num_index = letters.find(i_word)
            translated += letters[num_index - 1]
        else:
            translated += i_word
    return translated


def shift(text, key):
    word_ln = len(text)
    shift = key % word_ln
    text = text[-shift:] + text[:-shift]
    return text

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"



text_2 = []
key = 3
for i_word in text:
    text_decryption = decryption(i_word)
    shift_text = shift(text_decryption, key)
    if shift_text.endswith("/"):
        key += 1
        text_2.append(shift_text)
    else:
        text_2.append(shift_text)

text_2 = " ".join(text_2)
text_2 = text_2.replace("+", "*")
text_2 = text_2.replace("-", ",")
text_2 = text_2.replace("(", "'")
text_2 = text_2.replace("..", "--")
text_2 = text_2.replace('"', "!")
text_2 = text_2.replace("/", ".\n")

print(text_2)