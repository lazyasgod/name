def max_prime():
   min_prime = 3                 
   usrnum = int(input("put number >"))     
   x = []
   while min_prime <= usrnum:
      if usrnum % min_prime == 0:
         x.append(min_prime)    
         usrnum = usrnum/min_prime
      else:
         min_prime = min_prime + 2     
   print ("max prime =", max(x))

max_prime()
