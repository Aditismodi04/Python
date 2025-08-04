def missingDigit(s):
    part = s.split()
    a = part[0]
    op = part[1]
    b = part[2]
    c = part[4]
    for d1 in range(10):
        for d2 in range(10):
            aa =  a.replace("?",str(d1))
            bb = b.replace("?",str(d1))
            cc = c.replace("?",str(d2))
            if "?" in aa or "?" in bb or "?" in cc:
                continue
            try:
                n1 = int(aa)
                n2 = int(bb)
                n3 = int(cc)
                if op == "+" and n1 + n2 == n3:
                    return f'{d1}{d2}'
                elif op == "-" and n1 - n2 == n3:
                    return f'{d1}{d2}'
                elif op == "*" and n1 * n2 == n3:
                    return f'{d1}{d2}' 
                elif op == "/" and  n2 != 0 and n1 / n2 == n3:
                    return f'{d1}{d2}' 
            except:
                continue 
    return "no solution found"
print(missingDigit("20 / ? = 2?" ))                  
            
            
