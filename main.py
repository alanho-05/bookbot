def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  chars_dict = get_char_dict(text)
  print(chars_dict)


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

main()
