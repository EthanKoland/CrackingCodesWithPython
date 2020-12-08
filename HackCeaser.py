def main():
    ind = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .?!"
    m = "iwx8Lx8L2!L8trt79L2t88pvt"
    for i in range(len(ind)):
        s = decText(m,i)
        
        print('Key: %d Message: %s' % (i, s))

def decText(m,k):
    ind = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .?!"
    o = ""
    for c in m:
        i = ind.find(c)
        i = i - k 
        if (i < 0):
            i = len(ind) + i
        o += ind[i]
    return o


main()