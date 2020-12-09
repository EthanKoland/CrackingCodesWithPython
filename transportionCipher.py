def main():
    k = 9
    s = "Common Sence is not so Common"
    print(encrypt(k,s))
    
def encrypt(k, s):
    out = []
    temp = []
    for i in range(len(s)):
        temp.append(s[i])
        if(len(temp) > (k - 1)):
            out.append(temp)
            temp = []

   
    
    out.append(temp)
    for line in out:
        print(line)

    final = ""
    for i in range(len(out[0])):
        for t in range(len(out)):
            if (i < len(out[t])):
                final += out[t][i]
    return(final)
        


if (__name__ == "__main__"):
    main()

