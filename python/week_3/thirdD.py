def a_dict():
    a_dict = {}
    with open("phone_book.txt") as f:
        for line in f:
            line = line.strip ('\n')
            (number, name) = line.split(" - ")
            a_dict[int(number)] = name
    return a_dict

def get_name(n):    #n is phone number
    phone_book = a_dict()
    if n in phone_book:
        x = phone_book[n]
        return x    #x is name
        


