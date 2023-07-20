for i in range(10):
    for n in range(i + 1, 10):
        print(f"{i}{n}", end=", " if i < 8 else "\n")