def main():
    book_path = "books/frankenstein.txt"
    text: str = get_book_text(book_path)
    num_words: int = get_num_words(text)
    chars_dict: dict[str, int] = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():  # type: ignore
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print()
    print("--- End report ---")


def get_num_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)


def sort_on(d: dict[str, int]) -> int:
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict[str, int]]:
    sorted_list: list[dict[str, int]] = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})  # type: ignore
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
