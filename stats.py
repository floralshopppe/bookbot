def get_book_text(book_path: str):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(book_path: str):
    book_text = get_book_text(book_path)
    num_words = len(book_text.split())
    return num_words
