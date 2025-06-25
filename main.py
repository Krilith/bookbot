#!/usr/bin/python3 -O
#starting script, contains debug options, add -O when script is in production

if __debug__:
    print("---start")

#list of global variables

file_contents = ""

#Functions

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return(file_contents)

def total_words(text):
    word_list = text.split()
    words = len(word_list)
    return words



def main():
    
    text = get_book_text("./books/frankenstein.txt")
    total = total_words(text)
    print(f"{total} words found in the document")
    pass





if __debug__:
    print("---call main")
main()
if __debug__:
    print("---end")