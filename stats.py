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
        ammount = text.count(each)
        text_counts[each] = ammount




    return text_counts