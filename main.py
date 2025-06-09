from stats import count_words, count_letters, list_dictionaries
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 main.py <path_to_book>")

def get_book_text(filepath):
    with open(filepath) as f:
        read_data = f.read()
    
    return read_data

dictionaries = list_dictionaries(count_letters(get_book_text(sys.argv[1]))) 

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")

    for pair in dictionaries:
        if pair["char"].isalpha() == True: 
            print(f"{pair["char"]}: {pair["occurrence"]}")

    print("============= END ===============")

main()
