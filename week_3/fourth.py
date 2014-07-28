def my_map(func, a_list):
    b_list = []
    for i in a_list:
        b_list.append(func(i))
    return b_list

def my_filter(func, a_list):
    b_list = []
    for i in a_list:
        if func(i):
            b_list.append(i)
    return b_list
