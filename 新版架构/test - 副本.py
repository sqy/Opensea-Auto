def a():
    global b
    b = 1 + c

def b():
    global c
    c = 1

if __name__ == "__main__":
    b()
    a()
    print(b)