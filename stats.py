def get_book_text(book_path: str):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(book_path: str):
    book_text = get_book_text(book_path)
    num_words = len(book_text.split())
    return num_words


def get_character_count(book_text: str):
    character_dict = {}
    for character in book_text:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_on(dictionary: dict):
    return dictionary["value"]


def get_sorted_list_of_dictionaries(dictionary: dict):
    list = []
    for character in dictionary:
        value = dictionary[character]
        list.append({"character": character, "value": value})
    list.sort(reverse=True, key=sort_on)
    return list
