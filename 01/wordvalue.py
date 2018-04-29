from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        dictionaryList = f.read().split('\n')
        dictionaryList.remove('')
    return dictionaryList

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    split_by_letter = [letter for letter in word.upper()]

    for x in split_by_letter:
        for letter, score in LETTER_SCORES.items():
            if x == letter:
                # print(x, score)
                word_value += score
    # print(word_value)
    return word_value


def max_word_value(listas = DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_list = {}

    if listas == DICTIONARY:
        for word in load_words():
            # print(word)
            max_list[word] = calc_word_value(word.upper())
        return max(max_list, key = lambda key: max_list[key])

    else:
        for word in listas:
            max_list[word] = calc_word_value(word.upper())
        return max(max_list, key = lambda key: max_list[key])
        # print(max_list)
