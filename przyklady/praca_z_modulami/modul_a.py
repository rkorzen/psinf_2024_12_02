a = 1

def add(a, b):
    return a + b


print(__name__)
if __name__ == "__main__":

    a = input("Podaj liczbe 1: ")
    b = input("Podaj liczbe 2: ")
    print(add(int(a), int(b)))

