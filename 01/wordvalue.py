from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as dictionary_file:
        return [word.strip() for word in dictionary_file.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    words_to_value = {word: calc_word_value(word) for word in words}
    word_with_max_value = max(words_to_value.items(), key=lambda word_to_value: word_to_value[1])
    return word_with_max_value[0]

if __name__ == "__main__":
    pass # run unittests to validate
