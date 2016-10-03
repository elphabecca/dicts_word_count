# put your code here.

def wordcount(filename):
    """ """

    dict_word_counts = {}

    with open(filename) as da_file:

        for line in da_file: 
            line = line.rstrip()
            word_list = line.split()

            for word in word_list:
                dict_word_counts[word] = dict_word_counts.get(word, 0) + 1

    for word, count in dict_word_counts.items():
        print "%s: %d" % (word, count)

    return dict_word_counts

wordcount("twain.txt")