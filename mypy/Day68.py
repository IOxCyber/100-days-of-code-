def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

@decor
def print_text():
    print("Hello world,I'm here!")

print_text();
