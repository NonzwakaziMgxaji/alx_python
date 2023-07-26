def add(a, b):
    return a + b


if __name__ == "__main__":
    add_0 = add
    a = 1
    b = 2
    result = add_0(a, b)
    print("{} + {} = {}\n".format(a, b, result))
