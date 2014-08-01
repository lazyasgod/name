def a_dict():
    a_dict = {}
    with open("phone_book.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (number, name) = line.split(" - ")
            a_dict[int(number)] = name
    return a_dict

