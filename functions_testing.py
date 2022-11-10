## Exercise 8

# Caesar Cipher
#
# A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter
# found by moving n places down the alphabet. For example, assume the input plain text is the following:
#
# `abcd xyz`
#
#
# If the shift value, n, is 4, then the encrypted text would be the following:
#
# `efgh bcd`
#
# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in
# the cipher.
#
# The function will return an encrypted string with all letters transformed and all punctuation and whitespace
# remaining unchanged.
#
# Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_cipher(plain_text, shift):
    new_text = ""
    for char in plain_text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % 26
            # print(alphabet[new_index], end="")
            new_text += alphabet[new_index]
        else:
            print(char, end="")
            new_text += char
    return new_text


if __name__ == '__main__':
    # caesar_cipher('abcd xyz', 4)
    print(caesar_cipher('abcd xyz', 4))
    print(caesar_cipher('efgh bcd', -4))
