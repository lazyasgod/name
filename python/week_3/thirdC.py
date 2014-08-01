def c_list():
    c_list = []
    with open("phone_book.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (number, name) = line.split(" - ")
            number = int(number)
            c_tuple = (number, name)
            c_list.append(c_tuple)

    final_list = sorted(c_list, key=lambda tup: tup[0])
    return final_list
