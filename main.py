def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
    

def count_words(text):
    words = text.split()
    return len(words)


def main():
    book_path = './books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f'Found {num_words} total words')


if __name__ == '__main__':
    main()