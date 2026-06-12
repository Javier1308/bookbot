from stats import count_words, count_letters, list_dictionaries, chars_dict_to_sorted_list

filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        read_data = f.read()
    
    return read_data

dictionaries = list_dictionaries(count_letters(get_book_text(filepath))) 

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(filepath))} total words")
    print("--------- Sorted Character List -------")
    print(f"{chars_dict_to_sorted_list(count_letters(get_book_text(filepath)))}")
    print("--------- Character Count -------")

    for pair in dictionaries:
        if pair["char"].isalpha() == True: 
            print(f"{pair['char']}: {pair['occurrence']}")

    print("============= END ===============")

main()
