def Raise():
# You can raise exceptions by using the raise statement.
   print(1)
   raise ValueError
   print(2)

def Exception():
# Exceptions can be raised with arguments that give detail about them.
  name = "123"
  raise NameError("Invalid name!")


def Re_raised():
# Raise statement can be used without arguments to re-raise whatever exception occurred.
  try:
    num = 5 / 0
  except:
     print("An error occurred")
     raise

"""
 TRY TO RUN THESE FUNCTION ONE BY ONE & OBSERVE THE ERROR
Raise()
Exception()
Re_raised()
"""
