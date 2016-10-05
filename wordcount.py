# http://fellowship.hackbrightacademy.com/materials/f16a/exercises/dicts-word-count/further-study.html

# put your code here.

import sys
import collections

filename = sys.argv[1]

# def print_wordcount(filename):
#     """Prints the word-count of each word in the given file. """

#     dict_word_counts = {}

#     with open(filename) as text:

#         for line in text: 
#             line = line.rstrip()
#             word_list = line.split()

#             for word in word_list:

#                 word = ''.join(char for char in word if char.isalnum())
#                 word = word.lower()

#                 dict_word_counts[word] = dict_word_counts.get(word, 0) + 1

#     for word, count in dict_word_counts.iteritems():
#         print "%s: %d" % (word, count)


# print_wordcount(filename)

def print_wordcount(filename):
    """Prints the word-count of each word in the given file. """

    dict_word_counts = {}

    with open(filename) as text:

        text = text.read()
        print text

    #         for word in word_list:

    #             word = ''.join(char for char in word if char.isalnum())
    #             word = word.lower()

    #             full_count = collections.Counter(word)

    # return full_count

print_wordcount(filename)
