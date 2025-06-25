#counts word total from string
def get_num_words(text):

    word_list = text.split()
    words = len(word_list)
    return words

#counts character total from sting
def get_num_letters(text):

    text_counts = {}
    text = text.lower()
    letters = list(text)
    unique_list = set(letters)

    for each in unique_list:
        if each.isalpha() == True:
            ammount = text.count(each)
            text_counts[each] = ammount

    return text_counts

#sorts the output 
def sort_output(text):

    sorted_items = sorted(text.items(), key=lambda item: item[1], reverse = True)
    sorted_dict = dict(sorted_items)

    return(sorted_dict)