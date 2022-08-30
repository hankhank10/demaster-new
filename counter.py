import sys

def add_one():
    current_count_int = 0

    a = open ("counter.txt", "r")
    current_count_str = a.read()
    current_count_int = int(current_count_str)
    a.close()

    current_count_int = current_count_int + 1

    b = open ("counter.txt", "w")
    b.write (str(current_count_int))
    b.close