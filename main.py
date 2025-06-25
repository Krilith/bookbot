#!/usr/bin/python3 -O
#starting script, contains debug options, add -O when script is in production

from stats import get_num_words, sort_output, get_num_letters

if __debug__:
    print("---start")

#list of global variables

file_contents = ""

#Functions

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return(file_contents)





def main():
    
    text = get_book_text("./books/frankenstein.txt")
    total = get_num_words(text)
    letters = get_num_letters(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    clean = sort_output(letters)
    for key, value in clean.items():
        print(f"{key}: {value}")


    print("============= END ===============")
    pass





if __debug__:
    print("---call main")
main()
if __debug__:
    print("---end")