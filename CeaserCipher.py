def main():
    m = "This is my secert message"
    k = 15
    
    out = ''
    encrypt = True
    decrypt = True
    if(encrypt):
        print(encText(m,k))
    if(decrypt):
        print(decText(encText(m,k),k))
    

def encText(t,k):
    o = ''
    ind = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 .?!"
    for c in t:
        i = ind.find(c)
        i += k 
        i %= len(ind)
        o += ind[i]
    return o

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