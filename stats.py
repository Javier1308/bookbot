def count_words(text):
    separated_words = text.split()
    count = len(separated_words)

    return count

def count_letters(text):
    text = text.lower()
    letter_count = dict()
    for char in text: 
        if char not in letter_count: 
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count
    

def sort_on(dict):
    return dict["occurrence"]


def list_dictionaries(letter_count):
    dictionaries = []

    for key in letter_count:
        pair = {"char": key, "occurrence": letter_count[key]}
        dictionaries.append(pair)

    
    dictionaries.sort(key=sort_on, reverse=True)

    return dictionaries


def sort_on_tuple(tuple: tuple[str, int]) -> int:
    return tuple[1]

def chars_dict_to_sorted_list(dictionary: dict[str, int]) -> list[tuple[str, int]]:
    list = []
    for key, value in dictionary.items():
        list.append((key, value))
    
    sorted_list = sorted(list, key=sort_on_tuple, reverse=True)
    
    return sorted_list