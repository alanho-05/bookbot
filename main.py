def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  chars_dict = get_char_dict(text)
  chars_list = convert_to_list(chars_dict)
  print_report(book_path, chars_list, word_count)


def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_dict(text):
  chars = {}
  lower_cased = text.lower()
  for char in lower_cased:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

def print_report(book_path, chars_list, word_count):
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document\n")
  for char_dict in chars_list:
    print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")
  print("--- End report ---")

def sort_on(d):
  return d["num"]

def convert_to_list(num_dict):
  characters = []
  for char in num_dict:
    if char.isalpha():
      characters.append({"char": char, "num": num_dict[char]})
  characters.sort(key=sort_on, reverse=True)
  return characters

main()
