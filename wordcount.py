# put your code here.

def print_wordcount(filename):
    """Prints the word-count of each word in the given file. """

    dict_word_counts = {}

    with open(filename) as text:

        for line in text: 
            line = line.strip([ ,.:;?!()])
            word_list = line.split()

            for word in word_list:
                dict_word_counts[word] = dict_word_counts.get(word, 0) + 1

    for word, count in dict_word_counts.iteritems():
        print "%s: %d" % (word, count)

print_wordcount("twain.txt")