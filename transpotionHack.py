import math

def main():
    s = "Cenoonommctmme oo snnio s S C"
    
    for key in range(2, len(s)):
        temp = {}
        for i in range(len(s)):
            temp[i] = s[i]
   
        arr = createArray(key, s)
    
        for col in range(len(arr)):
            for row in range(len(arr[col])):
                arr[col][row] = (temp[arr[col][row]])
                #print(col + row * int(len(s)/key), temp[col + row * int(len(s)/key)])
                pass
        final = ""
        for col in range(len(arr)):
            for row in range(len(arr[col])):
                final += arr[col][row]
        print(final)


        

def createArray(key,s):
    i = len(s)
    
    out = []
    while(i != 0):
        if(i > key):
            out.append([''] * key)
            i -= key
        else:
            out.append(['']*i + ['skip'] *( key - i))
            
            i = 0
    
    c = 0
    
    for row in range(len(out[0])):
        for col in range(len(out)):
            if(out[col][row] != 'skip'):
                out[col][row] = c
                c+=1
                
    
    for col in range(len(out)):
        rm = 0
        for row in range(len(out[col])):
            if(out[col][row - rm] == 'skip'):
                
                out[col].pop(row - rm)
                rm += 1
    
    return out
            

    
            
        

    
        
        




if __name__ == "__main__":


    main()