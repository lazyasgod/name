def prime(n):
  n = abs(int(n))
  if n <= 2: 
    return n == 2
  for x in range(3, int(sqrt(n))+1, 2):
     if n % x == 0:
        return False
  return True


def max_prime(usrnum):
    if prime(usrnum) == True:
        return usernum
    if usrnum >= 2:
        for i in range(int(usrnum), 2): 
            if prime(i) == True and not usrnum % i == 0 :
                x = i 
        return x
