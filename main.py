import sys
from stats import count_words
from stats import count_chars
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    #Confirm there are two args
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    # Code from prior lesson, works just fine
    book_text = get_book_text(book_path)
    number_of_words = count_words(book_text)
    character_count = count_chars(book_text)

    #Current lesson doesn't want this printed
    #print(f"Found {number_of_words} total words")
    #print(character_count)

    #Code for current lesson, unverified
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    list_of_char_dicts = sort_dict(character_count)

    for char_dict in list_of_char_dicts:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")
main()