def main():
    k = 8
    s = "Common Sence is not so Common"
    out = []
    temp = []
    for i in range(len(s)):
        temp.append(s[i])
        if(len(temp) > 7):
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
    print(final + "|")
        


main()
