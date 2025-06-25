#!/usr/bin/python3 

import sys
from stats import get_num_words, sort_output, get_num_letters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


#list of global variables

file_contents = ""

#Functions

def get_book_text(book):

    with open(book) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    
    text = get_book_text(sys.argv[1])
    total = get_num_words(text)
    letters = get_num_letters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")

    clean = sort_output(letters)

    for key, value in clean.items():
        print(f"{key}: {value}")

    print("============= END ===============")
    pass

main()