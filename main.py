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

    print(f"{total} words found in the document")


    print(sort_output(letters))
    pass





if __debug__:
    print("---call main")
main()
if __debug__:
    print("---end")