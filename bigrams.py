#!/usr/bin/env python2


import sys
import itertools
from io import open


def second(x):
    return x[1]

def main():
    try:
        bigrams = {}
        with open(sys.argv[1]) as f:
            words = f.read().split()
            for bigram in zip(words, words[1:]):
                if bigram in bigrams:
                    bigrams[bigram] += 1
                else:
                    bigrams[bigram] = 1
        for pair, freq in itertools.islice(sorted(
            list(bigrams.items()), key=second, reverse=True), 10):
            print(':'.join(pair), 'appears', freq, 'times')
    except IOError as e:
        print(str(e))
    except IndexError:
        print('File argument is required!')

if __name__ == '__main__':
    main()
