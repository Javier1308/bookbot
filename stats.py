def count_words(text):
    separated_words = text.split()
    count = len(separated_words)

    return count


def count_letters(text):
    text = text.lower().split()
    letter_count = dict()

    for word in text:
        for char in word:
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
