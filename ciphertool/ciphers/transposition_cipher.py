# Python 3 implementation of Columnar Transposition
import math
from itertools import permutations


def bruteforce(ciphertext):

    keyword = str(input("Keyword to find"))
    alphabet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    m = 2
    r = 2
    while True:

        m += 1
        alphabetPerms = alphabet[0:m]

        perms = permutations(alphabetPerms, r)
        for i in list(perms):

            if r == max(i):
                print(i)
            if keyword in decryptMessage(ciphertext, i):
                print(i)

                return i

        r = m


# Encryption
def encryptMessage(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty
    # the empty cell of the matix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend("_" * fill_null)

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i : i + col] for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += "".join([row[curr_idx] for row in matrix])
        k_indx += 1
    print(cipher.replace("_", ""))
    return cipher


# Decryption
def decryptMessage(cipher, key):
    msg = ""

    # track key indices
    k_indx = 0

    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    fill_null = int((row * col) - msg_len)

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for i in range(col):

        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):

            if j == row - 1 and curr_idx > (col - fill_null - 1):
                dec_cipher[j][curr_idx] = "_"
            else:
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1

        k_indx += 1
        # todo
    # current index on bottom row
    # right position = insert_
    # convert decrypted msg matrix into a string

    try:
        msg = "".join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = msg.count("_")

    if null_count > 0:
        return msg[:-null_count]

    return msg


def main():

    mode = str(input("e for encypt d for decrypt:  "))
    if mode == "e":

        plaintext_unfiltered = input("Enter plaintext to encrypt: \n\n\n\n ")

        # Filters the text so it is only alphanumeric characters, and lowercase
        plaintext = "".join(x.lower() for x in plaintext_unfiltered if x.isalpha())

        key = str(input("Input key permutation (e.g) 1: or e to exit:  "))

        encryptMessage(plaintext, key)

    if mode == "d":

        ciphertext_unfiltered = input("Enter ciphertext to decrypt: \n\n\n\n ")

        # Filters the text so it is only alphanumeric characters, and lowercase
        ciphertext = "".join(x.lower() for x in ciphertext_unfiltered if x.isalpha())

        keyKnown = str(input("Do you know the key? y for yes  n for no:   "))
        if keyKnown == "y":

            key = str(input("Input key permutation (e.g) 1234: or e to exit:  "))
            print(decryptMessage(ciphertext, key))

        else:
            bruteforce(ciphertext)


def encode(text, key):
    return encryptMessage(text, key)


def decode(text, key):
    return decryptMessage(text, key)


def crack(text):
    bruteforce(text)


if __name__ == "__main__":
    main()
