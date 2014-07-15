def prime(n):
  n = abs(int(n))
  if n < 2 :
     return False
  if n == 2:
     return True
  if not n & 1:
     return False 
  for x in range(3, int(n**0.5)+1, 2):
     if n % x == 0:
        return False
  return True


def max_prime(usrnum):
    if prime(usrnum) == True:
        return usernum
    if usrnum >= 2:
        for i in range(2, int(usrnum)): 
            if prime(i) == True and not usrnum % i == 0 :
                x = i 
        return x
