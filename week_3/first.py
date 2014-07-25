def is_number(x): 
    import re
    string = re.compile('^-?\d+\.?\d*$')
    isnumber = re.match(string,x)
    if isnumber:
       return True
    else:
       return False

print (is_number("asdf"))
