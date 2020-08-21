#!/usr/bin/env python3

'''
This program reads in a multi-character string, usually containing long runs of the same character.
It then performs run-length encoding on it such that runs of characters are denoted (c, char), where c is the
integer count of char
These are output as sequential tuples to the user

The program features two functions that perform the same task.
basic_compressor uses a less efficient method whereby the string is iterated through sequentally and characters
are counted one by one
advanced_compressor uses itertools.groupby to split the string into a list of iterators, the lengths of which are
then calculated and output.

Both functions are called and their respective execution times are output. advanced_compressor performs about 20% faster
'''

from itertools import groupby
from timeit import default_timer

class Compressor:
    
    @staticmethod
    def basic_compressor(line):
        if not isinstance(line, str) or line == "":
            return "Invalid input!"

        all_chars = iter(line)
        current = next(all_chars)
        count = 1
        output = ""

        while current:
            try:
                next_char = next(all_chars)
            except StopIteration:
                output += "({}, {})".format(count, current)
                break
            if next_char == current:
                count += 1
            else:
                output += "({}, {}) ".format(count, current)
                count = 1
            current = next_char

        return output

    @staticmethod
    def advanced_compressor(line):
        if not isinstance(line, str) or line == "":
            return "Invalid input!"

        output = ""
        # groupby(line) returns a group of iterators, with each iterator containing each unique element that appears in a consecutive order
        # for example, 112221 would return [['1', '1'], ['2', '2', '2'], ['1']] as an iterator
        # this can be cast to a list using list(g)
        # k represents the key of that list/iterator, so the key for the first list would be '1'
        grouped = [list(g) for k, g in groupby(line)]
        for item in grouped:
            output += "({}, {}) ".format(len(item), item[0])
        return output[:-1]

def compress_and_time():
    line = input("Please enter a string of characters:\n")
    start = default_timer()
    print(Compressor.basic_compressor(line))
    end = default_timer()
    brun = end - start
    start = default_timer()
    print(Compressor.advanced_compressor(line))
    end = default_timer()
    arun = end - start
    print("\nBasic runtime: {} seconds".format(brun))
    print("Advanced runtime: {} seconds".format(arun))


if __name__ == "__main__":
    compress_and_time()
    exit(0)
