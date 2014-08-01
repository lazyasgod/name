def phone_book(n):
    import random
    import string
    phone_book = {}
    book_size = n
    while len(phone_book) < book_size:
        number = random.randint(0000000, 9999999)
        if number not in phone_book:
            name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(4,10)))
            phone_book[number] = name
            file = str(number) + str(' - ') + str(name) + str("\n")
            with open('phone_book.txt', 'a') as f:
                f.write(file)
    return phone_book

phone_book(100000)
