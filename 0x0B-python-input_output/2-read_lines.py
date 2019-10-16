#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        nl = 0
        for line in f:
            nl += 1
        f.seek(0, 0)
        if nb_lines <= 0 or nb_lines >= nl:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
