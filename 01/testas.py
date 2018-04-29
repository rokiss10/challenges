from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        dictionaryList = f.read().split('\n')
    return dictionaryList

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    split_by_letter = [letter for letter in word]

    for x in split_by_letter:
        for letter, score in LETTER_SCORES.items():
            if x == letter:
                print(x, score)
                word_value += score
    return word_value

# for word in load_words()[:5]:
#     print(word.upper())

def max_word_value(func, listas = DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if listas == DICTIONARY:
        for word in load_words()[:10]:
            # print(word)
            calc_word_value(word.upper())
            print('\n')
    else:
        for word in listas:
            calc_word_value(word)
            max_list.append(word)
        print(max(max_list))

print(max_word_value(calc_word_value))