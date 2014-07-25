def sieve(n):
    x = 2
    a_list = list(range(x,n+1)) 
    while(x != n):
          for i in a_list:
            if i % x == 0 and i != x:
                a_list.remove(i)
            x = x+1
            return a_list


