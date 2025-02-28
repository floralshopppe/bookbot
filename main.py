from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    dictionary = get_character_count(book_text)
    sorted_list = get_sorted_list_of_dictionaries(dictionary)
    number_of_words = get_num_words(book_text)
    print_report(book_path, number_of_words, sorted_list)


def print_report(book_path: str, number_of_words: str, sorted_list: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        character = dictionary["character"]
        value = dictionary["value"]
        if character.isalpha():
            print(f"{character}: {value}")

    print("============= END ===============")


main()
