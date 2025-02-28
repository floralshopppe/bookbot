def get_book_text(book_path: str):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
