def make_word():
  words = input()
  word = ""
  for ch in words:
    word =word+ch
    yield word

print(list(make_word()))
