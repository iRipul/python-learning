import pandas

# read csv and create dataframe
with open("nato_phonetic_alphabet.csv") as data:
    alpha_data = pandas.read_csv(data)

alpha_dict = {row.letter: row.code for (index, row) in alpha_data.iterrows()}

valid = False


def generate_phonetic():
    name = input("Type your name: ")
    try:
        result = [alpha_dict[letter.upper()] for letter in name]
    except KeyError:
        print("Sorry, please enter alphabets only")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
