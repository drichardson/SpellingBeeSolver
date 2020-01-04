#!/usr/bin/python3

import os
import sys

def load_words():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'english-words/words_alpha.txt')
    with open(path) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def solve(all_words, valid_letters, must_have_letter):
    """
    Return a list of words from all_words that:
      - are at least 4 letters long
      - are only composed of valid_letters
      - have must_have_letter at least once 
    
    all_words: an array of english words
    valid_letters: letters that can be used in the returned array
    must_have_letter: a letter that must appear i
    
    returns a list of words that meet the criteria.
    Note: does not remove proper nouns or cuss words, which are not allowed in NYT spelling bee.
    """
    for word in all_words:
        if len(word) < 4:
            continue
        if not all([letter in valid_letters for letter in word]):
            continue
        if not must_have_letter in word:
            continue
        yield word

def usage():
    print("""
    solve.py <letters> <must_have_letter>
    Usage:
      ./solve.py bawcokl l
    """)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    valid = sys.argv[1]
    must_have = sys.argv[2]

    if len(valid) != 7:
        print("letters must be 7 characters long")
        sys.exit(1)

    if len(must_have) != 1:
        print("must_have_letter must be 1 character long.")
        sys.exit(1)

    # print(f"valid: {valid}, must_have: {must_have}")
    english_words = load_words()
    print("\n".join(sorted(solve(english_words, valid, must_have))))
    # print(list(solve(["testing", "block", "lack", "howdy", "black", "wok", "law", "back"], "bawcokl", "l")))


