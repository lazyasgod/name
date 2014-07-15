def input_int(a, b):
    while True:
        x = input("put a number >")
        if x.isdigit() and a <= int(x) <= b:
            break
        elif not x.isdigit() or a >= int(x) >= b :
            print ("put a number from " + str(a) +" to " + str(b))
        else: 
            print ("error")

input_int(1,100)
