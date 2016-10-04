# put your code here.

import sys

filename = sys.argv[1]

def print_wordcount(filename):
    """Prints the word-count of each word in the given file. """

    dict_word_counts = {}

    with open(filename) as text:

        for line in text: 
            line = line.rstrip()
            word_list = line.split()

            for word in word_list:
                # FORMAT WORD
                dict_word_counts[word] = dict_word_counts.get(word, 0) + 1

    for word, count in dict_word_counts.iteritems():
        print "%s: %d" % (word, count)

def format_word(word):
    
    evil_chars = (",", "'")

    for char in word:
        print char
        if char in evil_chars:
            print char
        else:
            print "Skip"


# print_wordcount(filename)