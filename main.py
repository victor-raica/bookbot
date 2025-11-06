from stats import count_words
from stats import count_chars
from stats import sort_char_count
import sys


def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
    

def main():
    header = '============ BOOKBOT ============'
    word_count_header = '----------- Word Count ----------'
    character_count_header = '--------- Character Count -------'
    end_header = '============= END ==============='

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_count = count_chars(book_text)

    print(header)
    print(f'Analyzing book found at {book_path}')
    print(word_count_header)
    print(f'Found {num_words} total words')
    print(character_count_header)
    for item in sort_char_count(chars_count):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print(end_header)


if __name__ == '__main__':
    main()