alphabet = "abcdefghijklmnopqrstuvwxyz"

# Array containing the relative frequency of each letter in the English language
english_frequences = [
    0.08167,
    0.01492,
    0.02782,
    0.04253,
    0.12702,
    0.02228,
    0.02015,
    0.06094,
    0.06966,
    0.00153,
    0.00772,
    0.04025,
    0.02406,
    0.06749,
    0.07507,
    0.01929,
    0.00095,
    0.05987,
    0.06327,
    0.09056,
    0.02758,
    0.00978,
    0.02360,
    0.00150,
    0.01974,
    0.00074,
]

# Returns the Index of Coincidence for the "section" of ciphertext given
def get_index_c(ciphertext):

    N = float(len(ciphertext))
    frequency_sum = 0.0

    # Using Index of Coincidence formula
    for letter in alphabet:
        frequency_sum += ciphertext.count(letter) * (ciphertext.count(letter) - 1)

    # Using Index of Coincidence formula
    ic = frequency_sum / (N * (N - 1))
    print(ic)
    return ic


# displays most common letters for visual tool
# finds frequencies of every letter which can later be used
def ciphertext_frequencies(ciphertext, printed):

    frequencies = []

    for letter in alphabet:
        # adds frequencies to list
        frequencies.append(ciphertext.count(letter) / len(ciphertext))

    sorted_frequencies = sorted(frequencies, reverse=True)

    # displays table when necessary
    if printed:
        for i in range(0, 26):
            print(
                alphabet[i]
                + ": "
                + "Rank:"
                + str(sorted_frequencies.index(frequencies[i]) + 1)
                + "        "
                + str(frequencies[i])
            )
            sorted_frequencies[sorted_frequencies.index(frequencies[i])] = 2

    return frequencies


# takes user input and calls functions for frequencies and IC calculation
def main(ciphertext_unfiltered=None):

    chi_squared_sum = 0

    if ciphertext_unfiltered is None:
        ciphertext_unfiltered = input("Enter ciphertext to analyse: \n\n\n\n ")

    # Filters the text so it is only alphanumeric characters, and lowercase
    ciphertext = "".join(x.lower() for x in ciphertext_unfiltered if x.isalpha())

    ciphertext_frequencies(ciphertext, True)

    # an ic of bloew 0.055 generally considered to be polyalphabetic
    # ic above 0.06 indicates transposition or monoalphabetic sustitution
    if 0.055 < get_index_c(ciphertext) < 0.08:

        # compares frequencies found in ciphertext to the english language using the chi squared test
        for i in range(0, 25):
            chi_squared_sum += (
                (english_frequences[i] - ciphertext_frequencies(ciphertext, False)[i])
                ** 2
            ) / english_frequences[i]

        print(chi_squared_sum)

        # e is almost always the most common letter and a chi squared test result < 0.04 indicates it must be transposition

        if (
            max(ciphertext_frequencies(ciphertext, False))
            == (ciphertext_frequencies(ciphertext, False)[4])
            and chi_squared_sum < 1
        ):

            print(
                "It is probably a transposition cipher  \n . Attempting transposition decryption"
            )
        else:
            # it is therefore monoalphabetic substitution

            print(
                "It is probably a monoalphabetic substitution cipher \n. Attempting monoalphabetic decryption"
            )

    else:
        # it is therefore polyalphabetic substitution
        print("it is probably a polyalphabetic subsitution cipher")


if __name__ == "__main__":
    main()
