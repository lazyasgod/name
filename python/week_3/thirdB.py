def b_list():
    b_list = []
    with open("phone_book.txt") as f:
        for line in f:
             line = line.strip ('\n')
             (number, name) = line.split(" - ")
             number = int(number)
             b_tuple = (number, name)
             b_list.append(b.tuple)
    return b_list
