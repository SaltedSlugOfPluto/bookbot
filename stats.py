def get_num_words(text):
    return (len(text.split()))


def get_char_dict(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        char_dict[char] = 0
    
    for char in text:
        char_dict[char] += 1
    
    return char_dict


def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    new_dict = {}
    char_list = []
    for char in dict:
        new_dict[char] = {"char":char,"num":dict[char]}
        char_list.append(new_dict[char])

    char_list.sort(reverse=True,key=sort_on)
    return char_list