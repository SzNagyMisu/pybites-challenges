#Imports and appending path to reach beyond parent dir
import os, sys
sys.path.append('..')
from data import LETTER_SCORES, DICTIONARY 


#File path for Dictionary
fname = os.path.join('../',DICTIONARY)

#Wordlist from dictionary
def load_words() -> list:
    with open(fname,'r') as f:
        wordlist = f.read().split()
    return wordlist

#Calculate score word for word
def calc_word_value(word:str) -> int:
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    return score

#Just get the max out of the word list (any list)
def max_word_value(words:list=None) -> str:
    wordvalue_pair = list()
    #checking if given argument
    if words == None:
        wordlist = load_words()
    else:
        wordlist = words
    for word in wordlist:
        score = calc_word_value(word)
        wordvalue_pair.append( (word,score) )
    result = max(wordvalue_pair, key=lambda x: x[1])
    return result[0]


