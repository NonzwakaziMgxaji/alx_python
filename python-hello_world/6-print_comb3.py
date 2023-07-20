
for i in range(10):
    for n in range(i + 1, 10):
        print("{:02d}".format(i * 10 + n), end=", " if i < 8 or n < 9 else "\n")
