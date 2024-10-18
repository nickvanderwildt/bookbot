def main():
    book_path = "books/frankenstein.txt"

    text: str = get_book_text(book_path)
    # print(text)

    num_words: int = get_num_words(text)
    print(f"{num_words} words found in the document")

    chars_dict: dict[str, int] = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars_dict: dict[str, int] = {}
    for char in text.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
