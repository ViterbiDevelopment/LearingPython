def fab(maxNum): 
    n, a, b = 0, 0, 1 
    while n < maxNum: 
        yield b 
        a, b = b, a + b 
        n = n + 1 
 
f = fab(5)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()