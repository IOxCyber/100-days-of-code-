#yield
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

#Yield into list
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11))) 
 
 #example
 def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
 
 
"""check out theory:
   https://github.com/SaranshChauhan/TheFuture-sTheory/new/master/pypy"""
